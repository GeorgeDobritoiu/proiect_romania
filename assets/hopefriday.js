(() => {
 const form=document.getElementById('sponsor-calculator'); if(!form)return;
 const output=document.getElementById('sponsor-result');
 const money=n=>new Intl.NumberFormat('ro-RO',{style:'currency',currency:'RON'}).format(n);
 form.addEventListener('submit',e=>{
  e.preventDefault();
  const regime=form.elements.regime.value;
  if(regime!=='profit'&&regime!=='estimate'){output.textContent=regime==='micro'?'Microîntreprinderile pot sponsoriza din fonduri proprii, dar nu beneficiază de acest credit fiscal.':'Pentru IMCA, grupuri fiscale sau alte regimuri speciale, calculul se verifică separat cu contabilul. Acest calculator nu stabilește suma eligibilă.';return;}
  const values=['turnover','tax','used','carried'].map(k=>Number(form.elements[k].value));
  if(values.some(n=>!Number.isFinite(n)||n<0)){output.textContent='Introdu sume valide, pozitive sau zero.';return;}
  let [turnover,tax,used,carried]=values;
  if(regime==='estimate'){const gross=Number(form.elements.gross.value);if(!Number.isFinite(gross)||gross<0){output.textContent='Introdu un profit contabil brut valid.';return;}if(gross===0){output.textContent='Profitul contabil brut introdus este zero. Verifică la firma de contabilitate dacă există impozit pe profit datorat și plafon disponibil pentru sponsorizări. Sponsorizările din fonduri proprii se pot acorda în condițiile legii, fără facilitate fiscală.';return;}tax=gross*.16;}
  const cap=Math.min(turnover*.0075,tax*.2),available=Math.max(0,cap-used-carried);
  output.textContent=(regime==='estimate'?'ESTIMARE DIN BILANȚ: presupunem profit contabil brut egal cu profitul impozabil și cotă de 16%. Cere firmei de contabilitate suma exactă disponibilă. ':'')+`Plafon general: ${money(cap)}. Disponibil estimat: ${money(available)}. Limita cifrei de afaceri: ${money(turnover*.0075)}; limita impozitului: ${money(tax*.2)}. ${used+carried>cap?'Sumele utilizate și reportate depășesc plafonul calculat; verifică datele cu contabilul. ':''}Estimarea presupune date complete pentru același an fiscal și eligibilitate confirmată de contabil. Plafonul privește facilitatea fiscală, nu o limită a donațiilor din fonduri proprii.`;
 });
})();
(() => {
 const lookup=document.getElementById('anaf-lookup');if(!lookup)return;
 const status=document.getElementById('anaf-status'),form=document.getElementById('sponsor-calculator');
 lookup.addEventListener('submit',async e=>{
  e.preventDefault();const button=lookup.querySelector('button');button.disabled=true;
  // Clear previous company data so an unsuccessful search cannot retain its estimate.
  form.elements.turnover.value='';form.elements.gross.value='0';form.elements.tax.value='0';form.elements.used.value='0';form.elements.carried.value='0';document.getElementById('sponsor-result').textContent='Se verifică bilanțul. Estimarea anterioară a fost eliminată.';
  status.textContent='Se caută în baza publică ANAF…';
  try{
   const response=await fetch('/api/anaf-bilant?'+new URLSearchParams({cui:lookup.elements.cui.value,year:lookup.elements.year.value}));const data=await response.json();if(!response.ok)throw Error(data.error||'Serviciul nu a răspuns.');
   form.elements.turnover.value=data.turnover;form.elements.gross.value=data.grossProfit;form.elements.regime.value='estimate';
   status.textContent=`${data.name} · CUI ${data.cui} · anul ${data.year} · sursa: ANAF. Cifra de afaceri: ${data.turnover.toLocaleString('ro-RO')} lei; profit contabil brut: ${data.grossProfit.toLocaleString('ro-RO')} lei${data.grossLoss?`; pierdere contabilă brută: ${data.grossLoss.toLocaleString('ro-RO')} lei`:''}. Estimarea presupune regim general de impozit pe profit și plafon neutilizat; confirmă la contabil. Pentru 2025, termenul obișnuit al formularului 177 a trecut; calculul este informativ.`;
   form.requestSubmit();
  }catch(error){status.textContent=error.message;document.getElementById('sponsor-result').textContent='Estimarea automată nu este disponibilă. Poți introduce manual datele confirmate de contabil.';}
  finally{button.disabled=false;}
 });
})();
