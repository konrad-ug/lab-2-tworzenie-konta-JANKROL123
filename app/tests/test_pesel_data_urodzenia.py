from ..Konto import oblicz_rok_urodzenia_z_peselu

import unittest

# https://pesel.cstudios.pl/o-generatorze/generator-on-line



class TestPeselDataUrodzenia(unittest.TestCase):
    def test_2000(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("00291717539"), 2000)
    
    def test_1989(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("89091762637"), 1989)

    def test_2100(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("00491788254"), 2100)
    
    def test_1820(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("20911788254"), 1820)
    
    def test_2223(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("23621788254"), 2223)

    def test_1959(self):
        self.assertEqual(oblicz_rok_urodzenia_z_peselu("59091754783"), 1959)
