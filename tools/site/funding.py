from pathlib import Path
from bs4 import BeautifulSoup
import html,json,re
P=Path(__file__).resolve().parents[2]
route='/oportunitati-de-finantare'
url=route+'/social-awards-2026'
title='Social Awards 2026: premii de până la 20.000 € pentru firme și ONG-uri care schimbă orașele'
desc='Concurs cu premii totale de 90.000 € pentru proiecte de regenerare urbană. Cine poate aplica, cum se punctează și până când.'
base=BeautifulSoup((P/'index.html').read_text(),'html.parser')
header=str(base.select_one('.site-header'));footer=str(base.select_one('.site-footer'))+str(base.select_one('#toast'))
# Article and listing are Romanian; they have no untranslated page counterpart.
h=BeautifulSoup(header,'html.parser');h.select_one('.languages').decompose();h.select_one('.site-nav').append(BeautifulSoup('<a href="'+route+'" aria-current="page">Oportunități de finanțare</a>','html.parser'));header=str(h)
def image():return '<img class="funding-city" src="/assets/img/city-960.webp" srcset="/assets/img/city-480.webp 480w, /assets/img/city-960.webp 960w, /assets/img/city-1600.webp 1600w" sizes="(max-width: 760px) 100vw, 900px" width="1600" height="2400" alt="Stradă urbană cu clădiri și arbori" decoding="async">'
def document(path,name,description,body,article=False):
 canonical='https://proiectromania.ro'+path
 schema={'@context':'https://schema.org','@type':'Article' if article else 'CollectionPage','headline':name,'description':description,'url':canonical,'inLanguage':'ro','image':'https://proiectromania.ro/assets/img/city-1600.webp'}
 if article:schema.update(datePublished='2026-10-07',publisher={'@type':'Organization','name':'Proiect România','url':'https://proiectromania.ro/'})
 return '<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><script>document.documentElement.classList.add("js")</script><title>'+html.escape(name)+' | Proiect România</title><meta name="description" content="'+html.escape(description,quote=True)+'"><link rel="canonical" href="'+canonical+'"><meta property="og:title" content="'+html.escape(name,quote=True)+'"><meta property="og:description" content="'+html.escape(description,quote=True)+'"><meta property="og:url" content="'+canonical+'"><meta property="og:type" content="'+('article' if article else 'website')+'"><meta property="og:image" content="https://proiectromania.ro/assets/img/city-960.webp"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/icon.svg"><link rel="stylesheet" href="/assets/site.css?rev=audit-20261003"><link rel="stylesheet" href="/assets/funding.css"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head><body class="platform-page"><a class="skip" href="#main">Mergi la conținut</a>'+header+'<main id="main">'+body+'</main>'+footer+'<script src="/assets/site.js?rev=audit-20261003" defer></script></body></html>'
article='<article class="funding-article wrap"><a class="funding-back" href="'+route+'">← Oportunități de finanțare</a><p class="eyebrow">OPORTUNITĂȚI DE FINANȚARE</p><h1>'+title+'</h1><p class="meta">Publicat la <time datetime="2026-10-07">7 octombrie 2026</time></p><aside class="funding-deadline"><strong>Termen: 6 noiembrie 2026, ora 23:59</strong></aside>'+image()+'<div class="funding-body">'+(P/'tools/site/source/social-awards-2026.html').read_text()+'</div><div class="funding-share"><button class="btn share" data-title="'+html.escape(title,quote=True)+'" data-text="'+html.escape(desc,quote=True)+'">Distribuie articolul ↗</button></div></article>'
p=P/(url.strip('/')+'.html');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(document(url,title,desc,article,True))
card='<article class="project-card"><div class="project-card-body"><p class="eyebrow">7 OCTOMBRIE 2026</p><h2><a href="'+url+'">'+title+'</a></h2><p>'+desc+'</p><p><strong>Termen: 6 noiembrie 2026, ora 23:59</strong></p><a class="btn" href="'+url+'">Citește articolul ↗</a></div></article>'
(P/(route.strip('/')+'.html')).write_text(document(route,'Oportunități de finanțare','Oportunități de finanțare pentru proiecte și comunități.', '<section class="page-intro wrap"><p class="eyebrow">RESURSE PENTRU COMUNITĂȚI</p><h1>Oportunități de finanțare</h1></section><section class="wrap funding-list">'+card+'</section>'))
# Keep discoverability on existing pages and after the main site generator runs.
for p in P.rglob('*.html'):
 if 'tools' in p.relative_to(P).parts or p.name in ['index-en.html','football-for-the-future.html','fotbal-pentru-viitor.html','frf2030.html']:continue
 s=p.read_text()
 if 'id="site-nav"' in s and 'href="'+route+'"' not in s:
  en='<html lang="en"' in s
  s=re.sub(r'(<nav[^>]*id="site-nav"[^>]*>.*?)(</nav>)',lambda m:m[1]+'<a href="'+route+'"'+(' lang="ro"' if en else '')+'>'+('Funding opportunities (RO)' if en else 'Oportunități de finanțare')+'</a>'+m[2],s,flags=re.S)
 if p==P/'index.html' and 'id="funding-home"' not in s:
  s=s.replace('</main>','<section class="section wrap" id="funding-home"><p class="eyebrow">OPORTUNITĂȚI DE FINANȚARE</p><h2>Social Awards 2026</h2><p>'+desc+'</p><p><strong>Termen: 6 noiembrie 2026, ora 23:59</strong></p><a class="btn" href="'+url+'">Citește articolul ↗</a></section></main>')
 p.write_text(s)
s=(P/'sitemap.xml').read_text()
for path in [route,url]:
 if 'https://proiectromania.ro'+path+'</loc>' not in s:s=s.replace('</urlset>','<url><loc>https://proiectromania.ro'+path+'</loc><lastmod>2026-10-07</lastmod></url></urlset>')
(P/'sitemap.xml').write_text(s)
print('Published funding section and article')

css=P/"assets/site.css"
if ".site-nav{flex-wrap:wrap}" not in css.read_text():css.write_text(css.read_text()+"\n.site-nav{flex-wrap:wrap}\n")
config=P/'vercel.json'
v=json.loads(config.read_text())
for path in [route,url]:
 if not any(x['source']==path for x in v['rewrites']):v['rewrites'].append({'source':path,'destination':path+'.html'})
 if not any(x['source']==path+'.html' for x in v['redirects']):v['redirects'].append({'source':path+'.html','destination':path,'statusCode':301})
config.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

# Keep shared navigation and discovery pages compact after content updates.
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('navigation.py')))
