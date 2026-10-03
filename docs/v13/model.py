import json, math
from pathlib import Path
P=Path('/workspace/scratch/9e81b6b71a6d/v13-extins')
rows=[
('Manager proiect',21,2200,'luni','Coordonare pe întreaga durată'),
('Sprijin financiar cu timp parțial',21,750,'luni','Contabilitate și control documente'),
('Coordonator local',12,2000,'luni','Activitate comunitară'),
('Trei mentori tehnici cu timp parțial',36,1100,'persoană-luni','12 luni pentru fiecare mentor'),
('Responsabil protecția copilului cu timp parțial',21,900,'luni','Prevenție, consultare și circuit de sesizare'),
('Acces la șase baze',72,250,'bază-luni','Cost incremental în bani, nu chirie de piață integrală'),
('Echipament comun pentru echipe',25,600,'pachete','Bunuri inventariate'),
('Pachet individual de bază',400,35,'copii','Necesarul suplimentar se validează'),
('Transport local țintit',12,1400,'luni','Rute și contracte de validat'),
('Festivaluri și activități comune',12,700,'luni','Include suport arbitraj aferent'),
('Asigurări',400,15,'copii','Reper de ofertare, acoperirea se confirmă'),
('Fond adaptări și incluziune',1,4000,'pachet','Peste sprijinul deja inclus la transport'),
('Configurare instrument digital minim',1,15000,'pachet','Nu include o platformă națională nouă'),
('Servicii digitale recurente',21,180,'luni','Găzduire, suport și instrumente'),
('Evaluare independentă',1,12000,'pachet','Inițială, intermediară și finală'),
('Juridic și proceduri achiziții',1,6000,'pachet','Validare documente și proceduri'),
('Comunicare și recrutare',1,4000,'pachet','Materiale și întâlniri locale'),
('Audit financiar final',1,6000,'pachet','Separat de evaluarea rezultatelor'),
('Programa formatorilor',1,9000,'pachet','Design și adaptare pe specializări'),
('Experți pentru formatori',30,300,'zile','Zile efective contractate'),
('Logistică formatori',1,6000,'pachet','Întâlniri regionale; nu două șederi lungi pentru toți'),
('Materiale pentru formatori',12,300,'candidați','Materiale și acces la resurse'),
('Evaluare formatori',12,400,'candidați','Probe și feedback independent'),
('Mentorat pentru formatori',12,400,'candidați','Practică de predare, distinctă de mentorii echipelor'),
('Instruire practicieni locali',60,120,'participanți','Cost incremental; licențe suplimentare după ofertă'),
]
subtotal=sum(q*u for _,q,u,_,_ in rows); reserve=math.ceil(subtotal*.15); total=subtotal+reserve
print(subtotal,reserve,total)
def money(x):return f'{x:,.0f}'.replace(',','.')
parts={}
parts['PILOT_TABLE']='| Linie | Cantitate × cost unitar | Total EUR |\n'+ '\n'.join(f'| {n} | {q} {unit} × {money(u)} | {money(q*u)} |' for n,q,u,unit,note in rows)+f'\n| Total înainte de rezervă | | {money(subtotal)} |\n| Rezervă 15% | | {money(reserve)} |\n| Plafon orientativ în bani | | {money(total)} |'
parts['PILOT_NOTES']='\n\n'.join(f'{n}: {note}.' for n,q,u,unit,note in rows if note)
parts['PILOT_TOTAL']=money(total)
parts['PILOT_SUBTOTAL']=money(subtotal)
# Tranches sum 100%, reserve separately
parts['CASH_TABLE']='| Fază | Bază EUR | Rezervă disponibilă EUR | Condiție |\n'+ '\n'.join(f'| {name} | {money(subtotal*pct)} | {money(reserve*r)} | {gate} |' for name,pct,r,gate in [('Lunile 1–3',.18,.10,'Diagnostic și acorduri'),('Lunile 4–6',.22,.20,'Personal și pregătire de deschidere'),('Lunile 7–12',.27,.30,'Primele șase luni de activitate'),('Lunile 13–18',.25,.30,'Continuarea sezonului'),('Lunile 19–21',.08,.10,'Evaluare și închidere')])
# cash steady unit components sum 420
unit=[('Pregătire și mentorat local',150),('Acces și exploatare spații',80),('Transport și acces',65),('Echipament și consumabile',45),('Activități și arbitraj',30),('Formare continuă',25),('Asigurări și sprijin incluziune',25)]
assert sum(v for _,v in unit)==420
parts['UNIT_TABLE']='| Componentă recurentă | EUR pe loc ocupat și an |\n'+'\n'.join(f'| {k} | {v} |' for k,v in unit)+'\n| Total variabil de referință | 420 |'
scens={'Prudent':[400,1200,2500,5000,8000,12000,16000,20000,25000,30000,35000], 'Referință':[400,2000,5000,10000,18000,28000,40000,55000,70000,85000,100000], 'Accelerat':[400,3000,8000,16000,28000,42000,60000,80000,100000,125000,150000]}
allrows=[]
for name,nums in scens.items():
 last=400; rr=[]
 for year,n in zip(range(2030,2041),nums):
  hubs=math.ceil(n/2000);add=max(0,n-last)
  central=300000+100000*max(0,math.ceil(n/50000)-1)
  operating=n*420+hubs*60000+central
  onboard=add*100
  totaly=1.10*(operating+onboard)
  nominal=totaly*1.025**(year-2026)
  econ=totaly+120*n
  rr.append(dict(year=year,n=n,hubs=hubs,new=add,operating=operating,onboard=onboard,cash=totaly,nominal=nominal,economic=econ,active=.75*n,teams=math.ceil(n/16),adults=math.ceil(n/16)*2.4,mentors=math.ceil(math.ceil(n/16)/10)))
  last=n
 parts['SCEN_'+name]='| An | Locuri ocupate | Centre de suport | Bani EUR 2026 | Bani nominali EUR |\n'+'\n'.join(f'| {r["year"]} | {money(r["n"])} | {r["hubs"]} | {money(r["cash"])} | {money(r["nominal"])} |' for r in rr)+f'\n| Total | {money(sum(nums))} ani-participant | | {money(sum(r["cash"] for r in rr))} | {money(sum(r["nominal"] for r in rr))} |'
 allrows.append({'name':name,'rows':rr})
parts['RESOURCE_TABLE']='| An reper | Locuri | Echipe la 16 copii | Adulți locali la 2,4 pe echipă | Mentori la 10 echipe |\n'+'\n'.join(f'| {r["year"]} | {money(r["n"])} | {r["teams"]} | {math.ceil(r["adults"])} | {r["mentors"]} |' for r in allrows[1]['rows'] if r['year'] in [2030,2033,2036,2040])
parts['SENS_TABLE']='| Caz la 10.000 de locuri stabile | Bani EUR 2026 cu rezervă | Cost pe copil activ |\n'
for label,v,active in [('Cost redus',340,.75),('Referință',420,.75),('Cost ridicat',520,.75),('Participare activă 60%',420,.60),('Participare activă 85%',420,.85)]:
 cash=1.1*(10000*v+5*60000+300000)
 parts['SENS_TABLE']+=f'| {label} | {money(cash)} | {money(cash/(10000*active))} |\n'
parts['PILOT_SENS']='| Configurație | Plafon EUR | Cost pe înscris | Cost pe activ la 75% |\n'+'\n'.join(f'| {name} | {money(t)} | {money(t/n)} | {money(t/(n*.75))} |' for name,t,n in [('400 copii de referință',total,400),('320 copii, costuri neschimbate',total,320),('Costuri de bază +10%',total*1.1,400)])
parts['SOURCE_MIX']='| Sursă țintită | Pondere ipotetică | EUR pentru pilot | Statut |\n'+'\n'.join(f'| {s} | {round(p*100)}% | {money(total*p)} | Necontractat |' for s,p in [('Finanțare publică eligibilă',.4),('Sponsorizări și fundații private',.35),('Parteneriate sportive instituționale',.15),('Donații și resurse proprii',.1)])
(P/'tables.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
(P/'model.json').write_text(json.dumps({'pilot':{'subtotal':subtotal,'reserve':reserve,'total':total,'rows':rows},'scenarios':allrows},ensure_ascii=False,indent=2))
