"""Publish the bilingual democracy section without rebuilding unrelated pages."""
from pathlib import Path
import copy
import html
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

P = Path(__file__).resolve().parents[2]
BASE = 'https://proiectromania.ro'
RO = ['/democratie-si-buna-guvernare', '/proiecte/partidul-ca-organizatie-responsabila']
EN = ['/en/democracy-and-governance', '/en/projects/accountable-political-party']
DATE = '2026-10-10'

CONTENT = {
 'ro': {
  'section': 'Democrație și bună guvernare',
  'title': 'Partidul ca organizație responsabilă',
  'intro': 'Proiecte politice și civice pentru organizații responsabile, finanțare transparentă și participare informată.',
  'description': 'Propunere de management profesionist, autonomie locală și democrație internă. Inițiator: George Dobritoiu.',
  'proposal': 'PROPUNERE PROPRIE · ÎN DEZBATERE',
  'external': 'Inițiative independente documentate',
  'disclosure': 'Aceste proiecte aparțin organizațiilor indicate. Prezentarea lor este editorială și nu reprezintă un parteneriat sau o afiliere. Activitățile și înscrierile se verifică pe site-urile organizatorilor.',
  'read': 'Citește propunerea',
  'explore': 'Descoperă secțiunea',
  'source': 'Sursa și site-ul proiectului',
  'checked': 'Surse consultate la 10 octombrie 2026.',
  'projects': [
   ('Banii Partidelor', 'Expert Forum', 'TRANSPARENȚĂ POLITICĂ', 'O platformă pentru explorarea veniturilor și cheltuielilor partidelor, a finanțării campaniilor electorale și a donatorilor. Pentru interpretare, consultă metodologia și perioada acoperită de fiecare set de date.', 'https://www.banipartide.ro/'),
   ('Vot Corect', 'Expert Forum · Coaliția Vot Corect', 'INFORMARE ȘI OBSERVARE ELECTORALĂ', 'Informații despre alegeri și sprijin pentru semnalarea neregulilor. Paginile sunt organizate pe scrutin; regulile și oportunitățile de observare trebuie verificate pentru ediția relevantă.', 'https://votcorect.ro/'),
   ('Cu ochii pe bugetele locale 2026', 'Funky Citizens și transparenta.eu', 'PARTICIPARE CIVICĂ · EDIȚIE APRILIE–MAI 2026', 'Program educațional anunțat pentru aprilie–mai 2026, despre citirea bugetelor locale, participarea la dezbateri și compararea planificării cu execuția. Este prezentat ca exemplu documentat; nu ca apel cu înscrieri deschise.', 'https://comunitate.funky.ong/bugete_2026'),
  ],
  'body': '''
<aside class="dem-note"><strong>Concept pentru dezbatere publică.</strong> Această pagină prezintă un model de organizare. Nu anunță înființarea unui partid, nu recrutează membri și nu constituie un statut juridic adoptat.</aside>
<h2>Ideea de la care pornim</h2>
<p>Un partid poate împrumuta disciplina unei organizații bine conduse: roluri clare, bugete urmărite, echipe competente și evaluarea rezultatelor. Scopul propunerii este ca aceste instrumente să servească interesul public și decizia democratică a membrilor.</p>
<p>George Dobritoiu a formulat conceptul în mai 2025 și l-a reluat în iunie 2026, sub ideea de „partid-franciză”: un centru național comun și filiale locale semi-autonome. „ACTIV” a fost un nume de lucru. Pagina de față este o sinteză editorială actualizată a ideii, nu reproducerea integrală a documentului inițial.</p>
<h2>Ce înseamnă „condus ca o companie”</h2>
<p>Fiecare echipă ar avea un mandat, resurse, un responsabil și termene. Performanța ar fi discutată pe baza unor rezultate verificabile. Autoritatea conducerii ar proveni din regulile democratice ale organizației, cu limite de mandat, control și posibilitatea contestării deciziilor.</p>
<div class="dem-table"><table><caption>Modelul de organizare propus</caption><thead><tr><th>Nivel</th><th>Responsabilități</th><th>Control</th></tr></thead><tbody>
<tr><td>Membrii și convenția</td><td>Aleg direcția, conducerea și regulile comune.</td><td>Vot verificabil, informare și proceduri de contestare.</td></tr>
<tr><td>Consiliul ales</td><td>Aprobă strategia și bugetele; supraveghează executivul.</td><td>Rapoarte periodice și răspundere în fața membrilor.</td></tr>
<tr><td>Echipa executivă</td><td>Organizează activitatea zilnică, resursele și proiectele.</td><td>Mandat limitat, obiective și evaluare documentată.</td></tr>
<tr><td>Filialele locale</td><td>Propun soluții locale și gestionează echipele în limitele regulilor comune.</td><td>Transparență financiară, evaluare locală și audit.</td></tr>
<tr><td>Control și integritate</td><td>Verifică finanțele, conflictele de interese și respectarea procedurilor.</td><td>Independență față de persoanele evaluate și drept la apărare.</td></tr>
</tbody></table></div>
<h2>Autonomie locală, standarde comune</h2>
<p>Centrul ar asigura valorile, identitatea, resursele de formare și instrumentele digitale. Filialele ar adapta prioritățile la comunitate și ar răspunde pentru activitatea lor. „Franciza” este o analogie organizațională: propunerea nu presupune cumpărarea unei filiale, vânzarea candidaturilor sau control politic acordat în schimbul unei contribuții financiare.</p>
<h2>Oameni selectați și evaluați transparent</h2>
<p>Pentru rolurile executive propunem criterii publice de competență, interviuri și evaluări periodice. Pentru funcțiile alese și candidaturi, selecția trebuie să păstreze participarea membrilor și reguli cunoscute dinainte. Verificările de integritate trebuie să fie proporționale, documentate și să permită corectarea erorilor.</p>
<h2>Bani și decizii care pot fi urmărite</h2>
<ul><li>Bugete aprobate, cheltuieli documentate și rapoarte periodice inteligibile.</li><li>Declararea intereselor relevante și abținerea de la decizii în caz de conflict.</li><li>Audit independent, cu publicarea concluziilor și a măsurilor de remediere.</li><li>O platformă digitală propusă pentru proiecte, consultări, vot intern și rapoarte, cu drepturi de acces și protejarea datelor personale.</li></ul>
<h2>Ce rezultate măsurăm</h2>
<p>Evaluarea ar include îndeplinirea angajamentelor organizaționale, publicarea la timp a rapoartelor, participarea membrilor, calitatea propunerilor și rezolvarea sesizărilor. Rezultatele electorale pot fi analizate, dar nu înlocuiesc integritatea sau calitatea muncii. Fiecare indicator ar avea o definiție, o sursă și o verificare; nu propunem scoruri automate pentru opiniile membrilor.</p>
<h2>Un pilot înainte de extindere</h2>
<p>Propunerea editorială pentru prima etapă este testarea procedurilor timp de șase luni în două sau trei echipe locale voluntare. Nu există în prezent un pilot confirmat, o echipă de implementare sau finanțare anunțată.</p>
<ol><li>Definirea regulilor, responsabilităților și procedurilor de contestație.</li><li>Stabilirea situației inițiale și a unui buget detaliat.</li><li>Testarea raportării, consultării și gestionării proiectelor.</li><li>Evaluare independentă și publicarea lecțiilor înainte de extindere.</li></ol>
<p>Resursele de estimat sunt coordonarea, consultanța juridică, contabilitatea, auditul, formarea și platforma digitală. Valoarea bugetului și sursele de finanțare rămân de stabilit; nu prezentăm sume sau angajamente neconfirmate.</p>
<h2>Riscuri și limite</h2>
<p>Riscurile principale sunt concentrarea puterii, autonomia locală folosită fără răspundere, indicatorii manipulați și transformarea diferențelor de opinie în motive de sancționare. Răspunsurile propuse sunt separarea atribuțiilor, verificarea independentă, publicarea motivelor deciziilor și contestații soluționate de persoane neimplicate.</p>
<p>Înainte de implementare, modelul trebuie dezbătut și verificat juridic pentru organizarea partidelor, finanțare, proceduri electorale și protecția datelor. Această pagină nu confirmă conformitatea juridică a unui statut.</p>
<h2>Contribuie la propunere</h2>
<p>Sunt utile observații despre democrația internă, administrație, organizare locală, audit și securitatea platformei. Autorul conceptului este George Dobritoiu. Colaboratorii și eventualele interese relevante vor fi declarați pe măsură ce se formează o echipă.</p>
<p><a class="btn" href="/contact">Trimite o observație sau propune o contribuție ↗</a></p>
'''
 },
 'en': {
  'section': 'Democracy and good governance',
  'title': 'The political party as an accountable organisation',
  'intro': 'Political and civic projects for accountable organisations, transparent funding and informed participation.',
  'description': 'A proposal for professional management, local autonomy and internal democracy. Initiator: George Dobritoiu.',
  'proposal': 'ORIGINAL PROPOSAL · OPEN FOR DISCUSSION',
  'external': 'Documented independent initiatives',
  'disclosure': 'These projects belong to the named organisations. Their inclusion is editorial and does not imply a partnership or affiliation. Check organisers’ websites for current activities and registration.',
  'read': 'Read the proposal',
  'explore': 'Explore this section',
  'source': 'Source and project website',
  'checked': 'Sources consulted on 10 October 2026.',
  'projects': [
   ('Banii Partidelor', 'Expert Forum', 'POLITICAL FINANCE TRANSPARENCY', 'Explore party income and expenditure, election campaign financing and donors. Consult the methodology and the period covered by each dataset before interpreting the figures.', 'https://www.banipartide.ro/'),
   ('Vot Corect', 'Expert Forum · Vot Corect Coalition', 'ELECTORAL INFORMATION AND OBSERVATION', 'Election information and support for reporting irregularities. Resources are organised by election; check the relevant edition for applicable guidance and observer opportunities.', 'https://votcorect.ro/'),
   ('Cu ochii pe bugetele locale 2026', 'Funky Citizens and transparenta.eu', 'CIVIC PARTICIPATION · APRIL–MAY 2026 EDITION', 'An educational programme announced for April–May 2026 about understanding local budgets, requesting public debate and comparing plans with actual spending. Presented as a documented example, not an open registration call.', 'https://comunitate.funky.ong/bugete_2026'),
  ],
  'body': '''
<aside class="dem-note"><strong>A concept for public discussion.</strong> This page presents an organisational model. It does not announce a new party, recruit members or constitute an adopted legal statute.</aside>
<h2>The starting point</h2><p>A political party could adopt the discipline of a well-run organisation: clear roles, accountable budgets, competent teams and assessment of results. These tools should serve the public interest and democratic decisions by members.</p>
<p>George Dobritoiu formulated the idea in May 2025 and revisited it in June 2026 as a “franchise party”: a shared national centre with semi-autonomous local branches. “ACTIV” was a working name. This page is an updated editorial synthesis, not a reproduction of the complete original document.</p>
<h2>Professional management under democratic control</h2><p>Teams would receive a mandate, resources, named responsibilities and deadlines. Members would elect the governing council and determine the organisation’s direction. The council would approve strategy and budgets, while an executive team would manage daily operations under a limited, reviewable mandate.</p>
<p>Independent oversight would review finances, conflicts of interest and compliance with agreed procedures. Decisions would have documented reasons, a right of reply and an appeal process handled by people not involved in the initial decision.</p>
<h2>Local autonomy and common standards</h2><p>The national centre would provide shared values, identity, training and digital tools. Local branches would develop community priorities and account for their work. “Franchise” is an organisational analogy: the proposal does not envisage buying branches, selling candidacies or granting political control in return for funding.</p>
<h2>Selection and evaluation</h2><p>Executive roles would have published competence criteria, interviews and periodic reviews. Elected positions and candidacies would retain member participation and rules announced in advance. Integrity checks would need to be proportionate, documented and open to correction.</p>
<h2>Traceable funding and decisions</h2><ul><li>Approved budgets, documented expenditure and understandable periodic reports.</li><li>Declarations of relevant interests and recusal where conflicts arise.</li><li>Independent audit with published findings and corrective actions.</li><li>A proposed digital platform for projects, consultations, internal voting and reporting, with access controls and personal-data protection.</li></ul>
<h2>What would be measured?</h2><p>Indicators would cover delivery of organisational commitments, timely reporting, member participation, quality of proposals and handling of complaints. Electoral results would not replace integrity or quality of work. Every indicator would have a definition, source and verification process; the proposal does not include automated scoring of members’ opinions.</p>
<h2>A pilot before expansion</h2><p>The editorial proposal is a six-month trial with two or three voluntary local teams. No pilot, implementation team or funding is currently confirmed. The stages would be agreement on rules and appeals, a baseline and detailed budget, testing of reporting and consultation, and independent evaluation before expansion.</p>
<p>Coordination, legal advice, accounting, audit, training and digital infrastructure require costing. Budget amounts and funding sources remain to be established.</p>
<h2>Risks and limits</h2><p>Concentrated power, unaccountable local autonomy, manipulated indicators and sanctions against legitimate disagreement are key risks. The proposed safeguards are separation of duties, independent review, reasoned decisions and impartial appeals.</p>
<p>Implementation would require debate and legal review covering party organisation, financing, electoral procedures and personal data. This presentation does not establish that a statute is legally compliant.</p>
<h2>Contribute</h2><p>Feedback on internal democracy, local organisation, audit and digital security is welcome. The concept’s author is George Dobritoiu. Collaborators and relevant interests would be disclosed as an implementation team develops.</p><p><a class="btn" href="/en/contact">Share feedback or offer a contribution ↗</a></p>
'''
 }
}


# The manual is maintained independently and shared by the HTML and PDF builders.
CONTENT['ro']['description'] = 'Manual practic pentru înființarea și organizarea unui partid în România: legislație, filiale, cotizații, KPI și tehnologie.'
CONTENT['ro']['proposal'] = 'MANUAL DE LUCRU · VERSIUNEA 1.0'
CONTENT['ro']['read'] = 'Citește manualul'
CONTENT['ro']['body'] = (P/'docs/manual-partid-responsabil.html').read_text()
CONTENT['en']['body'] = '<aside class="dem-note"><strong>Practical manual now available in Romanian.</strong> The expanded edition covers registration in Romania, branch governance, membership dues, financial controls, 14 administrative KPIs, technology and privacy, a documentary case study of the AUR app, and eight working templates. Legal requirements are distinguished from proposed rules. Sources reviewed on 10 October 2026. <a href="/proiecte/partidul-ca-organizatie-responsabila">Read the Romanian manual</a> · <a href="/downloads/manual-partid-responsabil.pdf">Download the Romanian PDF</a>.</aside>' + CONTENT['en']['body']

def card(lang):
 d=CONTENT[lang]; paths=EN if lang=='en' else RO
 return f'<article class="dem-card" id="accountable-party-card"><p class="eyebrow">{d["proposal"]}</p><h2><a href="{paths[1]}">{d["title"]}</a></h2><p>{d["description"]}</p><p class="meta">George Dobritoiu · 2025–2026</p><a class="btn" href="{paths[1]}">{d["read"]} ↗</a></article>'

def page(lang, index, body):
 d=CONTENT[lang]; paths=EN if lang=='en' else RO; path=paths[index]
 s=BeautifulSoup((P/('en.html' if lang=='en' else 'index.html')).read_text(),'html.parser')
 title=d['section'] if index==0 else d['title']; desc=d['intro'] if index==0 else d['description']
 s.title.string=title+' | Proiect România'
 for n in s.select('script[type="application/ld+json"],link[rel="alternate"]'): n.decompose()
 s.select_one('link[rel="canonical"]')['href']=BASE+path
 for attr,value in [('name="description"',desc),('property="og:title"',title),('property="og:description"',desc),('property="og:url"',BASE+path)]:
  s.select_one('meta['+attr+']')['content']=value
 for l,prefix in [('ro',RO),('en',EN),('x-default',RO)]:
  tag=s.new_tag('link',rel='alternate',hreflang=l,href=BASE+prefix[index]);s.head.append(tag)
 s.head.append(s.new_tag('link',rel='stylesheet',href='/assets/democracy.css'))
 for a in s.select('.languages a'):
  a['href']=(EN if a.get('lang')=='en' else RO)[index]
 main=s.select_one('main');main.clear();main.append(BeautifulSoup(body,'html.parser'))
 schema={'@context':'https://schema.org','@type':'WebPage','name':title,'description':desc,'url':BASE+path,'inLanguage':lang}
 tag=s.new_tag('script',type='application/ld+json');tag.string=json.dumps(schema,ensure_ascii=False);s.head.append(tag)
 q=P/(path.lstrip('/')+'.html');q.parent.mkdir(parents=True,exist_ok=True);q.write_text(str(s))

for lang in ['ro','en']:
 d=CONTENT[lang];paths=EN if lang=='en' else RO
 external=''.join(f'<article class="dem-card"><p class="eyebrow">{html.escape(k)}</p><h3>{html.escape(t)}</h3><p class="meta">{html.escape(o)}</p><p>{html.escape(b)}</p><a class="text-link" href="{u}">{d["source"]} ↗</a></article>' for t,o,k,b,u in d['projects'])
 body=f'<section class="page-intro wrap"><p class="eyebrow">PROIECT ROMÂNIA</p><h1>{d["section"]}</h1><p class="lead">{d["intro"]}</p></section><section class="wrap dem-section">{card(lang)}<h2>{d["external"]}</h2><p class="dem-note">{d["disclosure"]}</p><div class="dem-grid">{external}</div><p class="meta">{d["checked"]}</p></section>'
 page(lang,0,body)
 back='Înapoi la secțiune' if lang=='ro' else 'Back to section'
 body=f'<article class="wrap dem-article"><a class="text-link" href="{paths[0]}">← {back}</a><p class="eyebrow">{d["proposal"]}</p><h1>{d["title"]}</h1><p class="lead">{d["description"]}</p><p class="meta">George Dobritoiu · 10.10.2026</p><div class="dem-body">{d["body"]}</div></article>'
 page(lang,1,body)
 # Add discoverable entry points without changing unrelated content or navigation.
 for filename in (['index.html','proiecte.html'] if lang=='ro' else ['en.html','en/projects.html']):
  s=BeautifulSoup((P/filename).read_text(),'html.parser')
  old=s.select_one('#democracy-entry')
  if old: old.decompose()
  is_projects='projects' in filename or filename=='proiecte.html'
  body=f'<section class="wrap section-space" id="democracy-entry"><p class="eyebrow">{d["section"].upper()}</p>'
  body+=(card(lang) if is_projects else f'<h2>{d["section"]}</h2><p>{d["intro"]}</p>')
  body+=f'<p><a class="btn" href="{paths[0]}">{d["explore"]} ↗</a></p></section>'
  s.select_one('main').append(BeautifulSoup(body,'html.parser'))
  if not s.select_one('link[href="/assets/democracy.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='/assets/democracy.css'))
  if is_projects:
   for n in s.select('main section.section-space > .meta'):
    if 'proiect' in n.get_text() or 'project' in n.get_text():
     n.string='Sport, solidaritate și democrație · Propuneri și inițiative documentate' if lang=='ro' else 'Sport and democracy · Proposals and documented initiatives'
  (P/filename).write_text(str(s))

v=json.loads((P/'vercel.json').read_text())
for path in RO+EN:
 if not any(x['source']==path for x in v['rewrites']):v['rewrites'].append({'source':path,'destination':path+'.html'})
 if not any(x['source']==path+'.html' for x in v['redirects']):v['redirects'].append({'source':path+'.html','destination':path,'statusCode':301})
(P/'vercel.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ns='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('',ns);tree=ET.parse(P/'sitemap.xml');root=tree.getroot()
known={n.text for n in root.findall('{'+ns+'}url/{'+ns+'}loc')}
for path in RO+EN:
 if BASE+path not in known:
  u=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(u,'{'+ns+'}loc').text=BASE+path
tree.write(P/'sitemap.xml',encoding='utf-8',xml_declaration=True)


# Keep shared navigation and discovery pages compact after content updates.
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('navigation.py')))
