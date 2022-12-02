import unittest
from parameterized import parameterized, parameterized_class  # type: ignore
from .. import (Konto, KontoFirmowe, RejestrKont)

class TestRejestrKont(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		konto1 = Konto("Jan", "Kowalski", "09876543212")
		RejestrKont.dodaj_konto(konto1)
	@classmethod
	def tearDownClass(cls):
		RejestrKont.konta_osobiste = []
    
	def test_1_rejestr_kont(self):
		self.assertEqual(RejestrKont.liczba_kont(), 1)
		konto_jana = RejestrKont.znajdz_po_peselu("09876543212")
		self.assertEqual(konto_jana.imie, "Jan")
		self.assertEqual(konto_jana.nazwisko, "Kowalski")
		self.assertEqual(konto_jana.pesel, "09876543212")
		nowe_konto = Konto("Krzysztof", "Nowak", "12345678901")
		RejestrKont.dodaj_konto(nowe_konto)
		self.assertEqual(RejestrKont.liczba_kont(), 2)
		konto_krzysztofa = RejestrKont.znajdz_po_peselu("12345678901")
		self.assertEqual(konto_krzysztofa.imie, "Krzysztof")
		self.assertEqual(konto_krzysztofa.nazwisko, "Nowak")
		self.assertEqual(konto_krzysztofa.pesel, "12345678901")
		konto_adama = RejestrKont.znajdz_po_peselu("00345678901")
		self.assertIsNone(konto_adama)

