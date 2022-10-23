class Konto:
    def __init__(self, imie: str, nazwisko: str, pesel: str, kod_promocyjny: str = None) -> None:
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.saldo: int = 0 if kod_promocyjny != "PROM_100" else 50
        self.pesel: str = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
