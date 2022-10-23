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

class Konto:
    def __init__(self, imie: str, nazwisko: str, pesel: str, kod_promocyjny: str = None) -> None:
        rok_urodzenia: int = oblicz_rok_urodzenia_z_peselu(pesel)
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.saldo: int = 50 if kod_promocyjny == "PROM_100" and rok_urodzenia > 1960 else 0
        self.pesel: str = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
