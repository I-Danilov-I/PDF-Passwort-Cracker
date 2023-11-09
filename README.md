# PDF-Passwort-Cracker

Dieses Python-Skript ist ein einfacher PDF-Passwort-Cracker. Es versucht, 
das Passwort einer verschlüsselten PDF-Datei zu knacken,
indem es verschiedene Kombinationen von Zeichen durchläuft.

## Abhängigkeiten

Das Skript verwendet die folgenden Python-Module:

- `datetime`: Zum Arbeiten mit Datum und Zeit.
- `sys`, `time`, `os`: Zum Interagieren mit dem Betriebssystem.
- `pikepdf`: Zum Lesen und Schreiben von PDF-Dateien.
- `string`, `itertools`: Zum Erzeugen von Permutationen (Kombinationen) von Zeichen.
- `sounds`: Ein benutzerdefiniertes Modul zur Wiedergabe von Soundeffekten.

Stellen Sie sicher, dass diese Module installiert und importiert sind, bevor Sie das Skript ausführen.

## Verwendung

Das Skript führt die folgenden Schritte aus:

1. Spielt einen Soundeffekt ab und zeigt die Dokumentation der `info()`-Funktion an.
2. Ruft die Funktion `check_pfad()` auf, um den Pfad zur PDF-Datei zu ermitteln.
3. Ruft die Funktion `passwort_pdf_generator()` auf, um das Passwort der PDF-Datei zu knacken.
4. Fordert den Benutzer auf, eine beliebige Taste zu drücken, um das Skript zu beenden.
5. Spielt einen weiteren Soundeffekt ab und beendet das Skript.

Das Skript fängt auch `KeyboardInterrupt`-Ausnahmen ab und beendet das Skript ordnungsgemäß, 
wenn der Benutzer es während der Ausführung abbricht.

## Hinweis

Bitte verwenden Sie dieses Skript mit Vorsicht, da es dazu gedacht ist, das Passwort von PDF-Dateien zu knacken. 
Es sollte nur für legitime Zwecke verwendet werden, z.B. wenn Sie das Passwort einer PDF-Datei vergessen haben, 
die Sie selbst erstellt haben. Es ist illegal und unethisch, dieses Skript zu verwenden, um auf PDF-Dateien zuzugreifen, 
für die Sie keine Berechtigung haben.
