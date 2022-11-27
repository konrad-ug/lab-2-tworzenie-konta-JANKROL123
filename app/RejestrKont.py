from .Konto import Konto

class RejestrKont:
	konta_osobiste: list[Konto] = []
	@classmethod
	def dodaj_konto(cls, konto: Konto):
		cls.konta_osobiste.append(konto)
	@classmethod
	def znajdz_po_peselu(cls, pesel: str) -> Konto | None:
		for konto in cls.konta_osobiste:
			if konto.pesel == pesel:
				return konto
		return None
	@classmethod
	def liczba_kont(cls) -> int:
		return len(cls.konta_osobiste)
