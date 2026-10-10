"""Promote the independent Romanian GCSE campaign with original attribution."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET
P=Path(__file__).resolve().parents[2]
BASE='https://proiectromania.ro'
RO='/proiecte/gcse-limba-romana';EN='/en/projects/romanian-gcse'
FORM='https://form.jotform.com/260113622781046'
OFFICIAL='https://romaniangcse.co.uk/ro/'
DATA={
'ro':dict(title='Limba română ca opțional GCSE',tag='EDUCAȚIE · CAMPANIE INDEPENDENTĂ',description='Promovăm campania Tessa Dunlop și Beyond Romania CIC pentru introducerea limbii române ca materie opțională GCSE.',read='Descoperă campania',back='Înapoi la proiecte',body=f'''
<aside class="dem-note"><strong>O inițiativă a Tessa Dunlop și Beyond Romania CIC.</strong> Proiect România promovează acțiunea organizatorilor. Prezentarea nu reprezintă un proiect propriu sau un parteneriat anunțat.</aside>
<p><a class="btn" href="{FORM}">Completează formularul de interes ↗</a></p>
<h2>Ce urmărește campania</h2>
<p>Introducerea limbii române ca materie opțională GCSE, pentru recunoașterea competențelor lingvistice ale elevilor. Este vorba despre un examen la limba română, nu despre susținerea tuturor materiilor în română.</p>
<p><strong>Statut:</strong> campanie pentru introducerea examenului. Această pagină nu anunță aprobarea calificării, o sesiune de examinare sau o dată de începere.</p>
<h2>Cine se află în spatele inițiativei</h2>
<p>Apelul Ambasadei României în Regatul Unit indică Tessa Dunlop și Beyond Romania CIC. Site-ul campaniei confirmă că aceasta este administrată de Beyond Romania CIC și prezintă echipa, inclusiv implicarea Tessei Dunlop în relația cu sectorul educațional și organismele de certificare.</p>
<h2>Cum poți sprijini acțiunea</h2>
<ol><li><strong>Exprimă-ți interesul</strong> prin formularul organizatorilor, în rolul care ți se potrivește: părinte/elev, profesor, școală, ONG sau alt rol.</li><li><strong>Oferă sprijin sau timp ca voluntar.</strong> Formularul permite descrierea contribuției pe care o poți aduce.</li><li><strong>Distribuie informația originală.</strong> Pagina „Cum poți ajuta” a organizatorilor prezintă și petiția, precum și modalități de a implica școlile și comunitatea.</li></ol>
<p><strong>Important:</strong> completarea formularului înregistrează interesul pentru inițiativă; nu echivalează cu înscrierea la un examen GCSE disponibil. Datele sunt introduse pe formularul extern al organizatorilor. Consultă informațiile lor privind utilizarea datelor înainte de completare.</p>
<p><a class="btn" href="{FORM}">Mergi la formularul campaniei ↗</a></p>
<p><a href="{OFFICIAL}">Site-ul campaniei</a> · <a href="{OFFICIAL}how-you-can-help/">Cum poți ajuta</a> · <a href="{OFFICIAL}contact/">Contactează organizatorii</a></p>
<h2>Surse și atribuirea inițiativei</h2>
<ul><li><a href="https://www.facebook.com/share/p/14rqS1QWPG9/">Apelul Ambasadei pe Facebook</a> — text consultat din captura postării furnizată de cititor.</li><li><a href="{OFFICIAL}meet-the-team/">Echipa campaniei</a> și <a href="{OFFICIAL}contact/">administratorul inițiativei</a>.</li><li><a href="{FORM}">Formularul de interes</a> și <a href="{OFFICIAL}">platforma Romanian GCSE</a>.</li></ul>
<p class="meta">Surse online consultate la 10 octombrie 2026. Actualizările și condițiile participării se verifică direct la organizatori.</p>'''),
'en':dict(title='Romanian as an optional GCSE subject',tag='EDUCATION · INDEPENDENT CAMPAIGN',description='Discover the campaign by Tessa Dunlop and Beyond Romania CIC to introduce Romanian as an optional GCSE subject.',read='Explore the campaign',back='Back to projects',body=f'''
<aside class="dem-note"><strong>An initiative by Tessa Dunlop and Beyond Romania CIC.</strong> Proiect România is helping publicise the organisers’ work. This is an editorial listing, not our own programme or an announced partnership.</aside>
<p><a class="btn" href="{FORM}">Register your interest with the organisers ↗</a></p>
<h2>The aim</h2><p>The campaign seeks a Romanian-language GCSE subject recognising pupils’ language skills. It concerns an optional language examination, not taking every school subject in Romanian.</p>
<p><strong>Status:</strong> a campaign for the examination’s introduction. This page does not announce an approved qualification, an examination session or a start date.</p>
<h2>The organisers</h2><p>The Romanian Embassy’s appeal names Tessa Dunlop and Beyond Romania CIC. The campaign website identifies Beyond Romania CIC as its administrator and describes Tessa Dunlop’s work with educators and awarding organisations.</p>
<h2>How to help</h2><ol><li>Complete the organisers’ expression-of-interest form as a parent/pupil, teacher, school, community organisation or other contributor.</li><li>Describe any volunteering or practical support you can offer.</li><li>Share the original campaign information. The organisers’ participation page also links to their petition and ways to involve schools and the community.</li></ol>
<p><strong>The form records interest, not registration for an available GCSE examination.</strong> It is hosted externally by the organisers; read their information about data use before submitting personal details.</p>
<p><a href="{OFFICIAL}">Campaign website (Romanian)</a> · <a href="{OFFICIAL}how-you-can-help/">Ways to help</a> · <a href="{OFFICIAL}contact/">Contact the organisers</a></p>
<h2>Sources</h2><ul><li><a href="https://www.facebook.com/share/p/14rqS1QWPG9/">Romanian Embassy Facebook appeal</a>, read from a reader-supplied screenshot.</li><li><a href="{OFFICIAL}meet-the-team/">Campaign team</a> and <a href="{OFFICIAL}contact/">campaign administrator</a>.</li><li><a href="{FORM}">Expression-of-interest form</a>.</li></ul><p class="meta">Online sources checked on 10 October 2026. Check participation details and updates with the organisers.</p>''')}

def card(lang):
 d=DATA[lang];path=RO if lang=='ro' else EN
 return f'<section class="wrap section-space" id="education-gcse-entry"><p class="eyebrow">{d["tag"]}</p><article class="dem-card"><h2><a href="{path}">{d["title"]}</a></h2><p>{d["description"]}</p><p class="meta">Tessa Dunlop · Beyond Romania CIC</p><a class="btn" href="{path}">{d["read"]} ↗</a></article></section>'

for lang in ['ro','en']:
 d=DATA[lang];path=RO if lang=='ro' else EN
 template='proiecte/partidul-ca-organizatie-responsabila.html' if lang=='ro' else 'en/projects/accountable-political-party.html'
 s=BeautifulSoup((P/template).read_text(),'html.parser')
 s.title.string=d['title']+' | Proiect România'
 for selector,value in [('meta[name="description"]',d['description']),('meta[property="og:title"]',d['title']),('meta[property="og:description"]',d['description']),('meta[property="og:url"]',BASE+path)]:s.select_one(selector)['content']=value
 s.select_one('link[rel="canonical"]')['href']=BASE+path
 for a in s.select('link[rel="alternate"]'):a['href']=BASE+(EN if a['hreflang']=='en' else RO)
 for a in s.select('.languages a'):a['href']=EN if a.get('lang')=='en' else RO
 for script in s.select('script[type="application/ld+json"]'):script.decompose()
 tag=s.new_tag('script',type='application/ld+json');tag.string=json.dumps({'@context':'https://schema.org','@type':'WebPage','name':d['title'],'url':BASE+path,'description':d['description'],'inLanguage':lang},ensure_ascii=False);s.head.append(tag)
 main=s.select_one('main');main.clear();main.append(BeautifulSoup(f'<article class="wrap dem-article"><a href="{"/proiecte" if lang=="ro" else "/en/projects"}">← {d["back"]}</a><p class="eyebrow">{d["tag"]}</p><h1>{d["title"]}</h1><p class="lead">{d["description"]}</p><div class="dem-body">{d["body"]}</div></article>','html.parser'))
 (P/(path.lstrip('/')+'.html')).write_text(str(s))
 for filename in (['index.html','proiecte.html'] if lang=='ro' else ['en.html','en/projects.html']):
  q=BeautifulSoup((P/filename).read_text(),'html.parser');old=q.select_one('#education-gcse-entry')
  if old:old.decompose()
  q.select_one('main').append(BeautifulSoup(card(lang),'html.parser'))
  (P/filename).write_text(str(q))
v=json.loads((P/'vercel.json').read_text())
for path in [RO,EN]:
 if not any(x['source']==path for x in v['rewrites']):v['rewrites'].append({'source':path,'destination':path+'.html'})
 if not any(x['source']==path+'.html' for x in v['redirects']):v['redirects'].append({'source':path+'.html','destination':path,'statusCode':301})
(P/'vercel.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns)
tree=ET.parse(P/'sitemap.xml');root=tree.getroot();known={x.text for x in root.findall('{'+ns+'}url/{'+ns+'}loc')}
for path in [RO,EN]:
 if BASE+path not in known:
  x=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(x,'{'+ns+'}loc').text=BASE+path
  ET.SubElement(x,'{'+ns+'}lastmod').text='2026-10-10'
tree.write(P/'sitemap.xml',encoding='utf-8',xml_declaration=True)
