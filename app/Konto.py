class Konto:
    def __init__(self, imie: str, nazwisko: str, pesel: str) -> None:
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.saldo: int = 0
        self.pesel: str = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
