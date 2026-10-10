# Proiect România

Static bilingual HTML/CSS/JavaScript website. Vercel preset: Other; no build command; output directory `.`.

## Routes

Romanian: `/`, `/proiecte`, `/cum-functioneaza`, `/propune-un-proiect`, `/despre`, `/contact`, `/confidentialitate`, `/proiecte/fotbal-pentru-viitor`.
English: `/en`, `/en/projects`, `/en/how-it-works`, `/en/propose-a-project`, `/en/about`, `/en/contact`, `/en/privacy`, `/en/projects/football-for-the-future`.

`vercel.json` uses explicit rewrites for clean URLs and direct HTTP 301 redirects. Automatic `cleanUrls` is disabled because it inserted an HTTP 308 before legacy redirects. All existing PDF names are retained unchanged.

## Editing

Shared platform styles and interactions: `assets/site.css`, `assets/site.js`. Football retains its detailed content and legacy anchors with `assets/football.css`.

Source project registry: `data/proiecte.json`. Cards are rendered into HTML so reading and navigation work without JavaScript. One published project currently; domain recruitment calls are not projects.

Page generator: `tools/site/build.py` (Python + beautifulsoup4). Run from any directory to regenerate HTML. Football content sources are under `tools/site/source/`. CSS and JavaScript are edited directly. The generator is an authoring convenience, not a deployment dependency. Extend the card loop and route list when adding projects.

## Preview review gates

The reviewed restructuring was published on 3 October 2026. `main` and `restructurare-site` include the release. Preview-only notices appear on localhost and Vercel preview hosts; hidden by default on the production custom domain.

Before production confirm: origin story, legal data controller/contact, privacy legal basis and retention, editorial decision maker, response time and author withdrawal procedure. Privacy is explicitly a draft. No institutional partnerships are implied.

The contact form prepares a WhatsApp message using the existing recipient. It never sends automatically. Email is not activated; do not replace with a fake endpoint. Replace WhatsApp only once an active email and a working, privacy-reviewed form service are available.

PDFs are Romanian. English pages explicitly label the presentation as translated and downloads as Romanian.

## Images

See `CREDITS.md`. Two relevant photos (a real Bucharest street and football pitch), three responsive WebP sizes each. No generated people. Avoid decorative image quotas. System fonts keep loading light and support Romanian diacritics.

## Verification

Check 390px and 1440px views, menu and keyboard focus, no horizontal overflow, WhatsApp draft without sending, language counterpart links and all legacy anchors. After deployment verify the real 301 status for old RO/EN football URLs, including `.html`, and successful PDF downloads. Lighthouse scores should be measured, not assumed.

## Democracy and good governance

The bilingual section is at `/democratie-si-buna-guvernare` and `/en/democracy-and-governance`. It contains George Dobritoiu’s conceptual party-governance proposal and editorial references to three independently operated civic initiatives. No affiliations or active registration calls are implied.

Run `python tools/site/democracy.py` after other page generators to regenerate these pages, home/project entry points, routes and sitemap entries. Its source contains both language versions; styling is in `assets/democracy.css`. The generator preserves unrelated page content.

### Manualul partidului responsabil

Sursa editorială: `docs/manual-partid-responsabil.html`. Conține cerințe legale citate distinct de propunerile operaționale. După editare, rulați `python tools/site/manual.py` pentru PDF (ReportLab și fonturi DejaVu Sans), apoi `python tools/site/democracy.py` pentru paginile publice. Verificați vizual PDF-ul și pagina pe mobil înainte de publicare. PDF: `downloads/manual-partid-responsabil.pdf`. Sursele au data verificării 10.10.2026; normele trebuie reverificate la fiecare ediție.
