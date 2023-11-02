# Importiere Buchstaben und Zeichen
import string

# Um Permutationen (Kombinierungen) mit Zeichen zu ermöglichen
import itertools

# Für die Messung der Dauer der Schleife
import datetime

# Systemsteuerung
import sys


# _____________________________________________________________________________________________________________________
# Konstante VARIABLE(Großschreiben, wenn sich der Wert nie ändert)
PASSWORT = "we4u"

# In dieser Variable sind alle Buchstaben, Zahlen und Zeichen definiert
buchstaben = string.ascii_lowercase + string.digits + string.punctuation

# Versuchszähler
ver = 0

# Zeitstempel vor dem Start
start = datetime.datetime.now()

# Suche nach nummer zwischen 0 und 9 und füge sie als parameter
for nummern in range(0, 10):
    # Hier werden auch die gleichen Buchstaben miteinander kombiniert
    for versuch in itertools.product(buchstaben, repeat=nummern):
        # Wandle Tupel in einen String
        versuch = "".join(versuch)
        ver += 1
        print("Teste>>>", versuch, "...")
        if versuch == PASSWORT:
            # Zeitstempel am Ende
            stop = datetime.datetime.now()
            # Berechne Differenz zwischen der fixierten Zeit bei Start und der am Ende, ergibt = Dauer
            dauer = stop - start
            # Ausgabe
            print("🌟" * 21 + " ERFOLG! " + "🌟" * 21 + "\n" + "_" * 100)
            print("Das Passwort ist:", PASSWORT)
            print("Versuche:", ver)
            print("Gestartet::", start)
            print("Beendet:", stop)
            print("Gesamtdauer:", dauer)
            print("_" * 100)
            sys.exit("Ende")
