import itertools

#from Matrizenbearbeitung3 import matrizenbearbeitung
n_reuse = 0
n_reuses = []
n_ava= []
starts = []
startzeiten = []
Anzahl_Schulen = int(input("Wie viele Schulen gibt es im Untersuchungsgebiet"))
for i in range(Anzahl_Schulen):
    anzahl_busse = int(input(f"Wie viele Busse fahren zu Schule {i+1} "))
    n_ava.append(anzahl_busse)
    startzeit = int(input(f"Gib an, um wie viele Minuten nach 7:00 Schule {i + 1} startet: "))
    startzeiten.append(startzeit)
    starts.append([])

busses_needed_without = sum(n_ava) #Anzahl benötigter Busse ohne Staffelung
#Angaben der Fahrzeiten
Travel_times= []

# Schleife über alle Startpunkte
for startpunkt in range(Anzahl_Schulen):
 #   # Schleife über alle Zielpunkte
    for zielpunkt in range(Anzahl_Schulen):
   #     # Schleife über alle Zwischenpunkte
        for header in range(n_ava[zielpunkt]):
            if startpunkt != zielpunkt:
                travel_time = int(input(f"Gib die Fahrzeit von Schule {startpunkt + 1} über den Zwischenpunkt {header + 1} zu Schule {zielpunkt + 1} an: "))
                Travel_times.append(travel_time)  # Speichere die Fahrzeit in der Liste
            if startpunkt == zielpunkt:
                Travel_times.append(100000000)



print(Travel_times)



for i in range(len(starts)):
    start_aktuell = startzeiten[i]
    current_list = starts[i]

    if start_aktuell < 40:
        current_list.extend([start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20, start_aktuell + 25, start_aktuell + 30, start_aktuell + 35, start_aktuell + 40])
    elif start_aktuell >= 40 and start_aktuell < 55:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20])
    elif start_aktuell >= 55:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15])


combinations = list(itertools.product(*starts))
for combination in combinations:
    print(combination)
    matrix = [[0 for _ in range(Anzahl_Schulen)] for _ in range(busses_needed_without)]
    i=0
    t=0
    p=0
    zielpunkt=0
    for col in range(len(matrix)):

        if p == n_ava[zielpunkt]:
            print(zielpunkt)
            zielpunkt += 1
            p = 0

        for row in range(len(matrix[col])):
            print("combination[row]",combination[row])
            print("TT[t]",Travel_times[t])
            print ("combination[zielpunkt]",combination[zielpunkt])
            if combination[row] + Travel_times[t] < combination[zielpunkt]:
                matrix[col][row] = 1
            t += 1

        p += 1
    print(matrix)
matrizen = []


print(n_ava)


print(starts)
print(startzeiten)
print(Travel_times)
