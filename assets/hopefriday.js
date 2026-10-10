(() => {
 const form=document.getElementById('sponsor-calculator'); if(!form)return;
 const output=document.getElementById('sponsor-result');
 const money=n=>new Intl.NumberFormat('ro-RO',{style:'currency',currency:'RON'}).format(n);
 form.addEventListener('submit',e=>{
  e.preventDefault();
  const regime=form.elements.regime.value;
  if(regime!=='profit'){output.textContent=regime==='micro'?'Microîntreprinderile pot sponsoriza din fonduri proprii, dar nu beneficiază de acest credit fiscal.':'Pentru IMCA, grupuri fiscale sau alte regimuri speciale, calculul se verifică separat cu contabilul. Acest calculator nu stabilește suma eligibilă.';return;}
  const values=['turnover','tax','used','carried'].map(k=>Number(form.elements[k].value));
  if(values.some(n=>!Number.isFinite(n)||n<0)){output.textContent='Introdu sume valide, pozitive sau zero.';return;}
  const [turnover,tax,used,carried]=values,cap=Math.min(turnover*.0075,tax*.2),available=Math.max(0,cap-used-carried);
  output.textContent=`Plafon general: ${money(cap)}. Disponibil estimat: ${money(available)}. Limita cifrei de afaceri: ${money(turnover*.0075)}; limita impozitului: ${money(tax*.2)}. ${used+carried>cap?'Sumele utilizate și reportate depășesc plafonul calculat; verifică datele cu contabilul. ':''}Estimarea presupune date complete pentru același an fiscal și eligibilitate confirmată de contabil. Plafonul privește facilitatea fiscală, nu o limită a donațiilor din fonduri proprii.`;
 });
})();
