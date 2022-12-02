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


