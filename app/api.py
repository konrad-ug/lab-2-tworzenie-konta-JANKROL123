from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    ile_kont = RejestrKont.liczba_kont()
    return jsonify(ile_kont), 200
    
@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.znajdz_po_peselu(pesel)
    return jsonify({
        "imie": konto.imie,
        "nazwisko": konto.nazwisko,
        "pesel": konto.pesel
    }), 200

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    konto = RejestrKont.znajdz_po_peselu(pesel)
    if konto == None:
        return jsonify({"error": "nie_istnieje"}), 404
    else:
        dane = request.get_json()
        konto.imie = dane["imie"] if "imie" in dane else konto.imie
        konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
        konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
        return jsonify({
            "imie": konto.imie,
            "nazwisko": konto.nazwisko,
            "pesel": konto.pesel
        }), 200
@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    usuwanie = RejestrKont.usun_konto(pesel)
    if usuwanie == None:
        return jsonify({"error": "nie_istnieje"}), 404
    else:
        return jsonify({"success": "deleted"}), 200
        
# flask --app app/api.py --debug run
