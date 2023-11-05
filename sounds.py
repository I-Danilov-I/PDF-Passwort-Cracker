import threading
import time
import sounddevice as sd
import soundfile as sf


# Variable zum Überwachen des Wiedergabe-Threads
playback_thread = None


def audio_play(audio_pfad):
    global playback_thread
    # Dateipfad zur Audiodatei
    audio_file = audio_pfad

    def playback_function():
        print("LOG: Audio-Datei mit soundfile lesen")
        audio_data, sample_rate = sf.read(audio_file, dtype='float32')

        print("LOG: Audiodaten mit sounddevice abspielen")
        sd.play(audio_data, sample_rate)
        sd.wait()

    print("LOG: Starten Sie die Wiedergabe in einem separaten Thread")
    playback_thread = threading.Thread(target=playback_function, daemon=True)
    playback_thread.start()


def stop_audio_playback():
    print("LOG: Playback Audio wird angehalten...")
    global playback_thread
    print("LOG: Wiedergabe-Thread wird beendet...")
    sd.stop()


if __name__ == "__main__":
    # # Beispiel für die Verwendung:
    audio_play("audio/typing.mp3")

    time.sleep(5)

    # # Irgendwann später, wenn Sie die Wiedergabe stoppen möchten:
    stop_audio_playback()
