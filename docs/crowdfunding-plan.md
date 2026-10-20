# Crowdfunding Proiect România — propunere de dezvoltare

Stare: concept editorial, 20 octombrie 2026. Nicio funcție de plată activată.

## Scop și model propus

Finanțare prin donații pentru proiecte comunitare concrete. Pentru pilot, propunem
organizații cu identitate verificată și 3–5 campanii cu obiective măsurabile.
Investițiile în capital și împrumuturile nu fac parte din acest concept.
Decizia de a lansa încasări necesită o etapă separată de implementare și aprobare.

## Etapele propuse

1. Director editorial cu linkuri oficiale către beneficiari — implementat.
2. Fișe de campanie: organizație, reprezentant, localitate, scop, buget detaliat,
   țintă, monedă, termen, rezultate, documente și plan de raportare.
3. Pilot: verificare manuală a organizațiilor și a destinației fondurilor;
   alegerea procesatorului și a modelului de transfer direct către beneficiar.
4. Plăți și raportare: confirmări, reconciliere, istoric și rapoarte publice.

## Decizii obligatorii înainte de dezvoltarea plăților

- Operatorul platformei, contractele cu beneficiarii și responsabilitățile fiecăruia.
- Donație flexibilă sau condiționată de atingerea țintei; cum funcționează anularea,
  restituirea, plata către beneficiar și soluționarea disputelor în modelul ales.
- Eligibilitatea beneficiarilor în sistemul procesatorului și verificările cerute.
- Comisioanele procesatorului, eventualele costuri ale platformei și afișarea lor.
- Tratamentul juridic, fiscal și al datelor, validat pentru modelul concret înainte
  de lansare; această notă nu stabilește concluzii juridice sau facilități fiscale.
- Cine aprobă campaniile, răspunde sesizărilor și suspendă campaniile problematice.

## Date și stări

Entități: organizație, campanie, buget, document, donație, eveniment procesator,
transfer, actualizare de proiect, raport final și jurnal de audit.

Stări: ciornă → în verificare → publicată → închisă → raportare → arhivă.
O campanie poate fi suspendată sau anulată, cu motiv documentat.
O ediție nouă are o fișă nouă; nu rescrie istoricul unei campanii închise.

Sumele colectate provin numai din plăți confirmate și reconciliate. Nu se afișează
bare de progres sau donatori fictivi. Donațiile recurente sunt explicite și au
anulare accesibilă. Datele cardului rămân la procesator. Donatorii nu sunt publicați
implicit. Documentele publice exclud date personale și medicale ale beneficiarilor.

## Criterii pentru pilot

- Fiecare campanie are beneficiar, buget, țintă, termen și contact confirmate.
- Plata reușită/eșuată, evenimentele duplicate, restituirea și reconcilierea sunt testate.
- Notificările au consimțământ și destinație corecte.
- Închiderea la termen oprește noi donații conform regulii campaniei.
- Pagina rămâne accesibilă în arhivă cu starea și raportul final.
- Indicatori: donatori, sumă netă confirmată, costuri, țintă atinsă,
  rapoarte publicate la timp, sesizări și restituiri.

## Întreținerea directorului actual

Registru: data/proiecte-de-sustinut.json. Fiecare fișă are sursă, data verificării,
termen (dacă există), stare și data recomandată pentru reverificare.
Apelurile continue nu au o dată fictivă de expirare. La reverificare se confirmă
existența apelului de donație și destinația fondurilor. O campanie închisă se marchează
ca încheiată și se păstrează pentru documentare; nu se prezintă ca activă.
Nu există încă o verificare automată periodică a acestor apeluri continue.
