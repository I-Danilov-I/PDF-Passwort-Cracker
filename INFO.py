# Importiere Buchstaben und Zeichen
import string
import itertools

print("Grß/Klein Buchstaben:", string.ascii_letters)

# sollen 2 Par gibt Anzahl der Kombinationen, gleiche werte werden nicht kombinierten
print(list(itertools.permutations(["a", "b", "c"], 3)))

# Hier werden auch die gleichen Buchstaben miteinander kombiniert
print(list(itertools.product(["a", "b", "c"], repeat=3)))
