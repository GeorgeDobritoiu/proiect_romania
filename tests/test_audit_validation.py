"""Teste negative pentru integritatea datelor de audit."""
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("audit_validate", ROOT / "tools/audit/validate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class AuditValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        for name, columns in module.SCHEMAS.items():
            with (self.path / (name + ".csv")).open("w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerow(columns)

    def add(self, name, **values):
        with (self.path / (name + ".csv")).open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow([values.get(c, "") for c in module.SCHEMAS[name]])

    def source_and_institution(self):
        self.add("surse", sursa_id="SRC-1", titlu="Act", emitent="Emitent", tip_sursa="act_normativ", metoda_extragere="randare_vizuala")
        self.add("institutii", institutie_id="INS-1", denumire="Instituție test", statut="activa", sursa_id="SRC-1")
        self.add("indicatori_dictionar", indicator_cod="POST", denumire="Posturi", definitie="Număr posturi", unitate="posturi", granularitate="an")

    def indicator(self, **overrides):
        row=dict(indicator_id="IND-1",institutie_id="INS-1",indicator_cod="POST",an="2025",tip_valoare="executat",valoare="100",unitate="posturi",nivel_raportare="propriu",sursa_id="SRC-1")
        row.update(overrides)
        self.add("indicatori",**row)

    def test_empty_files_are_valid(self):
        self.assertEqual(module.validate(self.path), [])

    def test_indicator_without_source_is_rejected(self):
        self.source_and_institution()
        self.indicator(sursa_id="")
        self.assertTrue(any("câmp obligatoriu lipsă sursa_id" in x for x in module.validate(self.path)))

    def test_invalid_institution_status_is_rejected(self):
        self.add("surse",sursa_id="SRC-1",titlu="Act",emitent="Emitent",tip_sursa="act_normativ",metoda_extragere="text_structurat")
        self.add("institutii",institutie_id="INS-1",denumire="Instituție test",statut="inventat",sursa_id="SRC-1")
        self.assertTrue(any("statut=inventat" in x for x in module.validate(self.path)))

    def test_orphan_institution_reference_is_rejected(self):
        self.source_and_institution()
        self.indicator(institutie_id="INS-404")
        self.assertTrue(any("referință orfană institutie_id" in x for x in module.validate(self.path)))

    def test_unknown_indicator_code_is_rejected(self):
        self.source_and_institution()
        self.indicator(indicator_cod="INEXISTENT")
        self.assertTrue(any("referință orfană indicator_cod" in x for x in module.validate(self.path)))

    def test_orphan_correction_target_is_rejected(self):
        self.source_and_institution()
        self.add("audit_corectii",corectie_id="COR-1",tabel="indicatori",tinta_id="IND-404",camp="valoare",data_sesizarii="2026-11-06",status="sesizata",sursa_id="SRC-1")
        self.assertTrue(any("tinta_id orfan" in x for x in module.validate(self.path)))


    def test_confirmed_overlap_with_press_only_is_rejected(self):
        self.source_and_institution()
        self.add("surse", sursa_id="PRESS", titlu="Articol", emitent="Redacție",
                 tip_sursa="presa", metoda_extragere="text_structurat")
        for key in ("A", "B"):
            self.add("atributii", atributie_id=key, institutie_id="INS-1",
                     functie_cod="CTRL", descriere="Control", obiect="alimente", sursa_id="SRC-1")
        self.add("suprapuneri", suprapunere_id="OV-1", atributie_a_id="A",
                 atributie_b_id="B", categorie="operationala", dovada_sursa_id="PRESS", status="confirmata")
        self.assertTrue(any("confirmare fără sursă primară" in e for e in module.validate(self.path)))

    def test_confirmed_claim_with_press_only_is_rejected(self):
        self.source_and_institution()
        self.add("surse", sursa_id="PRESS", titlu="Articol", emitent="Redacție",
                 tip_sursa="presa", metoda_extragere="text_structurat")
        self.add("afirmatii_publice", afirmatie_id="AF-1", text_afirmatie="Afirmație",
                 data_afirmatie="2026-11-06", status_verificare="confirmata", sursa_id="PRESS")
        self.assertTrue(any("verdict fără sursă primară" in e for e in module.validate(self.path)))

    def test_non_numeric_indicator_is_rejected(self):
        self.source_and_institution()
        self.indicator(valoare="abc")
        self.assertTrue(any("valoare nenumerică" in e for e in module.validate(self.path)))

    def test_indicator_unit_mismatch_is_rejected(self):
        self.source_and_institution()
        self.indicator(unitate="lei")
        self.assertTrue(any("unitate diferită de dicționar" in e for e in module.validate(self.path)))

    def test_reversed_overlap_duplicate_is_rejected(self):
        self.source_and_institution()
        for key in ("A", "B"):
            self.add("atributii", atributie_id=key, institutie_id="INS-1",
                     functie_cod="CTRL", descriere="Control", obiect="alimente", sursa_id="SRC-1")
        for number, a, b in ((1,"A","B"),(2,"B","A")):
            self.add("suprapuneri", suprapunere_id=f"OV-{number}", atributie_a_id=a,
                     atributie_b_id=b, categorie="operationala", dovada_sursa_id="SRC-1", status="suspectata")
        self.assertTrue(any("pereche duplicată" in e for e in module.validate(self.path)))

    def test_self_parent_is_rejected(self):
        self.add("surse",sursa_id="SRC-1",titlu="Act",emitent="Emitent",tip_sursa="act_normativ",metoda_extragere="text_structurat")
        self.add("institutii",institutie_id="INS-1",denumire="Instituție",statut="activa",
                 autoritate_parinte_id="INS-1",sursa_id="SRC-1")
        self.assertTrue(any("propriul părinte" in e for e in module.validate(self.path)))

    def test_deadline_before_submission_is_rejected(self):
        self.add("cereri_544",cerere_id="C1",destinatar="MADR",subiect="Cerere",
                 data_trimiterii="2026-11-06",termen_legal="2026-11-05",status="depusa")
        self.assertTrue(any("anterior trimiterii" in e for e in module.validate(self.path)))

if __name__ == "__main__":
    unittest.main()
