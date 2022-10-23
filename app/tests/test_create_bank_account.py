import unittest

from .. import Konto


class TestCreateBankAccount(unittest.TestCase):
    def setUp(self):
        self.imie = "darek"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, "Januszewski")
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    #tutaj proszę dodawać nowe testy