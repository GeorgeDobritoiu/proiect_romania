"""Build the Romanian association handbook and its English introduction."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, runpy, xml.etree.ElementTree as ET
P=Path(__file__).resolve().parents[2]
RO='/proiecte/cum-infiintezi-o-asociatie'; EN='/en/projects/start-an-association'; BASE='https://proiectromania.ro'
body=(P/'tools/site/source/asociatie.html').read_text()
english='''<aside class="dem-note">This guide concerns Romania. The full practical handbook is available in Romanian. Legal references were checked on 10 October 2026; operational budgets, roles and targets are proposals, not statutory requirements.</aside><h2>Build a useful organisation</h2><p>Start with a specific local need, a team and a realistic budget. The handbook covers formation, the statute, registration, ongoing administration, membership fees, volunteering, financial controls and measurable results.</p><h2>Two practical routes</h2><ul><li><strong>Nonprofit sports club:</strong> distinguish association registration from recognition as a sports structure, sporting registration and competition affiliation.</li><li><strong>Animal welfare:</strong> distinguish supporting veterinary care and responsible adoption from operating an animal shelter. Registration as an association does not itself authorise shelter operations.</li></ul><h2>Tools to use</h2><p>A 90-day planning framework, a budget worksheet, eight operational indicators and five templates help founders assign tasks and review progress.</p><p><a class="btn" href="/proiecte/cum-infiintezi-o-asociatie">Read the full Romanian handbook →</a></p><p><a href="/proiecte/cum-infiintezi-o-asociatie#surse">Official legal sources and checks before filing</a></p>'''
for lang,route,title,desc,content in [('ro',RO,'Cum înființezi și organizezi o asociație','Ghid practic pentru România: înființare, club sportiv, protecția animalelor, buget, voluntari și primele 90 de zile.',body),('en',EN,'Start and run an association in Romania','A practical handbook for nonprofit sports clubs and animal welfare associations. Full guide in Romanian.',english)]:
 s=BeautifulSoup((P/('proiecte/gcse-limba-romana.html' if lang=='ro' else 'en/projects/romanian-gcse.html')).read_text(),'html.parser')
 s.title.string=title+' | Proiect România'
 for sel,value in [('meta[name="description"]',desc),('meta[property="og:title"]',title),('meta[property="og:description"]',desc),('meta[property="og:url"]',BASE+route)]:s.select_one(sel)['content']=value
 s.select_one('link[rel="canonical"]')['href']=BASE+route
 for a in s.select('link[rel="alternate"]'):a['href']=BASE+(EN if a.get('hreflang')=='en' else RO)
 for a in s.select('.languages a'):a['href']=EN if a.get('lang')=='en' else RO
 for x in s.select('script[type="application/ld+json"]'):x.decompose()
 x=s.new_tag('script',type='application/ld+json');x.string=json.dumps({'@context':'https://schema.org','@type':'Article','headline':title,'url':BASE+route,'inLanguage':lang,'author':{'@type':'Person','name':'George Dobritoiu'},'dateModified':'2026-10-10'},ensure_ascii=False);s.head.append(x)
 parsed=BeautifulSoup(content,'html.parser')
 toc='<nav class="manual-toc" aria-label="Cuprins"><h2>Cuprins</h2><ol>'+''.join(f'<li><a href="#{sec["id"]}">{sec.h2.get_text().split(". ",1)[1]}</a></li>' for sec in parsed.select('section[id]'))+'</ol></nav>' if lang=='ro' else ''
 main=s.select_one('main');main.clear();main.append(BeautifulSoup(f'<article class="wrap dem-article"><a href="{"/proiecte" if lang=="ro" else "/en/projects"}">← {"Toate proiectele" if lang=="ro" else "All projects"}</a><p class="eyebrow">{"ASOCIAȚII · GHID PRACTIC" if lang=="ro" else "ASSOCIATIONS · PRACTICAL GUIDE"}</p><h1>{title}</h1><p class="lead">{desc}</p><p class="meta">George Dobritoiu · 10.10.2026</p>{toc}<div class="dem-body">{content}</div></article>','html.parser'))
 (P/(route.lstrip('/')+'.html')).write_text(str(s))
v=json.loads((P/'vercel.json').read_text())
for route in [RO,EN]:
 if not any(x['source']==route for x in v['rewrites']):v['rewrites'].append({'source':route,'destination':route+'.html'})
 if not any(x['source']==route+'.html' for x in v['redirects']):v['redirects'].append({'source':route+'.html','destination':route,'statusCode':301})
(P/'vercel.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns);tree=ET.parse(P/'sitemap.xml');root=tree.getroot();known={x.text for x in root.findall('{'+ns+'}url/{'+ns+'}loc')}
for route in [RO,EN]:
 if BASE+route not in known:
  x=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(x,'{'+ns+'}loc').text=BASE+route;ET.SubElement(x,'{'+ns+'}lastmod').text='2026-10-10'
tree.write(P/'sitemap.xml',encoding='utf-8',xml_declaration=True)
runpy.run_path(str(Path(__file__).with_name('navigation.py')))
