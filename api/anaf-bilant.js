// Official public annual financial statements. Never requests private SPV data.
const cache=new Map();let tail=Promise.resolve(),last=0;
const normalize=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/\s+/g,' ').trim();
function parse(data,cui,year){
 if(!data||Number(data.cui)!==Number(cui)||Number(data.an)!==year||!Array.isArray(data.i))throw Error('shape');
 const get=labels=>{const row=data.i.find(r=>labels.includes(normalize(r.val_den_indicator)));if(!row||row.val_indicator===null||row.val_indicator==='')return null;const v=Number(row.val_indicator);return Number.isFinite(v)&&v>=0?v:null;};
 const turnover=get(['cifra de afaceri neta','cifra de afaceri']),profit=get(['profit brut']),loss=get(['pierdere bruta']);
 if(turnover===null||(profit===null&&!(loss>0)))throw Error('indicators');
 return {cui:String(cui),year,name:String(data.deni||''),turnover,grossProfit:profit===null?0:profit,grossLoss:loss,source:'ANAF',fetchedAt:new Date().toISOString()};
}
async function handler(req,res){
 res.setHeader('Cache-Control','no-store');
 if(req.method!=='GET')return res.status(405).json({error:'Metodă neacceptată.'});
 const cui=String(req.query.cui||'').trim().replace(/^RO/i,'').trim(),year=Number(req.query.year);
 if(!/^\d{2,10}$/.test(cui)||!Number.isInteger(year)||year<2014||year>=new Date().getUTCFullYear())return res.status(400).json({error:'Introdu un CUI valid și un an fiscal încheiat.'});
 const key=cui+':'+year,old=cache.get(key);if(old&&Date.now()-old.time<86400000)return res.status(200).json(old.value);
 const job=tail.then(async()=>{await new Promise(r=>setTimeout(r,Math.max(0,1100-(Date.now()-last))));last=Date.now();const upstream=await fetch(`https://webservicesp.anaf.ro/bilant?an=${year}&cui=${cui}`,{signal:AbortSignal.timeout(18000),headers:{Accept:'application/json'}});if(!upstream.ok)throw Error('upstream');const value=parse(await upstream.json(),cui,year);if(cache.size>=1000)cache.delete(cache.keys().next().value);cache.set(key,{time:Date.now(),value});return value;});
 tail=job.catch(()=>{});
 try{return res.status(200).json(await job);}catch{return res.status(502).json({error:'ANAF nu a returnat un bilanț utilizabil pentru CUI-ul și anul selectate. Încearcă mai târziu sau completează datele confirmate de contabil. Suma nu poate fi estimată automat.'});}
}
module.exports=handler;module.exports.parse=parse;
