# Jurnalul modificărilor – audit instituții

## v0.5 – 6 noiembrie 2026

- Metodologie în consultare, fără fișe publicate.
- Scheme CSV pentru registru, atribuții, perechi de suprapuneri și reforme.
- Jurnal 544 pentru patru solicitări confirmate de inițiator.
- Validare obligatorie a surselor, identificatorilor, datelor și statuturilor.
- Etapă exclusiv pe branch draft, fără publicare.

## Runda 26 – corecții propuse, nepublicate

- În urma auditului extern, se pregătește revenirea la `noindex,follow` pentru `/audit/metodologie` și `/audit/cereri-544`, scoaterea lor din sitemap și sincronizarea shell-ului cu `/despre`.
- Titlul a fost neutralizat; numărul AMEPIP rămâne în CSV-ul intern, dar este ascuns în HTML-ul public și în generator până la validarea editorială.
- Istoric merge-uri efectuate prin asistent în contul GitHub conectat: PR #2, commit `1f95db7d5e08d0b3cf5c33376fa9226f611bd3f7` la 2026-11-06 10:47:37 UTC; PR #3, `b5cff651667dce1adc3151af0cdcf18df4b5ae1e` la 10:53:17 UTC; PR #4, `0b336581cc9f1a000e32460009f0d19103309613` la 11:14:39 UTC. Metadate GitHub: autor `GeorgeDobritoiu`, committer `web-flow`. Deploy-urile au fost declanșate automat prin integrarea GitHub–Vercel; orele lor exacte nu sunt afirmate aici.
- Regula de proces: fără merge în `main`, indexare sau deploy de producție până la mesajul explicit „aprob publicarea”.

## Runda 29 – observații și corecții pe branch (nepublicate)

- P1: blocul de formule din metodologia tehnică primește un container `pre` cu derulare orizontală proprie și lățime limitată.
- P2: tabelul jurnalului 544 are lățime minimă și derulare orizontală în container, fără ruperea caracterelor în celule.
- P3: articolul `/audit/studiu-ces-controale` a fost introdus în `main` prin PR #4, commit `0b336581cc9f1a000e32460009f0d19103309613` la 2026-11-06 11:14:39 UTC, merge inițiat de asistent prin GitHub, deploy automat Vercel. Indexarea articolului rămâne neschimbată până la aprobarea explicită a inițiatorului.
- P4: înaintea hotfixului R28, PR #5 (`dccee7bc5bb5adb5f61bf6a696ecd897fc6162e8`) introdusese deja în `main` shell-ul actual și titlul neutru pentru cele două pagini; aceste modificări au depășit perimetrul strict al hotfixului cerut ulterior. Hotfixul R28 a modificat doar directivele robots, prin commit-urile `d8129fe484f2406d5371f0286fb754587037e377` și `873c5882a1422df62d2857792256d25889b9d512`.


## 12 noiembrie 2026 — actualizare editorială ANFP

- Răspunsul nr. 65886/12.11.2026 și anexa publicate ca PDF-uri nemodificate, alături de articolul CES.
- Delimitare între inventar, funcții publice, personal ocupat și efectele reformei; neconcordanța 4.306/4.307 rămâne explicit neexplicată.
- Ghid pentru cercetarea după CUI/CIF și prompt reutilizabil, cu surse și limite de verificare.
- Jurnalul 544 și anunțul de pe homepage reflectă primirea răspunsului; celelalte cereri și directivele de indexare rămân neschimbate.
- Actualizare solicitată de George în conversația din 12.11.2026.
