class Konto:
    def __init__(self, imie: str, nazwisko: str) -> None:
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.saldo: int = 0
