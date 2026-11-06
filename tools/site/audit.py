#!/usr/bin/env python3
"""Generează două pagini statice în shell-ul existent, fără navigație sau sitemap."""
from pathlib import Path
import csv,html
P=Path(__file__).resolve().parents[2]
HEADER="<a class=\"skip\" href=\"#main\">Mergi la conținut</a><header class=\"site-header\"><a aria-label=\"Proiect România — Acasă\" class=\"site-brand\" href=\"/\"><img alt=\"\" class=\"brand-map\" height=\"52\" src=\"/assets/img/proiect-romania-logo-tricolor.png\" width=\"78\"/><span class=\"brand-wordmark\"><small>PROIECT</small><strong>ROMÂNIA<span class=\"brand-dot\">.</span></strong></span></a><button aria-controls=\"site-nav\" aria-expanded=\"false\" class=\"menu-toggle\">Meniu</button><nav aria-label=\"Navigare principală\" class=\"site-nav\" id=\"site-nav\"><a href=\"/\">Acasă</a><details class=\"nav-projects\"><summary>Proiecte <span aria-hidden=\"true\">⌄</span></summary><div class=\"nav-project-panel\"><a class=\"nav-all-projects\" href=\"/proiecte\">Toate proiectele <span aria-hidden=\"true\">→</span></a><a href=\"/proiecte#sport\">Sport <span aria-hidden=\"true\">↗</span></a><a href=\"/proiecte#solidaritate\">Solidaritate <span aria-hidden=\"true\">↗</span></a><a href=\"/proiecte#educatie\">Educație <span aria-hidden=\"true\">↗</span></a><a href=\"/proiecte#democratie\">Democrație <span aria-hidden=\"true\">↗</span></a><a href=\"/proiecte#mediu\">Mediu și comunitate <span aria-hidden=\"true\">↗</span></a><a href=\"/proiecte#sanatate\">Sănătate și familie <span aria-hidden=\"true\">↗</span></a></div></details><details class=\"nav-projects\"><summary>Finanțare <span aria-hidden=\"true\">⌄</span></summary><div class=\"nav-project-panel\"><a href=\"/oportunitati-de-finantare\">Oportunități de finanțare</a><a href=\"/proiecte-de-sustinut\">Proiecte de susținut</a><a href=\"/proiecte-de-sustinut#crowdfunding\">Crowdfunding — în pregătire</a></div></details><a href=\"/despre\">Despre</a><a href=\"/contact\">Contact</a><a class=\"nav-cta\" href=\"/propune-un-proiect\">Propune un proiect</a></nav></header>"
FOOTER="<footer class=\"site-footer\"><div><a aria-label=\"Proiect România — Acasă\" class=\"site-brand\" href=\"/\"><img alt=\"\" class=\"brand-map\" height=\"52\" src=\"/assets/img/proiect-romania-logo-tricolor.png\" width=\"78\"/><span class=\"brand-wordmark\"><small>PROIECT</small><strong>ROMÂNIA<span class=\"brand-dot\">.</span></strong></span></a><p>Idei argumentate. Proiecte cu un plan.</p></div><div><a href=\"/propune-un-proiect\">Contribuie cu un proiect</a><a href=\"/confidentialitate\">Confidențialitate</a><a href=\"/CREDITS.md\">Credite foto</a><a href=\"/cum-functioneaza\">Cum funcționează</a></div><p>O inițiativă de George Dobritoiu.</p></footer>"
def esc(x):return html.escape(str(x),quote=True)
def section(title,content):return f'<section class="text-section"><h2>{esc(title)}</h2>{content}</section>'
def render(path,title,body):
    page=f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{esc(title)} | Proiect România</title>
<link rel="stylesheet" href="/assets/site.css">
<style>
.audit-content{{max-width:980px;margin:36px auto 80px;padding:0 20px;overflow-wrap:anywhere}}
.audit-content section{{margin:34px 0}}
.audit-content h1{{line-height:1.16}}
.audit-content a:focus-visible{{outline:3px solid #125e70;outline-offset:3px}}
.audit-table-wrap{{max-width:100%;overflow-x:auto}}
.audit-table{{width:100%;border-collapse:collapse;font-size:.92rem}}
.audit-table th,.audit-table td{{padding:12px;text-align:left;border-bottom:1px solid #d3dedc;vertical-align:top}}
.audit-table th{{background:#edf5f3}}
.audit-table td{{overflow-wrap:anywhere}}
@media(max-width:600px){{.audit-content{{padding:0 16px}}.audit-table{{font-size:.82rem}}}}
</style>
</head>
<body class="platform-page">
<a class="skip" href="#main">Mergi la conținut</a><header class="site-header"><a aria-label="Proiect România — Acasă" class="site-brand" href="/"><img alt="" class="brand-map" height="52" src="/assets/img/proiect-romania-logo-tricolor.png" width="78"/><span class="brand-wordmark"><small>PROIECT</small><strong>ROMÂNIA<span class="brand-dot">.</span></strong></span></a><button aria-controls="site-nav" aria-expanded="false" class="menu-toggle">Meniu</button><nav aria-label="Navigare principală" class="site-nav" id="site-nav"><a href="/">Acasă</a><details class="nav-projects"><summary>Proiecte <span aria-hidden="true">⌄</span></summary><div class="nav-project-panel"><a class="nav-all-projects" href="/proiecte">Toate proiectele <span aria-hidden="true">→</span></a><a href="/proiecte#sport">Sport <span aria-hidden="true">↗</span></a><a href="/proiecte#solidaritate">Solidaritate <span aria-hidden="true">↗</span></a><a href="/proiecte#educatie">Educație <span aria-hidden="true">↗</span></a><a href="/proiecte#democratie">Democrație <span aria-hidden="true">↗</span></a><a href="/proiecte#mediu">Mediu și comunitate <span aria-hidden="true">↗</span></a><a href="/proiecte#sanatate">Sănătate și familie <span aria-hidden="true">↗</span></a></div></details><details class="nav-projects"><summary>Finanțare <span aria-hidden="true">⌄</span></summary><div class="nav-project-panel"><a href="/oportunitati-de-finantare">Oportunități de finanțare</a><a href="/proiecte-de-sustinut">Proiecte de susținut</a><a href="/proiecte-de-sustinut#crowdfunding">Crowdfunding — în pregătire</a></div></details><a href="/despre">Despre</a><a href="/contact">Contact</a><a class="nav-cta" href="/propune-un-proiect">Propune un proiect</a></nav></header>
<main id="main" class="audit-content">
{body}
</main>
<footer class="site-footer"><div><a aria-label="Proiect România — Acasă" class="site-brand" href="/"><img alt="" class="brand-map" height="52" src="/assets/img/proiect-romania-logo-tricolor.png" width="78"/><span class="brand-wordmark"><small>PROIECT</small><strong>ROMÂNIA<span class="brand-dot">.</span></strong></span></a><p>Idei argumentate. Proiecte cu un plan.</p></div><div><a href="/propune-un-proiect">Contribuie cu un proiect</a><a href="/confidentialitate">Confidențialitate</a><a href="/CREDITS.md">Credite foto</a><a href="/cum-functioneaza">Cum funcționează</a></div><p>O inițiativă de George Dobritoiu.</p></footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
    dest=P/(path+".html");dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page,encoding="utf-8")
def main():
    body="""<p class="eyebrow">METODOLOGIE ÎN CONSULTARE · v0.5</p>
<h1>Auditul instituțiilor publice – metodologie</h1>
<p class="lead">Metodologie în consultare. Nu există încă fișe de instituții publicate.</p>
"""
    body+=section("1. Registrul instituțiilor","<p>Inventariem instituțiile, mandatul legal, relațiile de subordonare, indicatorii anuali și sursele verificabile. Nu confundăm bugetele consolidate cu cheltuielile instituțiilor componente.</p>")
    body+=section("2. Analiza atribuțiilor și reorganizării","<p>Analizăm separat suprapunerea juridică, intersecția dintre competența generală și cea specială, suprapunerea operațională, cooperarea reglementată și suprapunerea percepută. Alternativele includ coordonarea, procedurile comune, interoperabilitatea digitală și reorganizarea, fără a presupune că o comasare economisește bani.</p>")
    body+=section("3. Verificarea reformelor promise","<p>Urmărim cronologic anunțurile, actele normative, bugetele și execuția. <strong>Anunțat ≠ bugetat ≠ realizat.</strong> Screening-ul art. XXIX din Legea nr. 296/2023 este o verificare juridică contextuală, cu excepții și versiuni istorice ale legii; nu atribuim aici statut de conformitate niciunei instituții.</p>")
    body+=section("Reguli de integritate","<ul><li>Presa = ipoteză; documentul primar = dovadă.</li><li>Fără scor public, calificative sau nume de persoane.</li><li>Drept la replică: 15 zile lucrătoare înainte de orice fișă.</li><li>Tabelele se verifică pe randare vizuală și se documentează metoda extragerii.</li><li>Corecțiile și conflictele de interese se consemnează trasabil.</li></ul>")
    body+=section("Limitele etapei","<p>Companiile de stat și organizațiile neguvernamentale aparțin unor etape separate, ulterioare. Această pagină nu conține evaluări individuale sau recomandări de desființare.</p><p><a href='/audit/cereri-544'>Jurnalul cererilor de informații (Legea 544/2001)</a></p>")
    render("audit/metodologie", "Auditul instituțiilor publice – metodologie v0.5",body)
    with (P/"data/audit/cereri_544.csv").open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
    heads=["Destinatar","Subiect","Stadiu","Data trimiterii","Număr înregistrare","Termen legal","Data răspunsului"]
    keys=["destinatar","subiect","status","data_trimiterii","nr_inregistrare","termen_legal","data_raspuns"]
    table='<div class="audit-table-wrap"><table class="audit-table"><thead><tr>'+''.join(f'<th scope="col">{esc(h)}</th>' for h in heads)+'</tr></thead><tbody>'
    for row in rows:table+='<tr>'+''.join(f'<td>{esc(row.get(k) or "—")}</td>' for k in keys)+'</tr>'
    table+='</tbody></table></div>'
    body='<p class="eyebrow">TRANSPARENȚĂ · LEGEA 544/2001</p><h1>Jurnalul cererilor de informații</h1><p>Solicitările sunt marcate ca trimise conform confirmării solicitantului; datele de trimitere, numerele de înregistrare și termenele rămân necompletate până la verificarea dovezilor.</p>'+table+'<p><a href="/audit/metodologie">Înapoi la metodologie</a></p>'
    render("audit/cereri-544","Jurnalul cererilor 544",body)
if __name__=="__main__":main()
