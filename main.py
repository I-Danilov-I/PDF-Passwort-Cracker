# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ main.py ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Modul: zum Arbeiten mit Datum und Zeit
import datetime

# Modul: zum Arbeiten mit dem OS
import sys

# Modul: zum Lesen und Schreiben von PDF-Dateien
import pikepdf

# Importiere Buchstaben und Zeichen
import string

# Um Permutationen (Kombinierungen) mit Zeichen zu ermöglichen
import itertools

# Interagieren mit OS
import os

# Ausgelegte sound.py für die Soundwiedergabe
import sounds

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ VARIABLEN ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Den Arbeitsverzeichnispfad auf das Verzeichnis der ausführbaren Datei setzen
working_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(working_directory)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ FUNKTIONEN ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def auto_format_ausgabe_titel(schrift):
    """
    Formatiert automatisch überschriften.
    :param: schrift: Hier wird der Text übergeben der Formatiert ausgegeben werden soll.
    """

    # Zeichenanzahl berechnung um den Text immer mittig zu halten
    lang = len(schrift)
    lang = int(lang)
    seitlich = (100 - lang - 4) / 2
    seitlich = int(seitlich)

    # Maßen ausgaben (Nur bei änderungen Nötig)
    # print("Mitte Länge: ", lang, seitlich, "Pro seite")

    # Zeichen die für die Formatierung verwendet werden
    a = "<"
    b = ">"
    c = "_"
    kl = "["
    kr = "]"

    # Ausgabe
    print(f"{a * seitlich}{kl} {schrift:{lang}} {kr}{b * seitlich}")
    print(c * 100)

def info():

    """
    <<<<<<<<<<[Das Programm ist ausschließlich für Übungszwecke, verständnislos und lernzwecke gedacht! ]>>>>>>>>>>

    So finden Sie den Pfad zu ihrer verschlüsselten PDF-Datei.
    _________________________________________________________________________________________________________________
    1. Drücken Sie die Schifft_Taste ⍐ (Links auf der Tastatur Pfeil nach oben),
        dann mit rechtsklick auf die PDF-Datei, die Entschlüsselt werden soll.
    2. Als Pfad kopieren mit Links Klick auswählen.
    3. Fügen Sie nun den Pfad hier ein und Bestätigen sie die Eingabe.
     _________________________________________________________________________________________________________________
    Das Programm wird jetzt alle möglichen variationen miteinander Testen.
    Jeh nach Länge des Passwords kann der Vorgang bis zu 48 Stunden dauern.
    Maximale Passwort Länge: 9 Stellen
     _________________________________________________________________________________________________________________
    """

def check_pfad():
    # print("Log: [Check Pfad]")
    """
    Funktion prüft, ob der Pfad vorhanden ist bevor die Permutation beginnen kann.

    :PFAD.replace('"', ""): Korrektur, anführungszeichen werden entfernt, um die Eingabe zu erleichtern.
    :return: Nach der prüfung erhalten wir den verfügbaren Pfad zurück.
    :except: Wenn der Pfad nicht verfügbar, fehler auffangen, anzeigen und zu erneuten eingabe auffordern.
    """
    while True:
        try:
            sounds.audio_play("audio/slam.mp3")
            # Funktion: Als Par. wird String übergeben der dann formatiert wird und dann ausgeben
            print()
            print()
            auto_format_ausgabe_titel("Bitte geben sie den Pfad zu ihrer PDF-Datei")

            # Hier wird der Pfad zu der Passwort geschützen PDF von Benutzer abgefragt
            pfad = input("EINGABE hier:")
            print()
            pfad = pfad.replace('"', "")
            open(pfad)

            # AUDIO:
            sounds.audio_play("audio/accept.mp3")

            auto_format_ausgabe_titel("Diese Pfad ist verfügbar! Programm ist bereit zum Start.")
            input("Drücke [Enter] um den Hack zu starten:")
            return pfad

        except FileNotFoundError:
            print("Der angegebene Pfad konnte nicht gefunden werden!")
            print()
        except OSError:
            print("Der Pfad muss mit dem Laufwerk beginnen:\n"
                  "zB. 'D:\\order\\datei.pdf' ")
            print()

def passwort_pdf_generator(pfad):
    """
    Die product()-Methode kann anstelle der for-Schleife verwendet werden. Es ist prägnant und viel schneller.
    IterTools product()-Methode vs. for-Schleife
    die itertools product()-Methode kann anstelle der for-Schleife verwendet werden. Es ist viel schneller hat
    minimale Code-Unordnung. Da itertools product() Methode einen Iterator gibt, der nur einen Wert nach
    dem anderen zurückgibt; nur auf Abruf.

    _____________________________________________________________________________________________________________
    Syntax: itertools.product(*iterables, repeat)

    Parameter:
        iterables: Iterierbar sind Objekte, die einen Iterator generieren. Zum Beispiel sind gängige Python-Iterable
        List, Tupel, String, Wörterbücher.

        repeat: Er ist ein optionaler Parameter und akzeptiert ganze Zahlen als Wert. Wenn es verwendet wird, gibt
        es das Cartesian-Produkt des Iterables mit sich selbst für die Anzahl der Male zurück, die im
        Wiederholungsparameter angegeben sind.
    """

    # print("Log: [passwort_pdf_generator]")

    # Variable versuchszähler
    anzahl_versuche = 0

    # Variable für Zeichengruppen
    ZEICHEN = string.ascii_lowercase + string.digits + string.punctuation

    # Zeitstempel vor dem Start
    start = datetime.datetime.now()

    # Playback Audio starten
    sounds.audio_play("audio/typing.mp3")

    # Suche nach nummer zwischen 0 und 9 und füge sie als parameter damit wird die Länge der Permutation bestimmt
    for nummern in range(0, 10):
        # Permutation mit den Zeichen aus der Liste ZEICHEN
        for PASSWORD in itertools.product(ZEICHEN, repeat=nummern):
            # Wandle Tupel in einen String
            PASSWORD = "".join(PASSWORD)

            # Try fängt die falsche passwort eingabe auf
            try:
                # Öffne mit pikepdf Datei namens beispiel.pdf / als argument übergeben wir das Passwort als string
                pikepdf.Pdf.open(pfad, password=PASSWORD)

                # Zeitstempel am Ende
                stop = datetime.datetime.now()
                # Berechne Differenz zwischen der fixierten Zeit bei Start und der am Ende, ergibt = Dauer
                dauer = stop - start

                # Stoppe das Playback
                sounds.stop_audio_playback()

                # AUDIO: Gratulation  Starten
                sounds.audio_play("audio/congratulations.mp3")

                # Ausgabe bei Erfolg
                print("🌟" * 21 + " ERFOLG! " + "🌟" * 21 + "\n" + "_" * 100)
                print("Das Passwort ist:", PASSWORD)
                print("Anzahl gescheiterter Versuche:", anzahl_versuche)
                print("Gestartet::", start)
                print("Beendet:", stop)
                print("Gesamtdauer:", dauer)
                print("_" * 100)

                with open("PASSWORD_HIER.txt", "w") as txt_file:
                    txt_file.writelines("Datei Pfad:" + "\n" + pfad + "\n" "PASSWORT:" + PASSWORD)
                    input("Zum beenden drücken sie beliebige taste: ")
                    print()
                    sys.exit("Passwort im Aktuellen Verzeichnis gespeichert! \n")

            # Wenn Datei nicht geöffnet werden konnte, wiederhole den Vorgang
            except pikepdf.PasswordError:
                # Versuche Zähler
                anzahl_versuche += 1
                # Ausgabe
                print("Teste mit: ", PASSWORD)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ HAUPTPROGRAMM ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def main():
    try:
        sounds.audio_play("audio/wind.mp3")
        print(info.__doc__)
        sounds.stop_audio_playback()

        PFAD = check_pfad()
        passwort_pdf_generator(PFAD)
        input("Zum Beenden beliebige Taste drücken: ")
    except KeyboardInterrupt:
        print()
        sys.exit("KeyboardInterrupt. Beenden durch den Benutzer.")


main()
