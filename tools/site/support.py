"""Publish the editorial fundraising directory. No payment data is collected."""
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import date
import json,html
P=Path(__file__).resolve().parents[2]
route='/proiecte-de-sustinut'
esc=html.escape
rows=json.loads((P/'data/proiecte-de-sustinut.json').read_text())
cards=[]
for x in rows:
    status='Apel continuu · fără termen publicat' if x['status']=='ongoing' else 'Apel încheiat'
    cards.append(f'''<article class="support-card" id="{x['id']}"><p class="eyebrow">{esc(x['category'])}</p><h2>{esc(x['title'])}</h2><p class="support-beneficiary">{esc(x['beneficiary'])}</p><p>{esc(x['purpose'])}</p><p><strong>Cum poți ajuta:</strong> {esc(x['support'])}</p><p class="support-state">{status}</p><p class="meta">Țintă și sumă strânsă: nepublicate în această selecție. Consultă datele actuale la beneficiar.</p><a class="btn" href="{esc(x['donation_url'])}" rel="noopener noreferrer" target="_blank">Susține pe site-ul beneficiarului ↗</a><p class="meta">Verificat editorial: {x['checked_at']} · <a href="{esc(x['source_url'])}" rel="noopener noreferrer" target="_blank">Sursa proiectului</a></p></article>''')
body='''<section class="wrap page-intro"><p class="eyebrow">OAMENI ȘI PROIECTE CARE AU NEVOIE DE SPRIJIN</p><h1>Proiecte de susținut</h1><p>Descoperă inițiative care strâng fonduri pentru sănătate, educație, natură și comunități. Alege o cauză și susține-o direct la beneficiar.</p><nav class="funding-tabs" aria-label="Resurse de finanțare"><a href="/oportunitati-de-finantare">Caut granturi ↗</a><a href="#proiecte">Vreau să susțin un proiect ↓</a><a href="#crowdfunding">Crowdfunding — în pregătire ↓</a></nav><aside class="support-note">Selecție editorială din surse publice, verificată la 20 octombrie 2026. Publicarea nu reprezintă un parteneriat sau un audit financiar. Donațiile se fac pe site-urile beneficiarilor; Proiect România nu încasează bani.</aside></section><section class="wrap support-grid" id="proiecte" aria-label="Proiecte care solicită sprijin">'''+''.join(cards)+'''</section><section class="wrap support-section" id="propune"><p class="eyebrow">PENTRU ORGANIZAȚII ȘI INIȚIATORI</p><h2>Ai un proiect care caută finanțare?</h2><p>Trimite-ne numele organizației, scopul proiectului, localitatea, bugetul, suma necesară, termenul, linkul oficial de donație și un contact public. Menționează dacă ai nevoie și de materiale, servicii sau voluntari.</p><p>Propunerile sunt analizate înainte de publicare. Nu trimite date medicale sau alte date personale ale beneficiarilor.</p><a class="btn" href="/contact">Propune un proiect pentru această secțiune ↗</a></section><section class="wrap support-section" id="crowdfunding"><p class="eyebrow">ETAPĂ VIITOARE · ÎN PREGĂTIRE</p><h2>Crowdfunding pentru proiecte concrete</h2><p>Ne propunem o secțiune în care comunitatea poate finanța obiective clare: de exemplu, echiparea unei săli, un program educațional sau o intervenție de mediu. Campaniile și plățile integrate nu sunt încă disponibile.</p><ol><li><strong>Proiect explicat:</strong> beneficiar identificat, buget, țintă de finanțare, termen și rezultate urmărite.</li><li><strong>Susținere transparentă:</strong> sumă colectată confirmată de procesator, costuri afișate și reguli clare dacă ținta nu este atinsă.</li><li><strong>Rezultate urmărite:</strong> actualizări, documente privind folosirea fondurilor și raport final.</li></ol><p>Prima etapă este directorul de mai sus. Următoarea propunere este un pilot cu un număr mic de organizații și campanii evaluate individual.</p><a href="/contact">Propune o campanie pentru viitorul pilot ↗</a></section>'''
doc=BeautifulSoup((P/'oportunitati-de-finantare.html').read_text(),'html.parser')
main=doc.select_one('main');main.clear();main.append(BeautifulSoup(body,'html.parser'))
doc.title.string='Proiecte de susținut | Proiect România'
desc='Proiecte care caută donații și sponsorizări: beneficiari, scopuri și legături oficiale pentru susținere.'
for selector,value in [('meta[name="description"]',desc),('meta[property="og:title"]','Proiecte de susținut'),('meta[property="og:description"]',desc),('meta[property="og:url"]','https://proiectromania.ro'+route)]:
    doc.select_one(selector)['content']=value
doc.select_one('link[rel="canonical"]')['href']='https://proiectromania.ro'+route
for tag in doc.select('script[type="application/ld+json"], script[src="/assets/funding.js"]'):tag.decompose()
doc.head.append(doc.new_tag('link',rel='stylesheet',href='/assets/support.css'))
(P/'proiecte-de-sustinut.html').write_text(str(doc))
# Reusable grouping avoids adding another top-level navigation item.
for p in P.rglob('*.html'):
    if any(z in p.relative_to(P).parts for z in ['tools','docs','node_modules']):continue
    s=BeautifulSoup(p.read_text(),'html.parser');nav=s.select_one('.site-nav')
    if not nav:continue
    anchor=nav.select_one('a[href="/oportunitati-de-finantare"]')
    if not anchor:continue
    old=anchor.find_parent('details') or anchor
    en=s.html.get('lang','ro').startswith('en')
    label='Funding' if en else 'Finanțare'
    grant='Grant opportunities (RO)' if en else 'Oportunități de finanțare'
    support='Support projects (RO)' if en else 'Proiecte de susținut'
    future='Crowdfunding — planned (RO)' if en else 'Crowdfunding — în pregătire'
    menu=f'<details class="nav-projects"><summary>{label} <span aria-hidden="true">⌄</span></summary><div class="nav-project-panel"><a href="/oportunitati-de-finantare">{grant}</a><a href="/proiecte-de-sustinut">{support}</a><a href="/proiecte-de-sustinut#crowdfunding">{future}</a></div></details>'
    old.replace_with(BeautifulSoup(menu,'html.parser'));p.write_text(str(s))
config=P/'vercel.json';v=json.loads(config.read_text())
if not any(x['source']==route for x in v['rewrites']):v['rewrites'].append({'source':route,'destination':route+'.html'})
if not any(x['source']==route+'.html' for x in v['redirects']):v['redirects'].append({'source':route+'.html','destination':route,'statusCode':301})
config.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
p=P/'sitemap.xml';s=p.read_text()
if 'https://proiectromania.ro'+route+'</loc>' not in s:s=s.replace('</urlset>','<url><loc>https://proiectromania.ro'+route+'</loc><lastmod>2026-10-20</lastmod></url></urlset>')
p.write_text(s)
print('Published four independently sourced support projects and crowdfunding concept.')
