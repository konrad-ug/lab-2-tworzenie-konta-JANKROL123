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
        self.historia = []
        self.historia_przelewow_ekspresowych = []
    def przelew_ekspresowy(self, odbiorca, kwota):
        if kwota <= self.saldo:
            self.saldo -= (kwota + self.oplata_za_przelew_ekspresowy)
            odbiorca.saldo += kwota
            self.historia.append(-kwota)
            odbiorca.historia.append(kwota)
            self.historia_przelewow_ekspresowych.append(-self.oplata_za_przelew_ekspresowy)
    def przelew(self, odbiorca, kwota):
        if kwota <= self.saldo:
            odbiorca.saldo += kwota
            self.saldo -= kwota
            self.historia.append(-kwota)
            odbiorca.historia.append(kwota)

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

class RejestrKont:
    lista_kont = []
    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista_kont.append(konto)
    @classmethod
    def znajdz_po_peselu(cls, pesel):
        szukane_konto = None
        for konto in cls.lista_kont:
            if konto.pesel == pesel:
                szukane_konto = konto
        return szukane_konto
    @classmethod
    def liczba_kont(cls):
        return len(cls.lista_kont)
    