"""Shared editorial covers: authentic marks, photography and type, never placeholder icons."""
from pathlib import Path
from html import escape
P=Path(__file__).resolve().parents[2]
OFFICIAL={
'/proiecte/code-kids':('/assets/img/official/code-kids.webp','CODE Kids'),
'/proiecte/harta-reciclarii':('/assets/img/official/harta-reciclarii.png','Harta Reciclării'),
'/proiecte/scoala-de-bani':('/assets/img/official/scoala-de-bani.svg','Școala de Bani'),
'/proiecte/ajungem-mari':('/assets/img/official/ajungem-mari.png','Ajungem MARI'),
'/proiecte/hopefriday':('/assets/img/hopefriday-logo.jpg','HopeFriday'),
'/proiecte/gcse-limba-romana':('/assets/img/romanian-gcse-logo.png','Romanian GCSE')}
TITLES={
'/proiecte/partidul-ca-organizatie-responsabila':('Organizație.\nResponsabilitate.','Organisation.\nAccountability.'),
'/proiecte/cum-infiintezi-o-asociatie':('De la idee\nla asociație.','From an idea\nto an association.'),
'/proiecte/porneste-un-proiect-local':('Schimbarea\nîncepe local.','Change\nstarts locally.'),
'/proiecte/competente-digitale-parinti-bunici':('Digital.\nPe înțelesul tău.','Digital.\nAt your pace.'),
'/proiecte/sah-in-scoli':('Următoarea\nmutare.','The next\nmove.'),
'/proiecte/ajungem-mari':('Timp oferit.\nViitor construit.','Time given.\nFutures built.')}
GUIDES={'/proiecte/partidul-ca-organizatie-responsabila','/proiecte/cum-infiintezi-o-asociatie','/proiecte/porneste-un-proiect-local','/proiecte/competente-digitale-parinti-bunici'}
def visual(entry,en=False):
 path,ep,cat,ro,eng,rd,ed,author,img=entry
 if path=='/proiecte/fotbal-pentru-viitor':
  return '<div class="editorial-visual visual-photo"><img src="/assets/img/football-960.webp" alt="" loading="lazy" decoding="async"/><span>'+('GRASSROOTS FOOTBALL' if en else 'FOTBAL DE BAZĂ')+'</span></div>'
 if path=='/proiecte/fertilizare-in-vitro':
  return '<div class="editorial-visual visual-photo"><img src="/assets/img/fiv-support-editorial.png" alt="'+('Illustrative AI-generated image of hands offering support' if en else 'Imagine ilustrativă generată cu AI: mâini oferind sprijin')+'" loading="lazy" decoding="async"/><span>'+('INFORMATION & SUPPORT' if en else 'INFORMARE ȘI SPRIJIN')+'</span></div>'
 if path in OFFICIAL and (P/OFFICIAL[path][0].lstrip('/')).exists():
  src,label=OFFICIAL[path]
  return '<div class="editorial-visual visual-brand"><img src="'+src+'" alt="'+escape(label)+'" loading="lazy" decoding="async"/></div>'
 title=TITLES.get(path,(ro,eng))[en]
 label=('PRACTICAL GUIDE' if en else 'GHID PRACTIC') if path in GUIDES else ('INITIATIVE' if en else 'INIȚIATIVĂ')
 title='<br/>'.join(escape(line) for line in title.split('\n'))
 return f'<div class="editorial-visual visual-type tone-{cat}" aria-hidden="true"><span class="cover-kicker">{label}</span><strong>{title}</strong><span class="cover-baseline">PROIECT ROMÂNIA <span>↗</span></span></div>'
