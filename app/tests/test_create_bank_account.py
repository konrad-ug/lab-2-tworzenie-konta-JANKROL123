import unittest

from .. import (Konto, KontoFirmowe)


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

class TestTransfer(unittest.TestCase):
    def test_przelew(self):
        wysylajacy = Konto("jan", "kowalski", "84100912345")
        odbiorca = Konto("piotr", "nowak", "68120554321")
        wysylajacy.saldo = 50
        wysylajacy.przelew(odbiorca, 10)
        self.assertEqual(wysylajacy.saldo, 40)
        self.assertEqual(odbiorca.saldo, 10)
    def test_przelew_z_za_duza_kwota(self):
        wysylajacy = Konto("jan", "kowalski", "84100912345")
        odbiorca = Konto("piotr", "nowak", "68120554321")
        wysylajacy.przelew(odbiorca, 10)
        self.assertEqual(wysylajacy.saldo, 0)
        self.assertEqual(odbiorca.saldo, 0)

class TestBusinessAccount(unittest.TestCase):
    def test_tworzenie_kont_firmowych(self):
        pierwsze_konto_firmowe = KontoFirmowe("index firma", "1234567890")
        self.assertEqual(pierwsze_konto_firmowe.nazwa, "index firma")
        self.assertEqual(pierwsze_konto_firmowe.nip, "1234567890")
    def test_niepoprawny_nip(self):
        konto_z_niepoprawnym_nipem = KontoFirmowe("sigma firma", "098765")
        self.assertEqual(konto_z_niepoprawnym_nipem.nip, "Niepoprawny NIP")

class TestExpressTransfer(unittest.TestCase):
    def test_poprawny_przelew_ekspresowy_firma(self):
        konto_wysylajace = KontoFirmowe("firma1", "1234567890")
        konto_odbierajace = KontoFirmowe("firma2", "0987654321")
        konto_wysylajace.saldo = 50
        konto_wysylajace.przelew_ekspresowy(konto_odbierajace, 20)
        self.assertEqual(konto_wysylajace.saldo, 25)
        self.assertEqual(konto_odbierajace.saldo, 20)
    def test_poprawny_przelew_ekspresowy_czlowiek(self):
        wysylajacy = Konto("jan", "kowalski", "84100912345")
        odbiorca = Konto("piotr", "nowak", "68120554321")
        wysylajacy.saldo = 10
        wysylajacy.przelew_ekspresowy(odbiorca, 5)
        self.assertEqual(wysylajacy.saldo, 4)
        self.assertEqual(odbiorca.saldo, 5)
    def test_niepoprawny_przelew_ekspresowy_firma(self):
        konto_wysylajace = KontoFirmowe("firma1", "1234567890")
        konto_odbierajace = KontoFirmowe("firma2", "0987654321")
        konto_wysylajace.saldo = 50
        konto_wysylajace.przelew_ekspresowy(konto_odbierajace, 60)
        self.assertEqual(konto_wysylajace.saldo, 50)
        self.assertEqual(konto_odbierajace.saldo, 0)
    def test_niepoprawny_przelew_ekspresowy_czlowiek(self):
        wysylajacy = Konto("jan", "kowalski", "84100912345")
        odbiorca = Konto("piotr", "nowak", "68120554321")
        wysylajacy.saldo = 10
        wysylajacy.przelew_ekspresowy(odbiorca, 15)
        self.assertEqual(wysylajacy.saldo, 10)
        self.assertEqual(odbiorca.saldo, 0)
class TestHistory(unittest.TestCase):
    def test_historii_przelewu(self):
        konto1 = Konto("jan", "kowalski", "12345678909")
        konto2 = Konto("piotr", "nowak", "00987654321")
        konto1.saldo = 10
        konto1.przelew(konto2, 3)
        self.assertEqual(konto1.historia, [-3])
        self.assertEqual(konto2.historia, [3])
    def test_historii_przelewu_ekspresowego(self):
        konto1 = Konto("jan", "kowalski", "12345678909")
        konto2 = Konto("piotr", "nowak", "00987654321")
        firma1 = KontoFirmowe("firma1", "1234567890")
        firma2 = KontoFirmowe("firma2", "0234567890")
        konto1.saldo = 10
        firma1.saldo = 10
        konto1.przelew_ekspresowy(konto2, 3)
        firma1.przelew_ekspresowy(firma2, 2)
        self.assertEqual(konto1.historia, [-3])
        self.assertEqual(konto2.historia, [3])
        self.assertEqual(konto1.historia_przelewow_ekspresowych, [-1])
        self.assertEqual(konto2.historia_przelewow_ekspresowych, [])
        self.assertEqual(firma1.historia, [-2])
        self.assertEqual(firma2.historia, [2])
        self.assertEqual(firma1.historia_przelewow_ekspresowych, [-5])
        self.assertEqual(firma2.historia_przelewow_ekspresowych, [])
class TestKredyt(unittest.TestCase):
    def test_kredyt(self):
        konto = Konto("jan", "kowalski", "0192837465")
        