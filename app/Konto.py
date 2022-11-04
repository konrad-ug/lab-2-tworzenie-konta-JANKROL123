<<<<<<< HEAD
class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
=======
def oblicz_rok_urodzenia_z_peselu(pesel: str) -> int:
    # https://pl.wikipedia.org/wiki/PESEL#Data_urodzenia
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    if miesiac > 80:
        rok += 1800
    elif miesiac > 60:
        rok += 2200
    elif miesiac > 40:
        rok += 2100
    elif miesiac > 20:
        rok += 2000
    else:
        rok += 1900
    return rok

class KontoPrototyp:
    def __init__(self):
        self.saldo = 0
    def przelew_ekspresowy(self, odbiorca, kwota):
        if kwota <= self.saldo:
            self.saldo -= (kwota + self.oplata_za_przelew_ekspresowy)
            odbiorca.saldo += kwota
    def przelew(self, odbiorca, kwota):
        if kwota <= self.saldo:
            odbiorca.saldo += kwota
            self.saldo -= kwota

class Konto(KontoPrototyp):
    oplata_za_przelew_ekspresowy = 1
    def __init__(self, imie: str, nazwisko: str, pesel: str, kod_promocyjny: str = None) -> None:
        super().__init__()
        rok_urodzenia: int = oblicz_rok_urodzenia_z_peselu(pesel)
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.saldo: int = 50 if kod_promocyjny == "PROM_100" and rok_urodzenia > 1960 else 0
        self.pesel: str = pesel if len(pesel) == 11 else "Niepoprawny pesel!"



class KontoFirmowe(KontoPrototyp):
    oplata_za_przelew_ekspresowy = 5
    def __init__(self, nazwa, nip):
        super().__init__()
        self.nazwa = nazwa
        self.nip = nip if len(nip) == 10 else "Niepoprawny NIP"
>>>>>>> 23b74b49167adcc9276e24bb5c09521232f76bd1
