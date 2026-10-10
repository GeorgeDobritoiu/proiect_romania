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
  if(regime==='estimate'){const gross=Number(form.elements.gross.value);if(!Number.isFinite(gross)||gross<0){output.textContent='Introdu un profit contabil brut valid.';return;}if(gross===0){output.textContent='Profitul contabil brut introdus este zero. Verifică la firma de contabilitate dacă există impozit pe profit datorat și plafon disponibil pentru sponsorizări. Sponsorizările din fonduri proprii se pot acorda în condițiile legii, fără facilitate fiscală.';return;}tax=gross*.16;form.elements.tax.value=tax.toFixed(2);}
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
   const response=await fetch('/api/anaf-bilant?'+new URLSearchParams({cui:lookup.elements.cui.value,year:lookup.elements.year.value}),{signal:AbortSignal.timeout(25000)});const data=await response.json();if(!response.ok)throw Error(data.error||'Serviciul nu a răspuns.');
   form.elements.turnover.value=data.turnover;form.elements.gross.value=data.grossProfit;form.elements.regime.value='estimate';form.elements.tax.value=(data.grossProfit*.16).toFixed(2);
   const contact=document.getElementById('hope-contact');if(contact){contact.elements.organisation.value=data.name;contact.elements.cui.value=data.cui;}
   status.textContent=`${data.name} · CUI ${data.cui} · anul ${data.year} · sursa: ANAF. Cifra de afaceri: ${data.turnover.toLocaleString('ro-RO')} lei; profit contabil brut: ${data.grossProfit.toLocaleString('ro-RO')} lei${data.grossLoss?`; pierdere contabilă brută: ${data.grossLoss.toLocaleString('ro-RO')} lei`:''}. Estimarea presupune regim general de impozit pe profit și plafon neutilizat; confirmă la contabil. Pentru 2025, termenul obișnuit al formularului 177 a trecut; calculul este informativ.`;
   form.requestSubmit();
  }catch(error){status.textContent=error.name==='TimeoutError'?'ANAF răspunde prea lent. Încearcă din nou mai târziu.':error.message;document.getElementById('sponsor-result').textContent='Estimarea automată nu este disponibilă. Poți introduce manual datele confirmate de contabil.';}
  finally{button.disabled=false;}
 });
})();
(() => {
 const calc=document.getElementById('sponsor-calculator');
 if(calc){const sync=()=>{const estimate=calc.elements.regime.value==='estimate';calc.elements.tax.readOnly=estimate;if(estimate){const gross=Number(calc.elements.gross.value);calc.elements.tax.value=Number.isFinite(gross)?(gross*.16).toFixed(2):'0';}};calc.elements.regime.addEventListener('change',sync);calc.elements.gross.addEventListener('input',sync);sync();}
 const form=document.getElementById('hope-contact');if(!form)return;
 form.addEventListener('submit',event=>{
  event.preventDefault();if(!form.reportValidity())return;
  const data=new FormData(form),value=k=>String(data.get(k)||'').trim();
  const text=`Salut, George! Doresc să particip la HopeFriday.\n\nTip: ${value('kind')}\nOrganizație: ${value('organisation')}\nCUI: ${value('cui')}\nPersoană de contact: ${value('person')}\nE-mail: ${value('email')}\nSite: ${value('website')||'Neprecizat'}\n\nPrezentare:\n${value('presentation')}\n\nContribuție propusă:\n${value('contribution')}\n\nSpațiu de prezentare: ${data.has('publish')?'Solicitat; publicarea se face după confirmarea textului final.':'Nu este solicitat acum.'}`;
  const email=event.submitter?.value==='email';
  if(email)window.location.href='mailto:salut@proiectromania.ro?subject='+encodeURIComponent('HopeFriday — participare: '+value('organisation'))+'&body='+encodeURIComponent(text);
  else window.open('https://wa.me/40722565555?text='+encodeURIComponent(text),'_blank','noopener,noreferrer');
  document.getElementById('hope-contact-status').textContent='Mesajul este pregătit. Verifică-l și trimite-l în aplicația aleasă; formularul nu l-a expediat automat.';
 });
})();
