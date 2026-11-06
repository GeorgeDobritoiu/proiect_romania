# Auditul instituțiilor publice – schema v0.5

Metodologie în consultare; fără fișe de instituții. Fiecare CSV are antet UTF-8, fără înregistrări, cu excepția jurnalului 544.

Valorile monetare sunt estimări distincte de execuția realizată; un câmp gol înseamnă necunoscut, nu zero. Datele și statuturile nu se inventează.

## Dicționar de coloane

### institutii.csv

| Coloană | Definiție |
|---|---|
| `institutie_id` | Cheie către institutii.institutie_id |
| `denumire` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `cui` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_institutie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `autoritate_parinte_id` | Identificator / cheie de legătură |
| `personalitate_juridica` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `statut` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_infiintarii` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_incetarii` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### relatii_institutii.csv

| Coloană | Definiție |
|---|---|
| `relatie_id` | Identificator / cheie de legătură |
| `institutie_sursa_id` | Identificator / cheie de legătură |
| `institutie_destinatie_id` | Identificator / cheie de legătură |
| `tip_relatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_inceput` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_sfarsit` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### indicatori.csv

| Coloană | Definiție |
|---|---|
| `indicator_id` | Identificator / cheie de legătură |
| `institutie_id` | Cheie către institutii.institutie_id |
| `indicator_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `an` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `valoare` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `unitate` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `perimetru` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_verificarii` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |
| `verificator_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

### indicatori_dictionar.csv

| Coloană | Definiție |
|---|---|
| `indicator_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `denumire` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `definitie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `unitate` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `granularitate` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `metoda_calcul` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

### surse.csv

| Coloană | Definiție |
|---|---|
| `sursa_id` | Cheie către surse.sursa_id |
| `titlu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `emitent` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `url` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_document` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_accesarii` | Data ISO 8601 a accesării sursei |
| `tip_sursa` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `metoda_extragere` | text_structurat / paragrafe_tabel / randare_vizuala / OCR / verificare_incrucisata |
| `verificare_tabel` | neverificat / verificat_vizual / reconciliat |
| `offset_pagina` | Diferența între numerotarea PDF și pagina tipărită |
| `hash_sha256` | Amprenta SHA-256 a fișierului, dacă e verificată |
| `observatii` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

### atributii.csv

| Coloană | Definiție |
|---|---|
| `atributie_id` | Identificator / cheie de legătură |
| `institutie_id` | Cheie către institutii.institutie_id |
| `functie_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `descriere` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `temei_legal` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_competenta` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_intersectie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `cofog_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `regim_juridic` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### audit_corectii.csv

| Coloană | Definiție |
|---|---|
| `corectie_id` | Identificator / cheie de legătură |
| `tabel` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tinta_id` | Identificator / cheie de legătură |
| `camp` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `valoare_anterioara` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `valoare_noua` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `motiv` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_corectie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |
| `verificator_cod` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

### scenarii_reorganizare.csv

| Coloană | Definiție |
|---|---|
| `scenariu_id` | Identificator / cheie de legătură |
| `titlu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_scenariu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `ipoteze` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `cost_tranzitie_estimat` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `economie_estimata` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `orizont_ani` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `stadiu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### scenariu_institutii.csv

| Coloană | Definiție |
|---|---|
| `legatura_id` | Identificator / cheie de legătură |
| `scenariu_id` | Identificator / cheie de legătură |
| `institutie_id` | Cheie către institutii.institutie_id |
| `rol` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

### proiecte_obligatii.csv

| Coloană | Definiție |
|---|---|
| `obligatie_id` | Identificator / cheie de legătură |
| `institutie_id` | Cheie către institutii.institutie_id |
| `obligatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `temei_legal` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `termen` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `stadiu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### reforme_anuntate.csv

| Coloană | Definiție |
|---|---|
| `reforma_id` | Cheie către reforme_anuntate.reforma_id |
| `titlu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_anuntului` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `initiator` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `obiectiv` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `economie_anuntata` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `economie_bugetata` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `economie_realizata` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `stadiu` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### reforme_evenimente.csv

| Coloană | Definiție |
|---|---|
| `eveniment_id` | Identificator / cheie de legătură |
| `reforma_id` | Cheie către reforme_anuntate.reforma_id |
| `data_eveniment` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_eveniment` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `descriere` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `act_normativ` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### afirmatii_publice.csv

| Coloană | Definiție |
|---|---|
| `afirmatie_id` | Identificator / cheie de legătură |
| `reforma_id` | Cheie către reforme_anuntate.reforma_id |
| `text_afirmatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `autor_institutional` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_afirmatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `tip_afirmatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `status_verificare` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `explicatie` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `sursa_id` | Cheie către surse.sursa_id |

### cereri_544.csv

| Coloană | Definiție |
|---|---|
| `cerere_id` | Identificator / cheie de legătură |
| `destinatar` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `subiect` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_trimiterii` | Data efectivă ISO 8601, necompletată dacă nu e documentată |
| `nr_inregistrare` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `termen_legal` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `data_raspuns` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |
| `status` | Valoare controlată; vezi validatorul |
| `observatii` | Câmp descriptiv sau măsură; sursa și unitatea se documentează explicit |

## Reguli

- Presa produce ipoteze; documentele primare susțin afirmații.
- Fără scoruri publice, calificative sau persoane nominalizate; drept la replică 15 zile lucrătoare.
- Tabelele se verifică vizual; anunțat ≠ bugetat ≠ realizat.
- Companiile de stat și ONG-urile sunt etape separate.
- `trimisa_confirmata_de_solicitant` reflectă confirmarea expeditorului, nu dovada înregistrării. Nu se completează retroactiv date necunoscute.
- Generator: `python tools/site/audit.py`; validator: `python tools/audit/validate.py`.
