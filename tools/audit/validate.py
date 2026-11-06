#!/usr/bin/env python3
"""Validare independentă a registrelor v0.5, fără dependențe externe."""
from pathlib import Path
import csv, datetime, re, sys
ROOT=Path(__file__).resolve().parents[2]/"data"/"audit"
SCHEMAS={"institutii":"institutie_id,denumire,cui,tip_institutie,autoritate_parinte_id,personalitate_juridica,statut,data_infiintarii,data_incetarii,sursa_id","relatii_institutii":"relatie_id,institutie_sursa_id,institutie_destinatie_id,tip_relatie,data_inceput,data_sfarsit,sursa_id","indicatori":"indicator_id,institutie_id,indicator_cod,an,valoare,unitate,perimetru,data_verificarii,sursa_id,verificator_cod","indicatori_dictionar":"indicator_cod,denumire,definitie,unitate,granularitate,metoda_calcul","surse":"sursa_id,titlu,emitent,url,data_document,data_accesarii,tip_sursa,metoda_extragere,verificare_tabel,offset_pagina,hash_sha256,observatii","atributii":"atributie_id,institutie_id,functie_cod,descriere,temei_legal,tip_competenta,tip_intersectie,cofog_cod,regim_juridic,sursa_id","audit_corectii":"corectie_id,tabel,tinta_id,camp,valoare_anterioara,valoare_noua,motiv,data_corectie,sursa_id,verificator_cod","scenarii_reorganizare":"scenariu_id,titlu,tip_scenariu,ipoteze,cost_tranzitie_estimat,economie_estimata,orizont_ani,stadiu,sursa_id","scenariu_institutii":"legatura_id,scenariu_id,institutie_id,rol","proiecte_obligatii":"obligatie_id,institutie_id,obligatie,temei_legal,termen,stadiu,sursa_id","reforme_anuntate":"reforma_id,titlu,data_anuntului,initiator,obiectiv,economie_anuntata,economie_bugetata,economie_realizata,stadiu,sursa_id","reforme_evenimente":"eveniment_id,reforma_id,data_eveniment,tip_eveniment,descriere,act_normativ,sursa_id","afirmatii_publice":"afirmatie_id,reforma_id,text_afirmatie,autor_institutional,data_afirmatie,tip_afirmatie,status_verificare,explicatie,sursa_id","cereri_544":"cerere_id,destinatar,subiect,data_trimiterii,nr_inregistrare,termen_legal,data_raspuns,status,observatii"}
STATUS={"cereri_544":{"pregatita_netrimisa","trimisa_confirmata_de_solicitant","inregistrata","raspuns_partial","raspuns_complet","refuz","contestata"},"afirmatii_publice":{"neanalizata","confirmata","partial_sustinuta","infirmata","neconcludenta"},"reforme_anuntate":{"anuntata","in_curs","finalizata","suspendata","necunoscut"},"institutii":{"activa","reorganizata","desfiintata","exceptata","necunoscut"}}
REFS={"relatii_institutii":{"institutie_sursa_id":"institutii","institutie_destinatie_id":"institutii"},"indicatori":{"institutie_id":"institutii"},"atributii":{"institutie_id":"institutii"},"scenariu_institutii":{"institutie_id":"institutii","scenariu_id":"scenarii_reorganizare"},"reforme_evenimente":{"reforma_id":"reforme_anuntate"},"afirmatii_publice":{"reforma_id":"reforme_anuntate"}}
DATES={"data_infiintarii","data_incetarii","data_inceput","data_sfarsit","data_document","data_accesarii","data_verificarii","data_corectie","data_anuntului","data_eveniment","data_afirmatie","data_trimiterii","data_raspuns","termen_legal","termen"}
def main():
    errors=[]; records={}; ids={}
    for name, header in SCHEMAS.items():
        path=ROOT/(name+".csv")
        if not path.exists():errors.append(f"{name}: lipseste fisierul");continue
        with path.open(encoding="utf-8-sig",newline="") as f:
            reader=csv.DictReader(f); actual=reader.fieldnames or []; expected=header.split(",")
            if actual!=expected:errors.append(f"{name}: antet invalid: {actual}")
            records[name]=list(reader)
        key=next((c for c in expected if c.endswith("_id") and c!= "sursa_id"),None)
        ids[name]={r.get(key,"") for r in records[name] if key and r.get(key)}
        if key and len(ids[name])!=sum(bool(r.get(key)) for r in records[name]):errors.append(f"{name}: ID duplicat sau lipsa")
    for name,rows in records.items():
        for n,row in enumerate(rows,2):
            for field,value in row.items():
                if not value:continue
                if field in DATES:
                    try:datetime.date.fromisoformat(value)
                    except ValueError:errors.append(f"{name}:{n} data invalida {field}={value}")
                if field=="status" and name in STATUS and value not in STATUS[name]:errors.append(f"{name}:{n} status invalid {value}")
                if field=="status_verificare" and value not in STATUS["afirmatii_publice"]:errors.append(f"{name}:{n} status verificare invalid")
                if field=="metoda_extragere" and value not in {"text_structurat","paragrafe_tabel","randare_vizuala","OCR","verificare_incrucisata"}:errors.append(f"{name}:{n} metoda extragere invalida")
                if field=="verificare_tabel" and value not in {"neverificat","verificat_vizual","reconciliat"}:errors.append(f"{name}:{n} verificare tabel invalida")
                target=REFS.get(name,{}).get(field)
                if field=="sursa_id" and name!="surse":target="surse"
                if target and value not in ids.get(target,set()):errors.append(f"{name}:{n} referinta orfana {field}={value}")
    for error in errors:print("EROARE:",error)
    print("OK: schema si integritate verificate" if not errors else f"{len(errors)} erori")
    return bool(errors)
if __name__=="__main__":sys.exit(main())
