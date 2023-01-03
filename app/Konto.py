import os
from datetime import date

import requests


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
    def zaciagnij_kredyt(self, kwota):
        if len(self.historia) < 5:
            return False
        trzy_ostatnie = self.historia[-3:]
        piec_ostatnich = self.historia[-5:]
        suma_pieciu_ostatnich = 0
        for transakcja in trzy_ostatnie:
            if transakcja < 0:
                return False
        for kwota_transakcji in piec_ostatnich:
            suma_pieciu_ostatnich += kwota_transakcji
        if suma_pieciu_ostatnich <= kwota:
            return False 
        self.saldo += kwota
        return True


class KontoFirmowe(KontoPrototyp):
    oplata_za_przelew_ekspresowy = 5
    def __init__(self, nazwa, nip):
        super().__init__()
        self.nazwa = nazwa
        self.nip = nip if len(nip) == 10 else "Niepoprawny NIP"
        if self.nip == nip:
            self.sprawdz_w_ministerstwie()
    def zaciagnij_kredyt(self, kwota_kredytu):
        if self.saldo < 2*kwota_kredytu:
            return False
        status = False
        for transakcja in self.historia:
            if transakcja == -1775:
                status = True 
                break
        if status:
            self.saldo += kwota_kredytu
        return status
    def sprawdz_w_ministerstwie(self):
        gov_url = os.getenv("BANK_APP_MF_NIP", "https://wl-api.mf.gov.pl/")
        data = date.today()
        zapytanie = requests.get(f"{gov_url}api/search/nip/{self.nip}?date={data}")
        if zapytanie.status_code == 200 and zapytanie.json["result"]["subject"] != None: 
            pass
        elif zapytanie.status_code == 200 and zapytanie.json["result"]["subject"] == None: 
            self.nip = "Pranie"
        else:
            raise Exception("Nie można połączyć się z ministerstwem finansów")
        