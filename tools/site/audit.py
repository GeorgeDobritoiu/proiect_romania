#!/usr/bin/env python3
"""Refresh the static 544 journal from CSV; HTML templates own the shared shell.

The two committed HTML pages are editorial templates. This generator modifies
only the journal tbody and its explanatory paragraph, preserving the site's
navigation/header/footer without embedding duplicate shell markup.
"""
from pathlib import Path
import csv
import html
import re

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "data/audit/cereri_544.csv"
PAGE = ROOT / "audit/cereri-544.html"
ABOUT = ROOT / "despre.html"
PAGES = (ROOT / "audit/metodologie.html", PAGE, ROOT / "audit/metodologie-tehnica.html")
LABELS = {
    "pregatita_netrimisa": "Pregătită, netrimisă",
    "trimisa": "Trimisă",
    "depusa": "Depusă",
    "inregistrata": "Înregistrată",
    "raspuns_partial": "Răspuns parțial",
    "raspuns_complet": "Răspuns complet",
    "refuz": "Refuz",
    "contestata": "Contestată",
}
COLUMNS = ("destinatar", "subiect", "status", "data_trimiterii",
           "nr_inregistrare", "termen_legal", "data_raspuns")

def render_rows(rows):
    rendered = []
    for row in rows:
        cells = []
        for column in COLUMNS:
            value = row.get(column, "") or "—"
            if column == "status":
                value = LABELS.get(value, value)
            cells.append("<td>" + html.escape(value, quote=True) + "</td>")
        rendered.append("<tr>" + "".join(cells) + "</tr>")
    return "\n".join(rendered)

def sync_shell():
    """Reuse the current generated /despre shell; never hardcode navigation."""
    about = ABOUT.read_text(encoding="utf-8")
    header = re.search(r'<a class="skip"[\\s\\S]*?</header>', about).group()
    header = header.replace(' aria-current="page" href="/despre"', ' href="/despre"')
    footer = re.search(r'<footer class="site-footer"[\\s\\S]*?</footer>', about).group()
    styles = "\\n".join(re.findall(r'<link[^>]+rel="stylesheet"[^>]*/>', about))
    for path in PAGES:
        page = path.read_text(encoding="utf-8")
        page = re.sub(r'<a class="skip"[\\s\\S]*?</header>', lambda _: header, page, count=1)
        page = re.sub(r'<footer class="site-footer"[\\s\\S]*?</footer>', lambda _: footer, page, count=1)
        page = re.sub(r'<link[^>]+rel="stylesheet"[^>]*/>(?:\\n<link[^>]+rel="stylesheet"[^>]*/>)*', lambda _: styles, page, count=1)
        path.write_text(page, encoding="utf-8")

def main():
    sync_shell()
    with CSV.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    page = PAGE.read_text(encoding="utf-8")
    new = re.sub(r"(?<=<tbody>).*?(?=</tbody>)", "\n" + render_rows(rows) + "\n",
                 page, count=1, flags=re.DOTALL)
    if new == page and "<tbody>" not in page:
        raise RuntimeError("Missing journal table body")
    PAGE.write_text(new, encoding="utf-8")

if __name__ == "__main__":
    main()
