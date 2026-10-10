"""Compact home, complete project directory, and consistent site-wide navigation.
Run last after content generators. Does not modify project article bodies.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import html,json
P=Path(__file__).resolve().parents[2]
CATS={'sport':('Sport','Sport'),'solidaritate':('Solidaritate','Solidarity'),'educatie':('Educație','Education'),'democratie':('Democrație','Democracy'),'mediu':('Mediu și comunitate','Environment & community')}
# path, English path, category, RO title, EN title, RO summary, EN summary, attribution, image
ITEMS=[
('/proiecte/fotbal-pentru-viitor','/en/projects/football-for-the-future','sport','Fotbal pentru Viitor','Football for the Future','Copii, antrenori și comunități. Propunere pentru fotbalul de bază.','Children, coaches and communities. A grassroots football proposal.','George Dobritoiu','/assets/img/fotbal-pentru-viitor-logo.png'),
('/proiecte/hopefriday',None,'solidaritate','HopeFriday','HopeFriday','Sponsorizări transparente pentru asociații și fundații.','Transparent sponsorship for charities and associations.','George Dobritoiu','/assets/img/hopefriday-logo.jpg'),
('/proiecte/gcse-limba-romana','/en/projects/romanian-gcse','educatie','Limba română ca opțional GCSE','Romanian as an optional GCSE','Campanie pentru introducerea unui examen de limba română.','A campaign to introduce a Romanian-language examination.','Tessa Dunlop · Beyond Romania CIC','/assets/img/romanian-gcse-logo.png'),
('/proiecte/partidul-ca-organizatie-responsabila','/en/projects/accountable-political-party','democratie','Partidul ca organizație responsabilă','The accountable political party','Manual: înființare, filiale, cotizații și organizare democratică.','A manual covering registration, branches, dues and democratic governance.','George Dobritoiu',None),
('/initiative-cetatenesti/oradea-refoloseste',None,'mediu','Oradea ReFolosește','Oradea ReFolosește','O a doua viață pentru obiectele utile.','A second life for useful objects.','Inițiativă cetățenească documentată',None),
('/initiative-cetatenesti/statii-verzi-oradea',None,'mediu','Stații verzi în Oradea','Green bus stops in Oradea','Propunere pentru stații de transport public mai verzi.','A proposal for greener public transport stops.','Inițiativă cetățenească documentată',None),
('/initiative-cetatenesti/biciclete-securizate-oradea',None,'mediu','Biciclete în siguranță','Secure bicycle parking','Un pilot propus în cartierul Nufărul, Oradea.','A proposed pilot in the Nufărul neighbourhood, Oradea.','Inițiativă cetățenească documentată',None),
('/initiative-cetatenesti/gradini-asumate',None,'mediu','Grădini asumate','Community garden stewardship','Vecinii îngrijesc natura din cartier.','Neighbours care for local green spaces.','Inițiativă cetățenească documentată',None),
('/initiative-cetatenesti/spatiuviu-mihalache126',None,'mediu','SpațiuViu@Mihalache126','SpațiuViu@Mihalache126','O grădină construită împreună cu locatarii.','A garden developed together with residents.','Inițiativă cetățenească documentată',None),
('https://www.banipartide.ro/',None,'democratie','Banii Partidelor','Banii Partidelor','Explorează finanțarea partidelor și a campaniilor.','Explore political party and campaign financing.','Expert Forum',None),
('https://votcorect.ro/',None,'democratie','Vot Corect','Vot Corect','Informare electorală și observarea alegerilor.','Election information and observation.','Expert Forum · Coaliția Vot Corect',None),
('https://comunitate.funky.ong/bugete_2026',None,'democratie','Cu ochii pe bugetele locale','Keeping an eye on local budgets','Program educațional documentat, ediția aprilie–mai 2026.','Documented educational programme, April–May 2026 edition.','Funky Citizens · transparenta.eu',None),
]
SYMBOLS=['votat','refoloseste','statii-verzi','biciclete','gradini','spatiuviu','banii-partidelor','vot-corect','bugete-locale']
ITEMS=[x if j<3 else (*x[:-1],'/assets/img/project-symbols/'+SYMBOLS[j-3]+'.svg') for j,x in enumerate(ITEMS)]
ITEMS.append(('/proiecte/cum-infiintezi-o-asociatie','/en/projects/start-an-association','solidaritate','Cum înființezi o asociație','Start an association in Romania','Ghid: sport, protecția animalelor, acte, buget și organizare.','Sports, animal welfare, registration, budgets and organisation. Full guide in Romanian.','George Dobritoiu','/assets/img/project-symbols/asociatie.svg'))
def esc(s):return html.escape(s,quote=True)
def card(i,en=False,compact=False):
 path,ep,cat,ro,eng,rd,ed,author,img=i;title=eng if en else ro;url=ep if en and ep else path
 note=(' · RO' if en and not ep else '')+(' · External' if en and path.startswith('https') else ' · Extern' if path.startswith('https') else '')
 author=('Documented citizen initiative' if en and author=='Inițiativă cetățenească documentată' else author)
 visual=f'<img src="{img}" alt="{esc(ro)}" loading="lazy" decoding="async"/>' if img else f'<span class="project-monogram" aria-hidden="true">{esc(CATS[cat][1 if en else 0][:1])}</span>'
 return f'<article class="directory-card" data-category="{cat}"><div class="directory-mark">{visual}</div><p class="directory-category">{CATS[cat][1 if en else 0]}{note}</p><h{3 if compact else 2}><a href="{url}">{esc(title)}</a></h{3 if compact else 2}><p class="directory-description">{esc(ed if en else rd)}</p><p class="directory-author">{esc(author)}</p></article>'
def links(en):
 return [('/en/projects' if en else '/proiecte','Projects' if en else 'Proiecte'),('/oportunitati-de-finantare','Funding (RO)' if en else 'Finanțare'),('/en/about' if en else '/despre','About' if en else 'Despre'),('/en/propose-a-project' if en else '/propune-un-proiect','Propose a project' if en else 'Propune un proiect'),('/en/contact' if en else '/contact','Contact')]
for en in [False,True]:
 lang='en' if en else 'ro';home='en.html' if en else 'index.html';directory='en/projects.html' if en else 'proiecte.html';route='/en/projects' if en else '/proiecte'
 s=BeautifulSoup((P/home).read_text(),'html.parser');main=s.select_one('main');main.clear()
 cats=''.join(f'<a href="{route}#{k}">{v[1 if en else 0]}</a>' for k,v in CATS.items())
 title='Good ideas. Find your next project.' if en else 'Idei bune. Proiecte de descoperit.'
 intro='Explore proposals and independent initiatives. Find a cause, read the details and choose how to contribute.' if en else 'Descoperă propuneri și inițiative independente. Alege un domeniu, citește proiectul și vezi cum te poți implica.'
 featured=''.join(card(x,en,True) for x in ITEMS[:4])
 body=f'''<section class="wrap compact-hero"><p class="eyebrow">PROIECT ROMÂNIA</p><h1>{title}</h1><p>{intro}</p><nav class="category-shortcuts" aria-label="{'Project categories' if en else 'Categorii de proiecte'}">{cats}</nav></section>
<section class="wrap home-directory"><div class="directory-heading"><h2>{'Discover the projects' if en else 'Descoperă proiectele'}</h2><a href="{route}">{('View all '+str(len(ITEMS))) if en else ('Vezi toate cele '+str(len(ITEMS)))} →</a></div><div class="directory-grid home-grid">{featured}</div></section>
<section class="wrap compact-callout"><div><h2>{'Have an idea or want to help?' if en else 'Ai o idee sau vrei să ajuți?'}</h2><p>{'Share your proposal or contribute your experience.' if en else 'Propune o soluție sau contribuie cu experiența ta.'}</p></div><a class="btn" href="{'/en/propose-a-project' if en else '/propune-un-proiect'}">{'Get involved' if en else 'Implică-te'} ↗</a></section>'''
 main.append(BeautifulSoup(body,'html.parser'));(P/home).write_text(str(s))
 s=BeautifulSoup((P/directory).read_text(),'html.parser');main=s.select_one('main');main.clear()
 filters='<button type="button" data-filter="all" aria-pressed="true">'+('All' if en else 'Toate')+'</button>'+''.join(f'<button type="button" data-filter="{k}" aria-pressed="false">{v[1 if en else 0]}</button>' for k,v in CATS.items())
 body=f'''<section class="wrap directory-intro"><p class="eyebrow">{'PROJECT DIRECTORY' if en else 'BIBLIOTECA DE PROIECTE'}</p><h1>{'All projects, in one place.' if en else 'Toate proiectele, într-un singur loc.'}</h1><p>{'Original proposals and independent initiatives, with attribution and links to their organisers. Romanian-only pages are marked RO.' if en else 'Propuneri proprii și inițiative independente, cu autorii și organizatorii indicați. Selectează un domeniu sau caută un proiect.'}</p><div class="directory-controls" hidden><label for="project-search">{'Search projects' if en else 'Caută un proiect'}</label><input type="search" id="project-search" placeholder="{'Name, topic or organiser' if en else 'Nume, subiect sau organizator'}"/><div class="directory-filters" aria-label="{'Filter by category' if en else 'Filtrează după categorie'}">{filters}</div><p id="project-count" role="status" aria-live="polite"></p></div></section><section class="wrap directory-results" aria-label="{'Projects' if en else 'Proiecte'}"><div class="directory-grid">{''.join(card(x,en) for x in ITEMS)}</div><p id="project-empty" hidden>{'No matches. Try another search or category.' if en else 'Nu am găsit rezultate. Încearcă alt cuvânt sau altă categorie.'}</p><p class="directory-footnote">{'Browse the original collections:' if en else 'Vezi și colecțiile originale:'} <a href="/initiative-cetatenesti">{'Citizen initiatives (RO)' if en else 'Inițiative cetățenești'}</a> · <a href="{'/en/democracy-and-governance' if en else '/democratie-si-buna-guvernare'}">{'Democracy and governance' if en else 'Democrație și bună guvernare'}</a></p></section>'''
 main.append(BeautifulSoup(body,'html.parser'))
 if not s.select_one('script[src="/assets/directory.js"]'):s.body.append(s.new_tag('script',src='/assets/directory.js',defer=''))
 (P/directory).write_text(str(s))
# Add original editorial symbols to detailed articles and collection cards.
for entry in ITEMS[3:]:
 path,ep,cat,ro,eng,rd,ed,author,img=entry
 for route in [path,ep]:
  if not route or route.startswith('https:'):continue
  file=P/(route.lstrip('/')+'.html')
  if not file.exists():continue
  doc=BeautifulSoup(file.read_text(),'html.parser');h=doc.select_one('main h1')
  if h and not doc.select_one('main .project-editorial-symbol'):
   icon=doc.new_tag('img',src=img,alt=('Editorial symbol: '+eng if route.startswith('/en/') else 'Simbol ilustrativ: '+ro),width='160',height='160',decoding='async')
   icon['class']='project-editorial-symbol';icon['style']='display:block;width:104px;height:104px;margin:20px 0'
   h.insert_before(icon);file.write_text(str(doc))
for collection in ['initiative-cetatenesti.html','democratie-si-buna-guvernare.html','en/democracy-and-governance.html']:
 file=P/collection
 doc=BeautifulSoup(file.read_text(),'html.parser')
 for entry in ITEMS[3:]:
  path,ep,cat,ro,eng,rd,ed,author,img=entry
  for a in doc.select('main a[href]'):
   if a['href'] not in [path,ep]:continue
   cardnode=a.find_parent('article')
   if cardnode and not cardnode.select_one('.project-editorial-symbol'):
    holder=cardnode.select_one('.project-card-body') or cardnode
    icon=doc.new_tag('img',src=img,alt='Simbol ilustrativ / editorial symbol: '+ro,width='160',height='160',decoding='async')
    icon['class']='project-editorial-symbol';icon['style']='display:block;width:80px;height:80px;margin:0 0 18px'
    holder.insert(0,icon)
 file.write_text(str(doc))

# Apply to every existing page using the current site shell, without changing article content.
changed=[]
for p in P.rglob('*.html'):
 if any(x in p.parts for x in ['.git','node_modules','docs']):continue
 original=p.read_text();s=BeautifulSoup(original,'html.parser');nav=s.select_one('.site-nav')
 if not nav:continue
 en=s.html.get('lang','ro').startswith('en');nav.clear()
 rel=p.relative_to(P).as_posix();current='/en' if rel=='en.html' else '/' if rel=='index.html' else '/'+rel.removesuffix('.html')
 for url,label in links(en):
  a=s.new_tag('a',href=url);a.string=label
  if current==url:a['aria-current']='page'
  nav.append(a)
 if not s.select_one('link[href="/assets/directory.css"]'):s.head.append(s.new_tag('link',rel='stylesheet',href='/assets/directory.css'))
 foot=s.select_one('.site-footer > div:nth-of-type(2)')
 if foot:
  href='/en/how-it-works' if en else '/cum-functioneaza'
  if not foot.select_one(f'a[href="{href}"]'):
   a=s.new_tag('a',href=href);a.string='How it works' if en else 'Cum funcționează';foot.append(a)
 result=str(s)
 if result!=original:p.write_text(result);changed.append(rel)
print('Navigation applied:',len(changed),'pages')
