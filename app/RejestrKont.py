from .Konto import Konto

class RejestrKont:
	konta_osobiste: list[Konto] = []
	@classmethod
	def dodaj_konto(cls, konto: Konto):
		for istniejace_konto in cls.konta_osobiste:
			if istniejace_konto.pesel == konto.pesel:
				return "Konto istnieje"
		cls.konta_osobiste.append(konto)
		return "Konto dodane"
	@classmethod
	def znajdz_po_peselu(cls, pesel: str) -> Konto | None:
		for konto in cls.konta_osobiste:
			if konto.pesel == pesel:
				return konto
		return None
	@classmethod
	def liczba_kont(cls) -> int:
		return len(cls.konta_osobiste)
	@classmethod
	def usun_konto(cls, pesel: str):
		for konto in cls.konta_osobiste:
			if konto.pesel == pesel:
				cls.konta_osobiste.remove(konto)
				return "Usuniete"
		return None
