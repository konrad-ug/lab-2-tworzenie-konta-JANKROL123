import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "darek"
    pesel = "38497392043"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, "Januszewski", self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "PESEL nie został podany!")
        
    #tutaj proszę dodawać nowe testy