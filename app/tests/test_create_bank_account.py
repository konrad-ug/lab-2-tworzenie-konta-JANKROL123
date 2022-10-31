import unittest

from .. import Konto


class TestCreateBankAccount(unittest.TestCase):
    def setUp(self):
        self.imie = "darek"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, "Januszewski", "68042385996")
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "68042385996", "Numer pesel nie został zapisany!")

    def test_niepoprawny_pesel(self):
        konto = Konto(self.imie, "Januszewski", "123")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    def test_konto_mlodego_z_kodem_promocyjnym(self):
        konto = Konto(self.imie, "Januszewski", "68042385996", "PROM_100")
        self.assertEqual(konto.saldo, 50)
    
    def test_konto_mlodego_bez_kodu_promocyjnego(self):
        konto = Konto(self.imie, "Januszewski", "68042385996")
        self.assertEqual(konto.saldo, 0)
    
    def test_konto_mlodego_z_niepoprawnym_kodem_promocyjnym(self):
        konto = Konto(self.imie, "Januszewski", "68042385996", "PROM_123")
        self.assertEqual(konto.saldo, 0)

    def test_konto_seniora_z_poprawnym_kodem_promocyjnym(self):
        konto = Konto(self.imie, "Senior", "05061047375", "PROM_100")
        self.assertEqual(konto.saldo, 0)
    
    def test_konto_seniora_z_niepoprawnym_kodem_promocyjnym(self):
        konto = Konto(self.imie, "Senior", "05061047375", "PROM_123")
        self.assertEqual(konto.saldo, 0)

    def test_konto_seniora_bez_kodu_promocyjnego(self):
        konto = Konto(self.imie, "Senior", "05061047375")
        self.assertEqual(konto.saldo, 0)
