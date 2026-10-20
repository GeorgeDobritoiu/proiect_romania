"""Render funding registry with explicit offset-aware expiry; safe to run daily."""
from pathlib import Path
from datetime import datetime, timezone
import json, html
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[2]
def expired(entry, now):
    return now >= datetime.fromisoformat(entry['expires_at'])
def render(now=None):
    now=now or datetime.now(timezone.utc)
    entries=json.loads((P/'data/finantari.json').read_text())
    doc=BeautifulSoup((P/'oportunitati-de-finantare.html').read_text(),'html.parser')
    main=doc.select_one('main');main.clear()
    main.append(BeautifulSoup('''<section class="page-intro wrap"><p class="eyebrow">RESURSE PENTRU COMUNITĂȚI</p><h1>Oportunități de finanțare</h1><p>Granturi, premii și incubatoare pentru inițiative din România. Vezi cine poate aplica, suma și termenul fiecărui apel.</p><nav class="funding-tabs" aria-label="Secțiuni finanțare"><a class="btn" href="#active">Apeluri active</a><a class="btn" href="#arhiva">Arhivă</a></nav><p class="meta">Termenele sunt în ora României. Pentru apelurile fără oră publicată, confirmă ora cu organizatorul; arhivarea se face la începutul zilei următoare. Finanțarea se acordă prin selecție. Proiect România nu gestionează înscrierile.</p><noscript><p>JavaScript este dezactivat: clasificarea reflectă ultima actualizare a paginii. Verifică data-limită și sursa oficială.</p></noscript></section><section class="wrap funding-list" id="active" aria-labelledby="active-title"><h2 id="active-title">Apeluri active</h2><div id="funding-active"></div><p id="funding-active-empty">Nu există apeluri active în această selecție.</p></section><section class="wrap funding-list" id="arhiva" aria-labelledby="archive-title"><h2 id="archive-title">Arhivă — înscrieri închise</h2><p>Apelurile expirate rămân disponibile pentru documentare. O ediție nouă se publică separat, după verificarea condițiilor.</p><div id="funding-archive"></div><p id="funding-archive-empty">Niciun apel arhivat încă.</p></section>''','html.parser'))
    for e in sorted(entries,key=lambda x:x['expires_at']):
        closed=expired(e,now)
        if 'legacy_html' in e:
            card=BeautifulSoup(e['legacy_html'],'html.parser').article
        else:
            esc=html.escape
            markup=f'''<article class="project-card"><div class="project-card-body"><p class="eyebrow">{esc(e['area'])}</p><h2>{esc(e['title'])}</h2><p class="funding-amount">{esc(e['amount'])}</p>{e['body']}<p><a class="btn" href="{esc(e['source'],quote=True)}" target="_blank" rel="noopener noreferrer">{esc(e['source_label'])} ↗</a></p></div></article>'''
            card=BeautifulSoup(markup,'html.parser').article
        card['id']=e['id'];card['data-funding-expiry']=e['expires_at']
        card['data-funding-status']='expired' if closed else 'active'
        holder=card.select_one('.project-card-body')
        badge=doc.new_tag('p',attrs={'class':'funding-status','data-funding-label':''})
        badge.string='Înscrieri închise' if closed else 'Apel activ';holder.insert(0,badge)
        term=doc.new_tag('p',attrs={'class':'funding-term'});term.string='Termen: '+e['deadline'];holder.insert(2,term)
        verified=doc.new_tag('p',attrs={'class':'meta'});verified.string='Ultima verificare editorială: '+e['verified_at']+'.';holder.append(verified)
        main.select_one('#funding-archive' if closed else '#funding-active').append(card)
    for kind in ['active','archive']:
        empty=not main.select_one('#funding-'+kind).select('article')
        el=main.select_one('#funding-'+kind+'-empty')
        if not empty:el['hidden']=''
    if not doc.select_one('script[src="/assets/funding.js"]'):
        doc.body.append(doc.new_tag('script',src='/assets/funding.js',defer=''))
    (P/'oportunitati-de-finantare.html').write_text(str(doc))
    # The existing full article must also advertise its closed status after expiry.
    file=P/'oportunitati-de-finantare/social-awards-2026.html'
    article=BeautifulSoup(file.read_text(),'html.parser')
    banner=article.select_one('#funding-expiry-notice')
    if banner:banner.decompose()
    e=next(e for e in entries if e['id']=='social-awards-2026')
    banner=article.new_tag('aside',attrs={'id':'funding-expiry-notice','class':'funding-deadline','data-funding-expiry':e['expires_at']})
    label=article.new_tag('strong',attrs={'data-funding-label':''});label.string='Înscrieri închise — articol arhivat.' if expired(e,now) else 'Termen înscrieri: 6 noiembrie 2026, ora 23:59 (România).'
    banner.append(label)
    link=article.new_tag('a',href='/oportunitati-de-finantare#arhiva');link.string=' Vezi arhiva finanțărilor';banner.append(link)
    article.select_one('h1').insert_after(banner)
    if not article.select_one('script[src="/assets/funding.js"]'):article.body.append(article.new_tag('script',src='/assets/funding.js',defer=''))
    file.write_text(str(article))
if __name__=='__main__':render()
