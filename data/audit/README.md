# Dicționar de date – Auditul instituțiilor publice v0.5

**Stadiu:** metodologie în consultare, fără fișe instituționale. Toate exemplele de mai jos sunt fictive, nu înregistrări.

Câmpurile `*_id` sunt identificatori stabili, de tip text, cu excepția referințelor explicate mai jos. Un câmp gol reprezintă informație necunoscută, nu valoarea zero. Valorile bănești sunt stocate numeric fără separator de mii, cu unitatea explicită. Valorile de tip „aprobat”, „bugetat” și „executat” nu se confundă.

## institutii.csv

Cheie primară: `institutie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `institutie_id` | Identificator unic al rândului din institutii | text stabil | INS-001 |
| `denumire` | Denumirea oficială completă a instituției sau indicatorului | text | Direcția X |
| `cui` | Cod unic de identificare fiscală, păstrat ca text | cifre ca text | 12345678 |
| `tip_institutie` | Clasa juridico-administrativă a entității | minister / agenție / direcție / altul | agenție |
| `nivel_ordonator` | Poziția în ierarhia bugetară | principal / secundar / terțiar / neaplicabil | terțiar |
| `autoritate_parinte_id` | Instituția superioară în ierarhia administrativă; referință internă | institutie_id | INST-001 |
| `personalitate_juridica` | Dacă entitatea are personalitate juridică | da / nu / necunoscut | da |
| `statut` | Starea juridică verificată la data evidenței | activa / reorganizata / desfiintata / exceptata / necunoscut | activa |
| `data_infiintarii` | Data intrării în existență juridică | AAAA-LL-ZZ | 2024-01-01 |
| `data_incetarii` | Data încetării personalității juridice, dacă există | AAAA-LL-ZZ | 2025-12-31 |
| `temei_legal_url` | URL direct către actul normativ de înființare sau funcționare | URL https | https://legislatie.just.ro/ |
| `garantii_juridice` | Garanții de independență sau mandat protejat prevăzute de lege | text cu trimitere legală | independență funcțională |
| `restrictii_reorganizare` | Limite legale aplicabile reorganizării | text cu articol | aviz obligatoriu |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## relatii_institutii.csv

Cheie primară: `relatie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `relatie_id` | Identificator unic al rândului din relatii_institutii | text stabil | REL-001 |
| `institutie_sursa_id` | Cheie externă către surse | ID existent | SUR-001 |
| `institutie_destinatie_id` | Cheie externă către institutii | ID existent | INS-001 |
| `tip_relatie` | Relația dintre două instituții | subordonare / coordonare / absorbție / transfer | subordonare |
| `data_inceput` | Prima dată de aplicare a relației | AAAA-LL-ZZ | 2025-01-01 |
| `data_sfarsit` | Ultima dată de aplicare a relației | AAAA-LL-ZZ | 2025-12-31 |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## indicatori.csv

Cheie primară: `indicator_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `indicator_id` | Identificator unic al rândului din indicatori | text stabil | IND-001 |
| `institutie_id` | Cheie externă către institutii | ID existent | INS-001 |
| `indicator_cod` | Cod stabil al indicatorului, definit în indicatori_dictionar | cheie | POSTURI_OCUPATE |
| `an` | An calendaristic sau bugetar raportat | AAAA | 2025 |
| `perioada` | Intervalul exact acoperit de valoare | text ISO / trimestru | 2025-Q4 |
| `tip_valoare` | Natura cifrei: nu se confundă aprobat cu executat | aprobat / bugetat / executat / estimat / anuntat | executat |
| `valoare` | Valoarea numerică fără separator de mii | număr zecimal | 1250.50 |
| `unitate` | Unitatea măsurii, coerentă cu dicționarul | lei / mii_lei / posturi / persoane / procent | posturi |
| `nivel_raportare` | Dacă cifra aparține instituției sau unui total consolidat | propriu / consolidat | propriu |
| `perimetru_consolidare_id` | Instituția rădăcină a consolidării, când este aplicabil | institutie_id | INST-001 |
| `perimetru` | Descrierea entităților incluse și excluse | text | aparat central fără subordonate |
| `document_referinta` | Identificatorul actului, raportului sau anexei | text | Raport execuție 2025 |
| `pagina_sau_tabel` | Pagina tipărită și tabelul din document | text | p. 12, tabel 4 |
| `data_verificarii` | Data verificării valorii față de sursă | AAAA-LL-ZZ | 2026-11-06 |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |
| `verificator_cod` | Cod pseudonim al evaluatorului | text | EV-01 |

## indicatori_dictionar.csv

Cheie primară: `indicator_cod`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `indicator_cod` | Identificator unic al rândului din indicatori_dictionar | text stabil | IND-001 |
| `denumire` | Denumirea oficială completă a instituției sau indicatorului | text | Direcția X |
| `definitie` | Definiție operațională, cu includeri și excluderi | text | posturi ocupate la 31 decembrie |
| `unitate` | Unitatea măsurii, coerentă cu dicționarul | lei / mii_lei / posturi / persoane / procent | posturi |
| `granularitate` | Nivel temporal și instituțional al observației | text | instituție-an |
| `metoda_calcul` | Regula de agregare și deduplicare | text | sumă posturi proprii |

## surse.csv

Cheie primară: `sursa_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `sursa_id` | Identificator unic al rândului din surse | text stabil | SUR-001 |
| `titlu` | Titlul exact al sursei, reformei sau scenariului | text | Nota de fundamentare |
| `emitent` | Instituția care a emis documentul | text | Guvernul României |
| `url` | Adresa originală a documentului | URL https | https://gov.ro/ |
| `data_document` | Data emiterii documentului | AAAA-LL-ZZ | 2025-12-30 |
| `data_accesarii` | Data accesării sau descărcării sursei | AAAA-LL-ZZ | 2026-11-06 |
| `tip_sursa` | Clasa sursei și gradul de primaritate | act_normativ / raport / declaratie / presa / altul | raport |
| `metoda_extragere` | Procedura efectiv folosită pentru citirea sursei | text_structurat / paragrafe_tabel / randare_vizuala / OCR / verificare_incrucisata | randare_vizuala |
| `verificare_tabel` | Stadiul verificării structurii unui tabel | neverificat / verificat_vizual / reconciliat | verificat_vizual |
| `offset_pagina` | Diferența pagină PDF minus pagină tipărită | număr întreg | 3 |
| `hash_sha256` | Hash-ul fișierului original dacă a fost calculat | 64 caractere hex | a repetat de 64 ori |
| `observatii` | Precizări factuale, incertitudini și limite | text | Număr de înregistrare încă necunoscut |

## atributii.csv

Cheie primară: `atributie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `atributie_id` | Identificator unic al rândului din atributii | text stabil | ATR-001 |
| `institutie_id` | Cheie externă către institutii | ID existent | INS-001 |
| `functie_cod` | Codul funcției controlate din taxonomia atribuțiilor | text | CONTROL_ALIMENTE |
| `descriere` | Descrierea atribuției ori a evenimentului | text | Verificarea etichetării |
| `obiect` | Obiectul material al controlului, vocabular controlat | alimente / energie / comunicatii / servicii_financiare / mediu / altul | alimente |
| `competenta_teritoriala` | Aria juridică a competenței | nationala / regionala / judeteana / locala | judeteana |
| `beneficiari_entitati_reglementate` | Categoriile de operatori sau beneficiari afectați | text controlat | operatori alimentari |
| `temei_legal` | Act și articol pentru atribuție sau obligație | text cu articol | Legea X art. 5 |
| `tip_competenta` | Tipul mandatului conferit de lege | generala / speciala | speciala |
| `tip_intersectie` | Etichetă preliminară, nu dovadă a unei perechi | juridica / generala_speciala / operationala / cooperare_reglementata / perceputa | operationala |
| `cofog_cod` | Codul clasificării funcțiilor guvernamentale | cod COFOG | 04 |
| `regim_juridic` | Reguli speciale aplicabile exercitării atribuției | text | competență exclusivă |
| `valabil_de_la` | Data de început a versiunii atribuției | AAAA-LL-ZZ | 2025-01-01 |
| `valabil_pana_la` | Data încetării versiunii atribuției | AAAA-LL-ZZ | 2025-12-31 |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## audit_corectii.csv

Cheie primară: `corectie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `corectie_id` | Identificator unic al rândului din audit_corectii | text stabil | AUD-001 |
| `tabel` | Tabelul în care se află valoarea contestată | nume CSV fără extensie | indicatori |
| `tinta_id` | Identificatorul rândului corectat din tabelul indicat | cheie internă | IND-001 |
| `camp` | Numele coloanei corectate | nume coloană | valoare |
| `valoare_anterioara` | Conținutul înaintea corecției, păstrat textual | text | 100 |
| `valoare_noua` | Conținutul după corecție, păstrat textual | text | 120 |
| `motiv` | Explicația documentată a sesizării sau corecției | text | eroare de transcriere |
| `data_sesizarii` | Data primirii sesizării | AAAA-LL-ZZ | 2026-11-06 |
| `data_corectie` | Data aplicării corecției | AAAA-LL-ZZ | 2026-11-07 |
| `status` | Stadiul fluxului, valori permise diferite pe tabel | vezi secțiunea valori permise | sesizata |
| `decizie_motivata` | Raționamentul deciziei de acceptare/refuz | text | corecție susținută de act |
| `dovada_url` | Link către dovada justificativă | URL https | https://example.org/ |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |
| `verificator_cod` | Cod pseudonim al evaluatorului | text | EV-01 |

## scenarii_reorganizare.csv

Cheie primară: `scenariu_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `scenariu_id` | Identificator unic al rândului din scenarii_reorganizare | text stabil | SCE-001 |
| `titlu` | Titlul exact al sursei, reformei sau scenariului | text | Nota de fundamentare |
| `tip_scenariu` | Mecanismul intervenției administrative | coordonare / digitalizare / comasare / mentinere | coordonare |
| `varianta` | Ipoteza de incertitudine financiară | pesimist / baza / optimist | baza |
| `ipoteze` | Presupuneri cuantificate, distincte de fapte | text | cost constant 2025 |
| `cost_tranzitie_estimat` | Cheltuială unică estimată de implementare | lei | 500000 |
| `costuri_transferate` | Cheltuieli mutate la alt ordonator, nu economii | lei/an | 200000 |
| `economie_bruta` | Reducerea totală înainte de costuri | lei/an | 1000000 |
| `economie_neta` | Reducere după costuri și transferuri | lei/an | 300000 |
| `economie_estimata` | Estimarea în ipoteza selectată | lei/an | 300000 |
| `orizont_ani` | Durata de analiză a efectului | ani întregi | 5 |
| `stadiu` | Starea reformei sau scenariului | vezi valori permise | anuntata |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## scenariu_institutii.csv

Cheie primară: `legatura_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `legatura_id` | Identificator unic al rândului din scenariu_institutii | text stabil | SCE-001 |
| `scenariu_id` | Cheie externă către scenarii_reorganizare | ID existent | SCE-001 |
| `institutie_id` | Cheie externă către institutii | ID existent | INS-001 |
| `rol` | Participarea instituției la scenariu | absorbanta / absorbita / coordonator / comparatie | absorbanta |

## proiecte_obligatii.csv

Cheie primară: `obligatie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `obligatie_id` | Identificator unic al rândului din proiecte_obligatii | text stabil | PRO-001 |
| `institutie_id` | Cheie externă către institutii | ID existent | INS-001 |
| `obligatie` | Acțiunea cerută prin lege sau proiect | text | raportare anuală |
| `temei_legal` | Act și articol pentru atribuție sau obligație | text cu articol | Legea X art. 5 |
| `termen` | Data scadentă a obligației | AAAA-LL-ZZ | 2027-01-31 |
| `stadiu` | Starea reformei sau scenariului | vezi valori permise | anuntata |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## reforme_anuntate.csv

Cheie primară: `reforma_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `reforma_id` | Identificator unic al rândului din reforme_anuntate | text stabil | REF-001 |
| `titlu` | Titlul exact al sursei, reformei sau scenariului | text | Nota de fundamentare |
| `data_anuntului` | Data publică a promisiunii de reformă | AAAA-LL-ZZ | 2025-12-30 |
| `initiator` | Autoritatea care a inițiat reforma | text | MADR |
| `obiectiv` | Rezultatul administrativ urmărit | text | reducere costuri |
| `tip_economie` | Natura economiei, pentru a evita amestecarea titlurilor | personal / bunuri_servicii / total / alta | personal |
| `orizont_ani` | Durata de analiză a efectului | ani întregi | 5 |
| `baza_comparatie` | Perioada și perimetrul folosite la comparație | text | execuție 2025 |
| `data_scadenta` | Termenul promis pentru rezultat | AAAA-LL-ZZ | 2026-12-31 |
| `grad_incredere` | Nivelul dovezilor disponibile | scazut / mediu / ridicat / neanalizat | neanalizat |
| `economie_anuntata` | Valoarea declarată public, fără a o trata ca realizată | lei/an | 100000 |
| `economie_bugetata` | Reducere inclusă într-un buget aprobat | lei/an | 80000 |
| `economie_realizata` | Reducere demonstrată prin execuție reconciliată | lei/an | 75000 |
| `stadiu` | Starea reformei sau scenariului | vezi valori permise | anuntata |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## reforme_evenimente.csv

Cheie primară: `eveniment_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `eveniment_id` | Identificator unic al rândului din reforme_evenimente | text stabil | REF-001 |
| `reforma_id` | Cheie externă către reforme_anuntate | ID existent | REF-001 |
| `data_eveniment` | Data actului sau etapei reformei | AAAA-LL-ZZ | 2025-12-30 |
| `tip_eveniment` | Categoria evenimentului din cronologia reformei | anunt / modificare / adoptare / implementare / suspendare | adoptare |
| `descriere` | Descrierea atribuției ori a evenimentului | text | Verificarea etichetării |
| `act_normativ` | Identificatorul actului relevant | text | OUG 92/2025 |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## afirmatii_publice.csv

Cheie primară: `afirmatie_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `afirmatie_id` | Identificator unic al rândului din afirmatii_publice | text stabil | AFI-001 |
| `reforma_id` | Cheie externă către reforme_anuntate | ID existent | REF-001 |
| `text_afirmatie` | Afirmația exactă de verificat | text | Au fost eliminate 73 de instituții |
| `autor_institutional` | Autorul afirmației sau instituția emitentă | text | MADR |
| `data_afirmatie` | Data publicării afirmației | AAAA-LL-ZZ | 2026-02-11 |
| `tip_afirmatie` | Domeniul verificării | financiar / personal / juridic / operational | financiar |
| `status_verificare` | Verdictul susținut de dovezi | neanalizata / confirmata / partial_sustinuta / infirmata / neconcludenta | neanalizata |
| `explicatie` | Motivarea verificării și limitele ei | text | necesită execuția bugetară |
| `sursa_id` | Cheie externă către surse | ID existent | SUR-001 |

## cereri_544.csv

Cheie primară: `cerere_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `cerere_id` | Identificator unic al rândului din cereri_544 | text stabil | CER-001 |
| `destinatar` | Instituția căreia i-a fost adresată cererea | text | MADR |
| `subiect` | Obiectul precis al cererii 544 | text | Reorganizare MADR |
| `data_trimiterii` | Data confirmată a depunerii/trimiterii | AAAA-LL-ZZ | 2026-11-06 |
| `nr_inregistrare` | Numărul oficial primit de la destinatar | text | 123/2026 |
| `termen_legal` | Pragul calendaristic de urmărire de 10 zile | AAAA-LL-ZZ | 2026-11-16 |
| `data_raspuns` | Data recepției răspunsului | AAAA-LL-ZZ | 2026-11-20 |
| `status` | Stadiul fluxului, valori permise diferite pe tabel | vezi secțiunea valori permise | sesizata |
| `observatii` | Precizări factuale, incertitudini și limite | text | Număr de înregistrare încă necunoscut |

## suprapuneri.csv

Cheie primară: `suprapunere_id`.

| Coloană | Definiție | Format / valori | Exemplu fictiv |
|---|---|---|---|
| `suprapunere_id` | Identificator unic al rândului din suprapuneri | text stabil | SUP-001 |
| `atributie_a_id` | Cheie externă către atributii | ID existent | ATR-001 |
| `atributie_b_id` | Cheie externă către atributii | ID existent | ATR-001 |
| `categorie` | Categoria verificată a relației dintre două atribuții | juridica / generala_speciala / operationala / cooperare_reglementata / perceputa | generala_speciala |
| `dovada_sursa_id` | Cheie externă către surse | ID existent | SUR-001 |
| `status` | Stadiul fluxului, valori permise diferite pe tabel | vezi secțiunea valori permise | sesizata |

## Reguli de calitate

- `sursa_id` este obligatoriu pentru orice rând care are această coloană; `dovada_sursa_id` este obligatoriu pentru suprapuneri.
- Înregistrările fără dovezi nu sunt acceptate; relațiile orfane sunt erori.
- `indicator_cod` trebuie să existe în dicționar; `audit_corectii.tinta_id` trebuie să existe în tabelul indicat.
- Tabelele financiare se verifică vizual pe randarea documentului, iar metoda se păstrează în `surse.csv`.
- Statutul instituției nu este un scor; calificările publice nu sunt permise.
- Jurnalul 544 conține trimiteri confirmate de solicitant, fără numere de înregistrare inventate; 2026-11-16 și 2026-12-06 sunt praguri orientative de urmărire, nu dovezi ale datei înregistrării.
- Componentele companii de stat și ONG-uri sunt etape ulterioare.

## Comenzi

`python tools/audit/validate.py` · `python -m unittest discover -s tests` · `python tools/site/audit.py`.
