#!/usr/bin/env python3
"""Validator v0.5: obligatorii, valori controlate, date și integritate referențială."""
from pathlib import Path
from datetime import date
import csv, json, re, sys
ROOT = Path(__file__).resolve().parents[2] / "data" / "audit"
SCHEMAS = {"institutii":["institutie_id","denumire","cui","tip_institutie","nivel_ordonator","autoritate_parinte_id","personalitate_juridica","statut","data_infiintarii","data_incetarii","temei_legal_url","garantii_juridice","restrictii_reorganizare","sursa_id"],"relatii_institutii":["relatie_id","institutie_sursa_id","institutie_destinatie_id","tip_relatie","data_inceput","data_sfarsit","sursa_id"],"indicatori":["indicator_id","institutie_id","indicator_cod","an","perioada","tip_valoare","valoare","unitate","nivel_raportare","perimetru_consolidare_id","perimetru","document_referinta","pagina_sau_tabel","data_verificarii","sursa_id","verificator_cod"],"indicatori_dictionar":["indicator_cod","denumire","definitie","unitate","granularitate","metoda_calcul"],"surse":["sursa_id","titlu","emitent","url","data_document","data_accesarii","tip_sursa","metoda_extragere","verificare_tabel","offset_pagina","hash_sha256","observatii"],"atributii":["atributie_id","institutie_id","functie_cod","descriere","obiect","competenta_teritoriala","beneficiari_entitati_reglementate","temei_legal","tip_competenta","tip_intersectie","cofog_cod","regim_juridic","valabil_de_la","valabil_pana_la","sursa_id"],"audit_corectii":["corectie_id","tabel","tinta_id","camp","valoare_anterioara","valoare_noua","motiv","data_sesizarii","data_corectie","status","decizie_motivata","dovada_url","sursa_id","verificator_cod"],"scenarii_reorganizare":["scenariu_id","titlu","tip_scenariu","varianta","ipoteze","cost_tranzitie_estimat","costuri_transferate","economie_bruta","economie_neta","economie_estimata","orizont_ani","stadiu","sursa_id"],"scenariu_institutii":["legatura_id","scenariu_id","institutie_id","rol"],"proiecte_obligatii":["obligatie_id","institutie_id","obligatie","temei_legal","termen","stadiu","sursa_id"],"reforme_anuntate":["reforma_id","titlu","data_anuntului","initiator","obiectiv","tip_economie","orizont_ani","baza_comparatie","data_scadenta","grad_incredere","economie_anuntata","economie_bugetata","economie_realizata","stadiu","sursa_id"],"reforme_evenimente":["eveniment_id","reforma_id","data_eveniment","tip_eveniment","descriere","act_normativ","sursa_id"],"afirmatii_publice":["afirmatie_id","reforma_id","text_afirmatie","autor_institutional","data_afirmatie","tip_afirmatie","status_verificare","explicatie","sursa_id"],"cereri_544":["cerere_id","destinatar","subiect","data_trimiterii","nr_inregistrare","termen_legal","data_raspuns","status","observatii"],"suprapuneri":["suprapunere_id","atributie_a_id","atributie_b_id","categorie","dovada_sursa_id","status"]}
REQUIRED = {"institutii":["institutie_id","denumire","statut","sursa_id"],"relatii_institutii":["relatie_id","institutie_sursa_id","institutie_destinatie_id","tip_relatie","sursa_id"],"indicatori":["indicator_id","institutie_id","indicator_cod","an","tip_valoare","valoare","unitate","nivel_raportare","sursa_id"],"indicatori_dictionar":["indicator_cod","denumire","definitie","unitate","granularitate"],"surse":["sursa_id","titlu","emitent","tip_sursa","metoda_extragere"],"atributii":["atributie_id","institutie_id","functie_cod","descriere","obiect","sursa_id"],"audit_corectii":["corectie_id","tabel","tinta_id","camp","data_sesizarii","status","sursa_id"],"scenarii_reorganizare":["scenariu_id","titlu","tip_scenariu","varianta","stadiu","sursa_id"],"scenariu_institutii":["legatura_id","scenariu_id","institutie_id","rol"],"proiecte_obligatii":["obligatie_id","institutie_id","obligatie","temei_legal","sursa_id"],"reforme_anuntate":["reforma_id","titlu","data_anuntului","tip_economie","stadiu","sursa_id"],"reforme_evenimente":["eveniment_id","reforma_id","data_eveniment","tip_eveniment","sursa_id"],"afirmatii_publice":["afirmatie_id","text_afirmatie","data_afirmatie","status_verificare","sursa_id"],"cereri_544":["cerere_id","destinatar","subiect","data_trimiterii","status"],"suprapuneri":["suprapunere_id","atributie_a_id","atributie_b_id","categorie","dovada_sursa_id","status"]}
ENUMS = {"institutii":{"statut":["activa","reorganizata","desfiintata","exceptata","necunoscut"]},"cereri_544":{"status":["pregatita_netrimisa","trimisa","depusa","inregistrata","raspuns_partial","raspuns_complet","refuz","contestata"]},"afirmatii_publice":{"status_verificare":["neanalizata","confirmata","partial_sustinuta","infirmata","neconcludenta"]},"reforme_anuntate":{"stadiu":["anuntata","in_curs","finalizata","suspendata","necunoscut"],"grad_incredere":["scazut","mediu","ridicat","neanalizat"]},"suprapuneri":{"categorie":["juridica","generala_speciala","operationala","cooperare_reglementata","perceputa"],"status":["suspectata","in_verificare","confirmata","infirmata","neconcludenta"]},"scenarii_reorganizare":{"stadiu":["ipoteza","evaluare","respins","aprobat"],"varianta":["pesimist","baza","optimist"]},"audit_corectii":{"status":["sesizata","in_analiza","acceptata","respinsa","inchisa"]},"indicatori":{"tip_valoare":["aprobat","bugetat","executat","estimat","anuntat"],"nivel_raportare":["propriu","consolidat"]}}
REFS = {"institutii":{"autoritate_parinte_id":"institutii"},"relatii_institutii":{"institutie_sursa_id":"institutii","institutie_destinatie_id":"institutii"},"indicatori":{"institutie_id":"institutii","indicator_cod":"indicatori_dictionar","perimetru_consolidare_id":"institutii"},"atributii":{"institutie_id":"institutii"},"scenariu_institutii":{"institutie_id":"institutii","scenariu_id":"scenarii_reorganizare"},"proiecte_obligatii":{"institutie_id":"institutii"},"reforme_evenimente":{"reforma_id":"reforme_anuntate"},"afirmatii_publice":{"reforma_id":"reforme_anuntate"},"suprapuneri":{"atributie_a_id":"atributii","atributie_b_id":"atributii"}}
KEYS = {"institutii":"institutie_id","relatii_institutii":"relatie_id","indicatori":"indicator_id","indicatori_dictionar":"indicator_cod","surse":"sursa_id","atributii":"atributie_id","audit_corectii":"corectie_id","scenarii_reorganizare":"scenariu_id","scenariu_institutii":"legatura_id","proiecte_obligatii":"obligatie_id","reforme_anuntate":"reforma_id","reforme_evenimente":"eveniment_id","afirmatii_publice":"afirmatie_id","cereri_544":"cerere_id","suprapuneri":"suprapunere_id"}
DATES = set("data_infiintarii data_incetarii data_inceput data_sfarsit data_document data_accesarii data_verificarii data_corectie data_sesizarii data_anuntului data_scadenta data_eveniment data_afirmatie data_trimiterii data_raspuns termen_legal termen valabil_de_la valabil_pana_la".split())
METHODS = {"text_structurat","paragrafe_tabel","randare_vizuala","OCR","verificare_incrucisata"}
TABLE_CHECKS = {"neverificat","verificat_vizual","reconciliat"}

def validate(root=ROOT):
    errors, records, identifiers = [], {}, {}
    for name, expected in SCHEMAS.items():
        path = root / (name + ".csv")
        if not path.is_file():
            errors.append(f"{name}: fișier lipsă")
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != expected:
                errors.append(f"{name}: antet invalid (așteptat {expected}, primit {reader.fieldnames})")
            records[name] = list(reader)
        key = KEYS[name]
        identifiers[name] = set()
        for line, row in enumerate(records[name], 2):
            value = (row.get(key) or "").strip()
            if value in identifiers[name]:
                errors.append(f"{name}:{line}: ID duplicat {value}")
            if value:
                identifiers[name].add(value)
            for col in REQUIRED[name]:
                if not (row.get(col) or "").strip():
                    errors.append(f"{name}:{line}: câmp obligatoriu lipsă {col}")
            for col, allowed in ENUMS.get(name, {}).items():
                v = (row.get(col) or "").strip()
                if v and v not in allowed:
                    errors.append(f"{name}:{line}: valoare invalidă {col}={v}")
            for col in DATES:
                v = (row.get(col) or "").strip()
                if v:
                    try:
                        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
                            raise ValueError()
                        date.fromisoformat(v)
                    except ValueError:
                        errors.append(f"{name}:{line}: dată invalidă {col}={v}")
            method = (row.get("metoda_extragere") or "").strip()
            if method and method not in METHODS:
                errors.append(f"{name}:{line}: metoda_extragere invalidă")
            check = (row.get("verificare_tabel") or "").strip()
            if check and check not in TABLE_CHECKS:
                errors.append(f"{name}:{line}: verificare_tabel invalidă")
            if name == "indicatori" and row.get("an") and not re.fullmatch(r"\d{4}",row["an"]):
                errors.append(f"{name}:{line}: an invalid")
            if name == "suprapuneri" and row.get("atributie_a_id") == row.get("atributie_b_id"):
                errors.append(f"{name}:{line}: atribuții identice în pereche")
    for name, rows in records.items():
        for line, row in enumerate(rows, 2):
            relations = dict(REFS.get(name, {}))
            if name != "surse" and "sursa_id" in SCHEMAS[name]:
                relations["sursa_id"] = "surse"
            if name == "suprapuneri":
                relations["dovada_sursa_id"] = "surse"
            for col, target in relations.items():
                v = (row.get(col) or "").strip()
                if v and v not in identifiers.get(target, set()):
                    errors.append(f"{name}:{line}: referință orfană {col}={v}")
            if name == "audit_corectii":
                table = row.get("tabel", "")
                target = row.get("tinta_id", "")
                if table not in KEYS:
                    errors.append(f"{name}:{line}: tabel corecție necunoscut {table}")
                elif target and target not in identifiers.get(table,set()):
                    errors.append(f"{name}:{line}: tinta_id orfan {target} în {table}")
    return errors

def main():
    errors = validate()
    for error in errors:
        print("EROARE:", error)
    if errors:
        print(f"FAIL: {len(errors)} erori")
        return 1
    print("OK: schema, câmpuri obligatorii, valori și referințe validate")
    return 0

if __name__ == "__main__":
    sys.exit(main())
