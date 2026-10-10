from pathlib import Path
from bs4 import BeautifulSoup
import json,html
P=Path(__file__).resolve().parents[2]
source='https://platformademediu.ro/media/ai-o-idee-pentru-cartierul-tau-perfect-hai-s-o-facem-realitate'
items=[dict(slug='gradini-asumate',title='Grădini asumate: vecinii îngrijesc natura din cartier',author='Grupul de inițiativă Plantaredetot',budget='64.000 lei',desc='Plantări, compostare și educație de mediu, într-o inițiativă a vecinilor de pe Strada Turda 125, București.',body='Grupul Plantaredetot propune îngrijirea spațiului verde din spatele blocului de pe Strada Turda 125. Proiectul combină plantările cu adăposturi pentru insecte, compostare și ateliere educative. Vecinii de vârste diferite sunt invitați să participe la activități și la îngrijirea spațiului.'),dict(slug='spatiuviu-mihalache126',title='SpațiuViu@Mihalache126: o grădină construită împreună cu locatarii',author='Grupul de Inițiativă Dioda',budget='42.000 lei',desc='O grădină comunitară cu plante native, apă de ploaie pentru irigare și colectarea uleiului uzat, în București.',body='Inițiativa urmărește transformarea curții blocului de pe Mihalache 126 într-o grădină comunitară. Planul include peste 200 de plante native, irigare cu apă de ploaie, colectarea uleiului uzat și un spațiu educativ pentru grădinărit și reciclare. Gestionarea împreună cu locatarii este parte din modelul propus.')]
paths=[]
for x in items:
 route='/initiative-cetatenesti/'+x['slug'];paths.append(route)
 s=BeautifulSoup((P/'initiative-cetatenesti/oradea-refoloseste.html').read_text(),'html.parser')
 s.title.string=x['title']+' | Proiect România'
 for m in s.select('meta[name=description],meta[property="og:description"]'):m['content']=x['desc']
 s.select_one('meta[property="og:title"]')['content']=x['title']
 s.select_one('meta[property="og:url"]')['content']='https://proiectromania.ro'+route
 s.select_one('link[rel=canonical]')['href']='https://proiectromania.ro'+route
 body='<article class="funding-article wrap"><a href="/initiative-cetatenesti">← Inițiative cetățenești</a><p class="eyebrow">MEDIU · BUCUREȘTI · INIȚIATIVĂ CIVICĂ</p><h1>'+x['title']+'</h1><p class="lead">'+x['desc']+'</p><p class="meta">Publicat și verificat la 10 octombrie 2026 · Prezentare editorială Proiect România</p><aside class="funding-deadline"><strong>Finanțare documentată: '+x['budget']+'.</strong> Finalizarea integrală a proiectului și stadiul actual al lucrărilor nu au fost confirmate separat.</aside><div class="funding-body"><h2>Ideea și oamenii din spatele ei</h2><p>Inițiator: <strong>'+x['author']+'</strong>.</p><p>'+x['body']+'</p><h2>Ce este confirmat</h2><p>Platforma de mediu pentru București include proiectul între inițiativele finanțate în a doua ediție a programului „În ZONA TA”, dezvoltat de Fundația Comunitară București și ING Bank România. Sursa descrie obiectivele și finanțarea acordată; aceasta nu este o invitație deschisă la finanțare.</p><h2>Ce poate inspira în alte comunități</h2><p>Vecinii pot porni de la un spațiu concret și de la un grup care își asumă îngrijirea lui. Pentru un proiect similar, primul pas este clarificarea dreptului de utilizare a terenului, acordurile necesare, bugetul și responsabilitatea întreținerii. Acestea sunt recomandări editoriale Proiect România, nu cerințe atribuite inițiatorilor.</p><h2>Consultă sursa originală</h2><p><a href="'+source+'">Platforma de mediu pentru București — proiecte finanțate „În ZONA TA”</a></p><p>Proiect România prezintă inițiativa independent. Autoratul aparține grupului menționat; publicarea nu presupune un parteneriat sau o susținere din partea acestuia.</p><h2>Ai o idee de mediu pentru cartierul tău?</h2><p>Prezintă problema, soluția și primul pas concret, apoi dezvoltă un pilot cu buget, responsabilități și rezultate măsurabile.</p><a class="btn" href="/propune-un-proiect">Propune un proiect ↗</a></div><div class="funding-share"><button class="btn share" data-title="'+html.escape(x['title'],quote=True)+'" data-text="'+html.escape(x['desc'],quote=True)+'">Distribuie inițiativa ↗</button></div></article>'
 s.main.clear();s.main.append(BeautifulSoup(body,'html.parser'));(P/(route[1:]+'.html')).write_text(str(s))
listing=BeautifulSoup((P/'initiative-cetatenesti.html').read_text(),'html.parser')
for x in items:
 ident='environment-'+x['slug']
 if listing.select_one('#'+ident):listing.select_one('#'+ident).decompose()
 listing.select_one('.funding-list').append(BeautifulSoup('<article class="project-card" id="'+ident+'"><div class="project-card-body"><p class="eyebrow">MEDIU · BUCUREȘTI · FINANȚARE DOCUMENTATĂ</p><h2><a href="/initiative-cetatenesti/'+x['slug']+'">'+x['title']+'</a></h2><p>'+x['desc']+'</p><p class="meta">'+x['author']+'</p><a class="btn" href="/initiative-cetatenesti/'+x['slug']+'">Descoperă inițiativa ↗</a></div></article>','html.parser'))
(P/'initiative-cetatenesti.html').write_text(str(listing))
s=BeautifulSoup((P/'index.html').read_text(),'html.parser');section=s.select_one('#citizens-home')
if section:section.select_one('p:not(.eyebrow)').string='Grădini comunitare, reutilizarea obiectelor, stații verzi și biciclete în siguranță: exemple documentate care pornesc de la cetățeni.'
(P/'index.html').write_text(str(s))
v=json.loads((P/'vercel.json').read_text());sm=(P/'sitemap.xml').read_text()
for route in paths:
 if not any(x['source']==route for x in v['rewrites']):v['rewrites'].append(dict(source=route,destination=route+'.html'))
 if not any(x['source']==route+'.html' for x in v['redirects']):v['redirects'].append(dict(source=route+'.html',destination=route,statusCode=301))
 if route+'</loc>' not in sm:sm=sm.replace('</urlset>','<url><loc>https://proiectromania.ro'+route+'</loc><lastmod>2026-10-10</lastmod></url></urlset>')
(P/'vercel.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');(P/'sitemap.xml').write_text(sm)
print('Built two citizen environment features and updated listing')
