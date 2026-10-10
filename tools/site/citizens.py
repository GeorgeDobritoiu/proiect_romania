from pathlib import Path
from bs4 import BeautifulSoup
import html,json,re
P=Path(__file__).resolve().parents[2]
route='/initiative-cetatenesti'
source='https://activ.oradea.ro/proiecte'
items=[
 {'slug':'oradea-refoloseste','title':'Oradea ReFolosește: obiectele utile merită o a doua viață','desc':'O propunere cetățenească pentru donații, reutilizare și reducerea deșeurilor în Oradea.','text':'Propunerea urmărește crearea unei platforme locale pentru donații și reutilizarea obiectelor. Descrierea depusă pe Activ Oradea leagă inițiativa de comunitatea „Cereri și Donații Bihor”. Pentru bunurile care nu mai pot fi reutilizate, sunt propuse informații despre colectarea și reciclarea autorizată.','category':'REUTILIZARE','source':source+'?page=2'},
 {'slug':'statii-verzi-oradea','title':'Stații verzi în Oradea: o propunere pentru transportul public','desc':'Cetățenii propun modernizarea ecologică a unor stații de transport public de pe strada Universității.','text':'Inițiativa „Stații Verzi” propune modernizarea ecologică a unor stații de autobuz și tramvai de pe strada Universității. Este un exemplu de propunere care pornește de la un spațiu folosit zilnic de comunitate: locul în care oamenii așteaptă transportul public.','category':'SPAȚIU PUBLIC','source':source+'?fltr_proiecte=3'},
 {'slug':'biciclete-securizate-oradea','title':'Biciclete în siguranță: un pilot propus în cartierul Nufărul','desc':'Un stand securizat pentru biciclete, propus de cetățeni în bugetarea participativă Oradea 2026.','text':'În lista propunerilor eligibile apare un stand securizat pentru biciclete, conceput ca proiect pilot de mobilitate urbană în cartierul Nufărul. Inițiativa aduce în discuție parcarea bicicletelor aproape de locuințe, ca parte a infrastructurii necesare deplasării pe două roți.','category':'MOBILITATE','source':source}
]
base=BeautifulSoup((P/'index.html').read_text(),'html.parser')
header=base.select_one('.site-header');header.select_one('.languages').decompose()
footer=str(base.select_one('.site-footer'))+str(base.select_one('#toast'))
def doc(path,title,desc,body):
 u='https://proiectromania.ro'+path
 return '<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><script>document.documentElement.classList.add("js")</script><title>'+html.escape(title)+' | Proiect România</title><meta name="description" content="'+html.escape(desc,quote=True)+'"><link rel="canonical" href="'+u+'"><meta property="og:title" content="'+html.escape(title,quote=True)+'"><meta property="og:description" content="'+html.escape(desc,quote=True)+'"><meta property="og:url" content="'+u+'"><meta property="og:type" content="website"><link rel="icon" href="/assets/icon.svg"><link rel="stylesheet" href="/assets/site.css?rev=audit-20261003"><link rel="stylesheet" href="/assets/funding.css"></head><body class="platform-page"><a class="skip" href="#main">Mergi la conținut</a>'+str(header)+'<main id="main">'+body+'</main>'+footer+'<script src="/assets/site.js?rev=audit-20261003" defer></script></body></html>'
cards=''
paths=[route]
for x in items:
 path=route+'/'+x['slug'];paths.append(path)
 body='<article class="funding-article wrap"><a href="'+route+'">← Inițiative cetățenești</a><p class="eyebrow">'+x['category']+' · ORADEA</p><h1>'+x['title']+'</h1><p class="meta">Publicat și verificat la <time datetime="2026-10-10">10 octombrie 2026</time> · Prezentare editorială Proiect România</p><aside class="funding-deadline"><strong>Stadiu: propunere în bugetarea participativă Oradea 2026.</strong> Selectarea pentru finanțare și implementarea nu sunt confirmate.</aside><div class="funding-body"><h2>Ce propun cetățenii</h2><p>'+x['text']+'</p><h2>Cine a propus ideea</h2><p>Propunerea aparține inițiatorilor care au depus-o în programul local. Numele autorului individual nu a fost confirmat din sursele consultate; dosarul original rămâne sursa pentru atribuirea completă. Proiect România prezintă inițiativa și nu revendică autoratul sau un parteneriat cu inițiatorii.</p><h2>Consultă propunerea originală</h2><p><a href="'+x['source']+'">Lista oficială Activ Oradea — caută titlul propunerii</a></p><p><a href="https://oradea.ro/stiri/au-ramas-10-zile-de-vot-topul-proiectelor-preferate-de-oradeni-in-cursa-pentru-15-milioane-de-lei/">Context: programul de bugetare participativă, Primăria Oradea</a></p><h2>Ai o soluție pentru comunitatea ta?</h2><p>Prezintă problema, ideea și primul pas concret. Poți porni de la o descriere scurtă, pe care să o dezvolți într-o propunere cu resurse și un pilot.</p><a class="btn" href="/propune-un-proiect">Propune un proiect ↗</a></div><div class="funding-share"><button class="btn share" data-title="'+html.escape(x['title'],quote=True)+'" data-text="'+html.escape(x['desc'],quote=True)+'">Distribuie inițiativa ↗</button></div></article>'
 p=P/(path.strip('/')+'.html');p.parent.mkdir(exist_ok=True);p.write_text(doc(path,x['title'],x['desc'],body))
 cards+='<article class="project-card"><div class="project-card-body"><p class="eyebrow">'+x['category']+' · ORADEA · PROPUNERE</p><h2><a href="'+path+'">'+x['title']+'</a></h2><p>'+x['desc']+'</p><a class="btn" href="'+path+'">Descoperă inițiativa ↗</a></div></article>'
(P/(route.strip('/')+'.html')).write_text(doc(route,'Inițiative cetățenești','Soluții propuse direct de cetățeni pentru comunitățile lor.','<section class="page-intro wrap"><p class="eyebrow">IDEI CARE PORNESC DE LA OAMENI</p><h1>Inițiative cetățenești</h1><p>Soluții pentru cartiere și comunități, propuse direct de cetățeni. Descoperă exemple documentate și prezintă propria idee.</p><a class="btn" href="/propune-un-proiect">Propune un proiect ↗</a></section><section class="wrap funding-list">'+cards+'</section>'))
for p in P.rglob('*.html'):
 if 'tools' in p.relative_to(P).parts:continue
 s=p.read_text()
 if 'id="site-nav"' in s and 'href="'+route+'"' not in s:
  en='<html lang="en"' in s
  s=re.sub(r'(<nav[^>]*id="site-nav"[^>]*>)',lambda m:m[1]+'<a href="'+route+'"'+(' lang="ro"' if en else '')+'>'+('Citizen initiatives (RO)' if en else 'Inițiative cetățenești')+'</a>',s,count=1)
 if p==P/'index.html':
  soup=BeautifulSoup(s,'html.parser');hero=soup.select_one('.home-hero')
  hero.select_one('h1').string='Ai o soluție pentru comunitatea ta? Pune-o în mișcare.'
  intro=hero.select_one('p:not(.eyebrow)')
  if intro:intro.string='Propune un proiect pentru cartierul, localitatea sau România în care vrei să trăiești. Prezintă problema, soluția și primul pas concret.'
  if not soup.select_one('#citizens-home'):
   section=BeautifulSoup('<section class="wrap section-space" id="citizens-home"><p class="eyebrow">PROPUNERI DIRECTE ALE CETĂȚENILOR</p><h2>Soluții care pornesc din comunitate</h2><p>Reutilizarea obiectelor, stații verzi și biciclete în siguranță: primele exemple documentate.</p><a class="btn" href="'+route+'">Descoperă inițiativele cetățenești ↗</a></section>','html.parser')
   hero.insert_after(section)
  s=str(soup)
 p.write_text(s)
v=json.loads((P/'vercel.json').read_text());sm=(P/'sitemap.xml').read_text()
for path in paths:
 if not any(x['source']==path for x in v['rewrites']):v['rewrites'].append({'source':path,'destination':path+'.html'})
 if not any(x['source']==path+'.html' for x in v['redirects']):v['redirects'].append({'source':path+'.html','destination':path,'statusCode':301})
 if 'https://proiectromania.ro'+path+'</loc>' not in sm:sm=sm.replace('</urlset>','<url><loc>https://proiectromania.ro'+path+'</loc><lastmod>2026-10-10</lastmod></url></urlset>')
(P/'vercel.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');(P/'sitemap.xml').write_text(sm)
print('Built citizen initiatives: 3 articles and listing')

# Keep shared navigation and discovery pages compact after content updates.
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('navigation.py')))
