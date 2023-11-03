# audio_funktionen.py
import sounddevice as sd  # Für die Audiowiedergabe
import soundfile as sf  # Für das Lesen von Audiodateien

# Diese Funktion spielt eine Audiodatei ab
def spiele_audio(dateipfad):
    # Lies die Audiodaten und die Abtastrate (Samplerate) aus der Datei
    data, samplerate = sf.read(dateipfad)
    # Spiele die Audiodaten ab
    sd.play(data, samplerate)
    # Warte, bis die Wiedergabe abgeschlossen ist
    sd.wait()

# Diese Funktion spielt den Slam-Sound einmal ab
def spiele_slam():
    # print("Log: [Starte slam Sound...]")
    dateipfad = "audio/slam.mp3"  # Dateipfad für den Slam-Sound
    spiele_audio(dateipfad)  # Rufe die Funktion auf, um den Slam-Sound abzuspielen
    # print("Log: [Beende slam Sound...]")

# Diese Funktion spielt den Wind-Sound einmal ab
def spiele_wind():
    # print("Log: [Starte Wind Sound...]")
    dateipfad = "audio/wind.mp3"  # Dateipfad für den Wind-Sound
    spiele_audio(dateipfad)  # Rufe die Funktion auf, um den Wind-Sound abzuspielen
    # print("Log: [Beende Wind Sound...]")

def spiele_success():
    # print("Log: [Starte success Sound...]")
    dateipfad = "audio/success.mp3"  # Dateipfad für den Wind-Sound
    spiele_audio(dateipfad)  # Rufe die Funktion auf, um den Wind-Sound abzuspielen
    # print("Log: [Beende success Sound...]")
