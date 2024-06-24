#Matrizenerstellung funktioniert korrekt - Aktuell Implemetierung der Matrizenbearbeiung
import itertools


n_reuse = 0
n_reuses = []
n_ava = []
starts = []
startzeiten = []
anzahl_schulen_bus = int(input("Wie viele Schulen mit Busanschluss gibt es im Untersuchungsgebiet? "))
for i in range(anzahl_schulen_bus):
    anzahl_busse = int(input(f"Wie viele Busse fahren zu Schule {i + 1}? "))
    n_ava.append(anzahl_busse)
    startzeit = int(input(f"Gib an, um wie viele Minuten nach 7:00 Schule {i + 1} startet: "))
    startzeiten.append(startzeit)
    starts.append([])

busses_needed_without = sum(n_ava)  # Anzahl benötigter Busse ohne Staffelung
# Angaben der Fahrzeiten
Travel_times = []

for startpunkt in range(anzahl_schulen_bus):
    for zielpunkt in range(anzahl_schulen_bus):
        for header in range(n_ava[zielpunkt]):
            if startpunkt != zielpunkt:
                travel_time = int(input(f"Gib die Fahrzeit von Schule {startpunkt + 1} über den Zwischenpunkt {header + 1} zu Schule {zielpunkt + 1} an: "))
                Travel_times.append(travel_time)  # Speichere die Fahrzeit in der Liste
            else:
                Travel_times.append(100000000)

print(Travel_times)

for i in range(len(starts)):
    start_aktuell = startzeiten[i]
    current_list = starts[i]

    if start_aktuell < 40:
        current_list.extend([start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20, start_aktuell + 25, start_aktuell + 30, start_aktuell + 35, start_aktuell + 40])
    elif start_aktuell >= 40 and start_aktuell < 55:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20])
    else:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15])
matrizen= []
schoolstart_combination=[]
combinations = list(itertools.product(*starts))
for combination in combinations:
    print("Current combination:", combination)
    matrix = [[0 for _ in range(anzahl_schulen_bus)] for _ in range(busses_needed_without)]
    t = 0

    for col in range(anzahl_schulen_bus):  # Schleife über die Spalten
        zielpunkt = 0
        p = 0

        for row in range(busses_needed_without):  # Schleife über die Zeilen, begrenzt auf busses_needed_without
            if zielpunkt >= len(combination):
                break

            print("Aktueller row Index:", row)
            print("Aktueller col Index:", col)
            print("combination[col]:", combination[col])
            print("TT[t]:", Travel_times[t])
            print("combination[zielpunkt]:", combination[zielpunkt])

            if combination[col] + Travel_times[t] < combination[zielpunkt]:
                matrix[row][col] = 1  # Hier wird das Element gesetzt, Beachte die Zeilen und Spalten vertauschen
                print("+1")
            t += 1

            p += 1
            if p == n_ava[zielpunkt]:
                print("zielpunkt vor Erhöhung:", zielpunkt)
                zielpunkt += 1
                p = 0

    print(f"Combination: {combination}, Result: {matrix}")
    matrizen.append(matrix)
    schoolstart_combination.append(combination)


n_reuses=[]

from Matrizenbearbeitung_felxibel import matrizenbearbeitung
for matrix in matrizen:
    print('neuer Durchlauf')
    max_anfahrten = []
    for i in range(len(n_ava)):
        max_anfahrten.append(0)
    n_ava_unverbraucht = n_ava.copy()
    n_anfahrten = n_ava.copy()
    n_reuse = 0
    n_reuse_einzel = matrizenbearbeitung(matrix, n_ava.copy(), n_ava_unverbraucht, n_reuse,max_anfahrten, n_anfahrten)
    n_reuses.append(n_reuse_einzel)


print(n_reuses)

# Wie viele Busse sollen mindestens eingespart werden? - Bestimmung hohes Einsparpotenzial
Anzahl_Einwohner = int(input("Wie viele Menschen leben es im Untersuchungsgebiet? "))
Teiler = 83300000/Anzahl_Einwohner
Busse_hohes_Einsparpotenzial = int(19600*1.15/Teiler)+1
print(Busse_hohes_Einsparpotenzial)


max_reuses = max(n_reuses)

indices_of_values = []


# Berechnen und Ausgeben, solange die Einsparung nicht hoch genug ist
for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial+1):
    # Neue Liste für jeden Durchlauf erstellen
    indices = [i for i, x in enumerate(n_reuses) if x == max_reuses - Durchläufe]
    indices_of_values.append(indices)  # Diese Liste in indices_of_values sammeln
    print("Durchläufe", Durchläufe)
    print("max_reuses-Busse hohes Einsparpotenzial", max_reuses - Busse_hohes_Einsparpotenzial)

print(indices_of_values)

# Ergbnistext
print("-------------------------------------------------------------")
print("Das sind die Ergebnisse")
print("Ohne Staffelung von Unterrichtszeiten werden " + str(busses_needed_without) + " Busse benötigt")
print(f"Eine hohe Buseinsparung wird ab {Busse_hohes_Einsparpotenzial} erreicht")
print(f"Die maximal einzusparende Busanzahl beträgt {max_reuses}")


Durchläufe=0
# Ausgabe der Ergebnisse für die restlichen höchsten Werte
for Durchläufe in range(max_reuses-Busse_hohes_Einsparpotenzial+1):
    print(f"Mit folgenden Varianten werden {max_reuses - Durchläufe} Busse gespart")
    for q in indices_of_values[Durchläufe]:
        print(schoolstart_combination[q])
    print(len(indices_of_values[Durchläufe]))