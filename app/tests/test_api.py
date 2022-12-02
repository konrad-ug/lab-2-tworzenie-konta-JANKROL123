import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    konto = {
            "imie": "Piotr",
            "nazwisko": "Nowak",
            "pesel": "01928374658"
        }
    def test_1_tworzenie_konta_poprawnie(self):
        r = requests.post("http://localhost:5000/konta/stworz_konto", json = self.konto)
        self.assertEqual(r.status_code, 201)
    def test_2_sprawdz_czy_stworzone_konto(self):
        r_get = requests.get("http://localhost:5000/konta/konto/"+self.konto["pesel"])
        self.assertEqual(r_get.status_code, 200)
        resp_body = r_get.json()
        self.assertEqual(resp_body["imie"], "Piotr")
        self.assertEqual(resp_body["nazwisko"], "Nowak")
        self.assertEqual(resp_body["pesel"], "01928374658")
    def test_3_modyfikacja_konta(self):
        nowe_dane = {
            "imie": "Jan",
            "nazwisko": "Kowalski"
        }
        r = requests.put("http://localhost:5000/konta/konto/"+self.konto["pesel"], json = nowe_dane)
        self.assertEqual(r.status_code, 200)
        resp_body = r.json()
        self.assertEqual(resp_body["imie"], "Jan")
        self.assertEqual(resp_body["nazwisko"], "Kowalski")
        self.assertEqual(resp_body["pesel"], "01928374658")
    def test_4_usuwanie_konta(self):
        r = requests.delete("http://localhost:5000/konta/konto/"+self.konto["pesel"])
        self.assertEqual(r.status_code, 200)

