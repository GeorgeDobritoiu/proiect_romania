# Metodologia tehnică v0.5 – Auditul instituțiilor publice

6 noiembrie 2026

**Pe scurt.** Verificăm trei lucruri: cine face ce în administrația publică, unde se întâlnesc atribuțiile instituțiilor și dacă reformele anunțate au produs rezultatele promise. Folosim doar documente oficiale ca dovadă; presa ne dă doar ipoteze. Fiecare cifră trebuie să aibă sursă și pagină, fiecare fișă trebuie să treacă prin verificare în doi și prin dreptul la replică al instituției, iar economiile se calculează net, nu din anunțuri. Nu publicăm scoruri, clasamente sau nume de persoane.

> **Stadiu:** metodologie în consultare, nu un sistem de audit deja aplicat. Nu există încă fișe de instituții publicate. Unde scrie „vom”, procedura este planificată; secțiunea 10 arată ce este deja automatizat și ce nu.

**Cuprins:** 1. Ce verificăm · 2. Universul analizei · 3. Surse și dovezi · 4. Suprapuneri · 5. Bani și personal · 6. Reforme și economii · 7. Verificări juridice · 8. Pilotul propus · 9. Drumul unei fișe · 10. Date și automatizări · 11. Limite și versiuni

## 1. Ce întrebări verificăm și ce nu facem

Proiectul are trei componente, fiecare cu propria întrebare:

| Componentă | Întrebarea | Ce produce |
| --- | --- | --- |
| Registrul instituțiilor | Cine există, ce mandat legal are, cât costă și câți oameni lucrează? | Fișe factuale, cu sursă pentru fiecare cifră |
| Analiza atribuțiilor | Fac două instituții același lucru, în lege sau în practică? | Perechi de atribuții analizate, cu dovadă și grad de încredere |
| Reformele promise | Ce s-a anunțat, ce s-a adoptat, ce s-a bugetat și ce s-a realizat? | Cronologia fiecărei reforme și comparația cifrelor |

**Ce nu facem:**

- Nu publicăm scoruri sau clasamente de instituții.
- Nu numim persoane și nu folosim calificative („inutilă”, „parazitară”).
- Nu recomandăm desființări pe baza unei singure surse sau a unui articol de presă.
- Nu prezentăm estimări drept economii realizate.
- Nu analizăm în această etapă companiile de stat și ONG-urile; au alt regim juridic și alte surse de date.

## 2. Universul analizei

**Intră:** instituțiile publice finanțate din bugetul de stat sau din bugetele locale, începând cu administrația centrală: ministere, agenții, autorități, instituții subordonate și servicii deconcentrate.

**Unitatea de evidență** este entitatea sau structura administrativă identificabilă juridic și funcțional. Calitatea de ordonator de credite nu coincide întotdeauna cu instituția, așa că o notăm separat, alături de:

- nivelul de ordonator, dacă există: principal (ex. un minister), secundar sau terțiar;
- instituția-părinte și istoricul subordonării (cu datele de început și sfârșit);
- dacă are personalitate juridică;
- actul de înființare și rangul lui (lege, ordonanță sau hotărâre de Guvern).

Așa nu pierdem din analiză structurile fără personalitate juridică sau fără buget propriu. Fiecare entitate primește un identificator intern stabil; CUI-ul ajută la identificare, dar nu este cheia registrului, pentru că instituțiile se reorganizează și își schimbă numele.

**Instituțiile cu mandat protejat** (prevăzut de Constituție, de dreptul UE sau de tratate internaționale) rămân în registru. Pentru ele notăm garanțiile care trebuie păstrate în orice scenariu (independență, buget separat, numire protejată). Mandatul protejat nu înseamnă automat că instituția nu poate fi reorganizată: în UE există autorități de reglementare care acoperă mai multe sectoare. Înseamnă că orice scenariu trebuie să păstreze acele garanții.

**Exclus în această etapă:** companiile cu capital de stat și institutele organizate ca societăți comerciale (guvernanță corporativă, alte date) și ONG-urile, inclusiv cele finanțate din bani publici (alt regim juridic; pentru ele analizăm doar finanțările primite, într-o etapă ulterioară).

## 3. Surse și dovezi

**Regula de bază:** presa este o ipoteză, documentul oficial este dovadă. O afirmație din presă nu poate susține singură nicio constatare publicată.

| Sursă | Ce oferă | Limită |
| --- | --- | --- |
| Monitorul Oficial, legislatie.just.ro | Actul de înființare, atribuțiile, modificările | Textul consolidat trebuie citit la data analizată |
| Ministerul Finanțelor – transparență bugetară | Bugete și execuții pe entitate | Necesită reconciliere pe instituție și perioadă |
| Note de fundamentare (gov.ro) | Intenția și impactul declarat al unui act | Sunt estimări, nu rezultate |
| Organigrame, state de funcții, rapoarte anuale | Posturi, structură, activitate | Publicate inegal |
| Răspunsuri la cereri pe Legea 544/2001 | Date care nu sunt publice altfel | Depind de răspunsul instituției |
| Rapoarte ale Curții de Conturi, studii oficiale (ex. CES), evaluări internaționale | Constatări independente | Au propriul perimetru și propriile limite |
| Presă, agregatoare independente | Ipoteze de verificat | Nu sunt dovadă |

Pentru fiecare sursă păstrăm: emitentul, data documentului, data accesării, metoda de extragere și amprenta digitală (SHA-256) a fișierului, ca să putem dovedi ulterior ce document am citit.

**Tabelele din documente oficiale se citesc pe pagina afișată**, nu doar din textul extras automat: extragerea automată poate muta valorile pe rândul greșit. Notăm și decalajul dintre pagina tipărită și cea din PDF.

**Ce poate dovedi o sursă și ce nu:**

- O sursă trebuie să demonstreze exact afirmația pentru care o folosim, nu doar să fie oficială.
- Un act normativ dovedește că o atribuție există în lege, nu că este exercitată de două ori în practică.
- O declarație a unei instituții despre economii este o afirmație de verificat, nu dovada execuției bugetare.
- Un studiu oficial (CES, Curtea de Conturi, o evaluare internațională) se citează cu propriile limite metodologice.
- Lipsa unui document sau a unui răspuns nu dovedește, singură, ineficiența sau încălcarea legii.

**Trasabilitate:** orice concluzie dintr-o fișă publică se poate urmări până la indicator, sursă, pagină, metoda de extragere și eventualele corecții. Nu este suficient ca documentul să apară în bibliografie.

## 4. Cum stabilim dacă există suprapunere

Două instituții care lucrează în același domeniu nu sunt automat redundante. Separarea dintre cine reglementează, cine autorizează, cine controlează și cine soluționează contestațiile poate fi voită și necesară.

**Pasul 1 – descriem fiecare atribuție** din actul normativ prin:

- tipul funcției: reglementare, autorizare, control/inspecție, sancționare, soluționarea contestațiilor, serviciu direct, finanțare, suport intern;
- obiectul (domeniul), dintr-un vocabular controlat, nu text liber;
- competența teritorială (națională, județeană, locală);
- cine este vizat (beneficiari sau entități controlate);
- regimul juridic și perioada de valabilitate.

**Pasul 2 – comparăm perechi de atribuții.** O pereche devine candidat la suprapunere doar dacă tipul funcției, obiectul, teritoriul și cei vizați coincid substanțial.

**Pasul 3 – încadrăm perechea într-una din cinci categorii:**

| Categorie | Ce înseamnă | Dovada necesară |
| --- | --- | --- |
| Suprapunere juridică | Două acte normative dau aceeași atribuție specifică | Textul celor două acte |
| Competență generală – specială | O instituție are un mandat general (ex. protecția consumatorului), alta o competență sectorială asupra acelorași operatori | Actele normative și regulile de prioritate dintre ele |
| Suprapunere operațională | În practică, același operator este controlat pe același aspect de două instituții | Registre de controale sau hotărâri judecătorești |
| Cooperare reglementată | Competențele se întâlnesc, dar există protocol de cooperare | Protocolul și date despre aplicarea lui |
| Suprapunere percepută | Operatorii relatează dublu control, fără confirmare independentă | Relatări, studii calitative |

O pereche poate aparține mai multor categorii. **Categoria descrie natura relației, nu un verdict.** Separat, fiecare pereche are un statut al verificării: suspectată, în verificare, confirmată, infirmată sau neconcludentă. Statutul „confirmată” se acordă doar când o sursă oficială primară demonstrează exact acea suprapunere, niciodată pe baza presei. O suprapunere operațională nu se poate vedea din lege: necesită date despre controalele efectuate.

## 5. Date financiare și de personal

**Fiecare cifră este un rând separat**, cu: instituția, indicatorul, anul, valoarea, unitatea, tipul valorii și sursa (cu pagina sau tabelul). Astfel bugetul poate avea o sursă, iar personalul alta, și putem urmări cinci ani.

**Tipul valorii** se notează mereu: aprobat, executat, estimat sau anunțat. Un buget aprobat și unul executat nu se compară între ele.

**Reguli de consolidare.** Bugetul unei instituții centrale poate include cheltuieli ale structurilor din subordine. Dacă am aduna automat aceste valori, am număra aceiași bani de două ori. De aceea:

1. Păstrăm cheltuielile proprii ale tuturor entităților, inclusiv ale ministerelor.
2. Nu adunăm bugetul consolidat al unui minister cu bugetele instituțiilor din subordine.
3. Eliminăm doar fluxurile interne identificate și reconciliate (ex. transferurile de la minister la subordonat), nu automat toate transferurile.
4. Documentăm perimetrul fiecărei sume. Diferențele din reconciliere se explică; nu se „închid” prin ajustări inventate.

**Personalul:** separăm posturile aprobate, ocupate și vacante și funcțiile de conducere de cele de execuție. Nu există o sursă publică unică a personalului pe fiecare instituție; folosim organigrame, state de funcții, rapoarte și cereri pe Legea 544.

**Comparații între instituții diferite** se fac doar pentru indicatori de structură (ponderea cheltuielilor de suport, proporția funcțiilor de conducere, posturile vacante, execuția față de buget) și doar ca semnal de verificat, nu ca dovadă de ineficiență. Indicatorii de rezultat (controale, dosare, beneficiari) se compară doar între instituții cu aceeași funcție. Un indicator de semnal nu apare singur într-o fișă publică: îl însoțim de explicația instituției sau de mențiunea „explicație solicitată, fără răspuns”.

## 6. Reformele promise și calculul economiilor

**O reformă este un singur fir cu mai multe evenimente:** anunțul, actul normativ, modificările din Parlament, normele de aplicare, implementarea și execuția bugetară de după. Aceeași reformă reluată nu se numără de două ori.

Pentru fiecare economie păstrăm separat **suma anunțată, suma bugetată și suma realizată**, cu sursa fiecăreia, tipul economiei, orizontul, baza de comparație și un grad de încredere.

**Cum calculăm economiile.** Folosim două calcule distincte:

```
economie operațională netă (pe an) = costuri recurente evitate
                                   − costuri recurente suplimentare

efect bugetar cumulat (n ani) = suma economiilor operaționale nete pe fiecare an
                              − costurile de tranziție
```

- **Costurile recurente suplimentare** includ costurile mutate la instituția care preia activitatea (ex. salarii mai mari pe noile funcții). Costurile transferate se reconciliază între instituții, ca să nu apară drept economie, și nu se scad de două ori.
- **Costurile de tranziție** sunt cele de o singură dată: IT, mutări de sedii, încheierea contractelor, compensații, litigii.
- **Un post vacant desființat nu este automat o economie realizată.** Poate reduce bugetul aprobat, dar economia efectivă se demonstrează prin cheltuieli.
- Transformarea unei funcții (ex. din conducere în execuție) produce economie doar prin diferența de salarizare efectivă.
- Precizăm perioada de referință și dacă valorile sunt nominale sau ajustate cu inflația.
- Prezentăm rezultatul la 1, 3 și 5 ani, în trei variante: pesimistă, de bază și optimistă.
- O estimare dintr-o notă de fundamentare rămâne estimare până o confirmă execuția bugetară.

**Verificăm și dacă statul și-a respectat propriile legi.** Exemplu: art. XXIX din Legea nr. 296/2023 prevede că o instituție își păstrează forma doar dacă are peste 50 de posturi aprobate și ocupate și activități care nu se suprapun cu ale altor instituții, cu excepții și derogări. Pentru fiecare instituție vizată notăm un statut factual: în domeniul de aplicare, exceptată, derogare identificată, reorganizată, în curs de verificare sau date insuficiente. Nu scriem „a încălcat legea” fără a stabili obligația concretă, termenul aplicabil și derogările, în versiunea legii valabilă la acea dată.

## 7. Verificări juridice înainte de orice scenariu de reorganizare

Niciun scenariu (comasare, transfer de activitate, coordonare, punct unic digital) nu se publică fără aceste verificări:

- [ ] **Rangul actului de înființare:** lege (necesită Parlamentul) sau hotărâre de Guvern.
- [ ] **Garanții cerute de dreptul UE sau de Constituție:** independență decizională și bugetară, proceduri de numire, separarea investigației de decizie.
- [ ] **Proiecte cu finanțare UE sau PNRR în derulare:** schimbarea beneficiarului poate duce la corecții financiare.
- [ ] **Regimul personalului:** reguli diferite pentru funcționari publici și personal contractual; costurile de tranziție depind de acesta.
- [ ] **Patrimoniu, contracte în derulare, litigii.**
- [ ] **Accesul cetățenilor la serviciu** după reorganizare.

Orice scenariu de reorganizare se compară cu alternative mai puțin intruzive: interoperabilitate și schimb de date, protocoale de cooperare, controale comune, simplificarea procedurilor. Alternativele se evaluează cu aceleași reguli de cost și risc; nici ele nu sunt automat mai ieftine.

## 8. Pilotul propus

Propunem testarea metodologiei pe aproximativ 12 instituții, în trei grupe. Componența și criteriile de selecție sunt încă supuse validării și vor fi publicate înainte de începerea pilotului. Fiecare grupă răspunde altei întrebări, deci nu facem un clasament comun.

| Grupă | Întrebarea | Punct de plecare oficial |
| --- | --- | --- |
| Protecția consumatorului și control | Cum se coordonează controalele? Există dublu control în practică? | Studiul CES din februarie 2026 |
| Agricultură | S-au realizat economiile anunțate la reorganizarea din 2024–2026? | OUG 85/2024, OUG 92/2025 și notele lor de fundamentare |
| Agențiile din jurul Guvernului | Au fost aplicate recomandările din 2010? | Banca Mondială, *Romania – Functional Review: Center of Government*, raport 74282 |

**Reguli de selecție:**

- Regula de selecție, datele de intrare și data extragerii se publică **înainte** de a vedea rezultatele. Orice abatere se motivează în jurnal.
- Grupele sunt alese pentru că există o evaluare oficială anterioară (studiu, notă de fundamentare sau recomandare internațională), nu după percepția publică.
- Fiecare grupă are cel puțin un **caz-martor**: o instituție la care nu bănuim probleme, ca să vedem dacă metoda produce alarme false.
- Publicăm și lista instituțiilor excluse, cu motivul.
- Evaluarea independentă în doi este o condiție înainte de publicarea oricărei fișe. După primele evaluări publicăm indicatorul de acord dintre evaluatori și modul în care se rezolvă divergențele; dacă acordul este slab, rubrica se revizuiește înainte de restul pilotului.

## 9. Drumul unei fișe până la publicare

1. **Colectare:** fiecare cifră și fiecare atribuție intră în registru cu sursa ei; tabelele se verifică pe pagina afișată.
2. **Cereri de informații:** ce nu e public se cere pe Legea 544/2001. Notăm data, numărul de înregistrare, termenul și răspunsul în [jurnalul cererilor](https://proiectromania.ro/audit/cereri-544). Lipsa unui răspuns nu este dovadă de ineficiență; o consemnăm separat, ca problemă de transparență.
3. **Evaluare dublă:** doi evaluatori, independent; dezacordurile se notează.
4. **Verificarea citatelor:** o a doua persoană verifică fiecare citat și fiecare număr pe documentul original.
5. **Drept la replică:** fișa se trimite instituției, iar cele 15 zile lucrătoare pentru răspuns se calculează de la transmiterea documentată. Păstrăm dovada transmiterii, răspunsul și explicația modificărilor făcute; lipsa răspunsului se consemnează factual. Răspunsul se publică integral alături de fișă, cu excepția datelor personale sau confidențiale.
6. **Aprobare editorială:** publicarea o aprobă explicit inițiatorul proiectului.
7. **Corecții:** orice sesizare se înregistrează cu data, motivul, valoarea veche și cea nouă și decizia motivată; corecțiile rămân vizibile în jurnalul de modificări.

Evaluatorii apar public prin coduri; identitățile și declarațiile de conflict de interese sunt păstrate într-un registru intern.

## 10. Date și automatizări

Schemele de date sunt pregătite; seturile verificate vor fi publicate pe măsură ce trec prin fluxul de la secțiunea 9. Separăm registrul intern de setul public: înainte de publicare eliminăm datele personale și informațiile protejate și verificăm dreptul de reutilizare. Nu publicăm automat toate documentele primite prin Legea 544; unele pot necesita anonimizare.

Datele publice vor fi fișiere CSV, împreună cu un dicționar care explică fiecare coloană (definiție, format, valori permise, exemplu).

| Fișier | Ce conține |
| --- | --- |
| institutii | Identitatea, nivelul de ordonator, actul de înființare, garanțiile juridice |
| relatii_institutii | Subordonarea și istoricul ei |
| indicatori, indicatori_dictionar | Cifrele anuale (o cifră pe rând) și definiția fiecărui indicator |
| atributii, suprapuneri | Atribuțiile și perechile analizate, cu categoria și dovada |
| surse | Fiecare document folosit, cu metoda de extragere și amprenta digitală |
| reforme_anuntate, reforme_evenimente | Reformele și cronologia lor; sumele anunțate, bugetate și realizate |
| scenarii_reorganizare, scenariu_institutii | Scenariile analizate și instituțiile implicate |
| proiecte_obligatii | Proiecte UE/PNRR, contracte și obligații care limitează o reorganizare |
| afirmatii_publice | Afirmații publice verificate și statutul lor |
| cereri_544 | Jurnalul cererilor de informații |
| audit_corectii | Toate corecțiile, cu motivul |

**Ce verifică automat un program și ce rămâne verificare umană:**

| Tip de verificare | Exemple | Stadiu |
| --- | --- | --- |
| Automată (program de validare) | Fiecare cifră are sursă; formate corecte; statusuri din lista permisă; nicio trimitere către o instituție sau sursă inexistentă | Implementată pentru schemele de date |
| Editorială, obligatorie | Sursa demonstrează exact afirmația; citatul și pagina sunt corecte; sensul juridic și financiar | Planificată; se aplică la fiecare fișă |
| Procedurală | Evaluare în doi, drept la replică, aprobare editorială | Planificată |

Un câmp de sursă completat și validat de program nu dovedește că documentul susține concluzia; asta rămâne responsabilitatea evaluatorilor. Un câmp gol înseamnă „necunoscut”, nu zero.

## 11. Limite cunoscute și versiuni

**Limite:**

- Nu există o sursă publică unică a personalului pe fiecare instituție; datele vor fi incomplete până la răspunsurile la cereri.
- Suprapunerea operațională nu se poate stabili din lege; fără registrele de controale rămâne nedeterminată.
- Evaluarea economiilor recurente necesită date de execuție comparabile; un an complet de după reformă este preferabil, dar nu întotdeauna suficient.
- Pilotul acoperă câteva grupe de instituții; concluziile lui nu se generalizează la toată administrația.

**Controlul versiunilor:** fiecare ediție a metodologiei și a fiecărei fișe precizează data, modificările, sursele noi, erorile corectate și eventualele concluzii retrase. O fișă publicată nu se rescrie fără urmă editorială.

**Versiuni:**

| Versiune | Data | Ce s-a schimbat |
| --- | --- | --- |
| v0.5 | 6 noiembrie 2026 | Trei componente; cinci categorii de suprapunere; economii anunțate, bugetate și realizate separat; verificarea legii 296/2023; pilot propus pe trei grupe; scheme de date cu validare automată |

Metodologia este în consultare. Un canal dedicat pentru observații este în pregătire; deocamdată nu colectăm observații printr-un formular specializat.