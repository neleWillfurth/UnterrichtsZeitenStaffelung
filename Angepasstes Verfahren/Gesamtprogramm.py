import csv
import itertools
from itertools import combinations
import pandas
import statistics
import numpy
from collections import defaultdict
d=pandas.read_csv('Daten_rating_system.csv', sep=';')
from collections import Counter



n_reuse = 0
n_reuses = []
n_ava = []
starts = []
startzeiten = []
Startzeiten_aktuell = []
Haltestellennummern=[]
Spaetere_Ankuenfte = []
Weg_Bus_Schule= []
merkmalsliste = []

anzahl_schulen_bus = int(input("Wie viele Schulen mit Busanschluss gibt es im Untersuchungsgebiet? "))
anzahl_schulen= int(input("Wie viele Schulen  gibt es im Untersuchungsgebiet? "))

for i in range (anzahl_schulen):
    s_merkmale = []
    while True:
        Startzeit_aktuell = input(f"Um wie viele Minuten nach 7 startet Schule {i + 1}- als Vielfaches von 5 angeben")
        if Startzeit_aktuell.isdigit() and int(Startzeit_aktuell) % 5 == 0:
            Startzeit_aktuell = int(Startzeit_aktuell)
            Startzeiten_aktuell.append(Startzeit_aktuell)
            s_merkmale.append(Startzeit_aktuell)
            break

    while True:
        Haltestellennummer = input(f"Welche Haltestelle nutzt Schule {i + 1}? ")
        if Haltestellennummer.isdigit():
            Haltestellennummer = int(Haltestellennummer)
            Haltestellennummern.append(Haltestellennummer)
            break
    while True:
        Spatere_Ankunft = input(f"Muss der Schulstart an Schule {i + 1} später liegen, wie an der fühesten Schule, die diese Haltestelle nutzt, weil sie als Anschlussfahrt angefahren wird oder der Fußweg länger ist. Falls ja hier Minutenanzahl angeben, ansonsten 0 eingeben-als Vielfaches von 5 angeben")
        if Spatere_Ankunft.isdigit() and int(Spatere_Ankunft) % 5 == 0:
            Spatere_Ankunft=int(Spatere_Ankunft)
            Spaetere_Ankuenfte.append(Spatere_Ankunft)
            break
    while True:
        Ein_Weg_Bus_Schule = input(f"Wie viel Zeit soll bei Schule {i + 1}  zwischen Busankunft und Schulbeginn liegen? - als Vielfaches von 5 angeben")
        if Ein_Weg_Bus_Schule.isdigit() and int(Ein_Weg_Bus_Schule) % 5 == 0:
            Ein_Weg_Bus_Schule=int(Ein_Weg_Bus_Schule)
            Weg_Bus_Schule.append(Ein_Weg_Bus_Schule)
            break

    while True:
        Schüleranzahl = input(f"Wie viele Schüler hat Schule {i + 1}")
        if Schüleranzahl.isdigit():
            Schüleranzahl=int(Schüleranzahl)
            if Schüleranzahl < 300:
                s_merkmale.append(1)
            elif Schüleranzahl >= 300 and Schüleranzahl < 500:
                s_merkmale.append(2)
            elif Schüleranzahl >= 500 and Schüleranzahl < 700:
                s_merkmale.append(3)
            elif Schüleranzahl >= 700 and Schüleranzahl < 900:
                s_merkmale.append(4)
            elif Schüleranzahl >= 900 and Schüleranzahl < 1100:
                s_merkmale.append(5)
            else:
                s_merkmale.append(6)
            break

    Betreuungangebot_morgens = input(
        f"Gibt es ein Betreuungsangebot morgens vor Unterrichtsbeginn an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n")
    if Betreuungangebot_morgens == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    Betreuungangebot_mittags = input(
        f"Gibt es ein Betreuungsangebot mittags nach Unterrichtsende an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n")
    if Betreuungangebot_mittags == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Mensa = input(f"Gibt es eine Mensa an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n")
    if Mensa == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Lehrer_andere_Schule = input(
        f"Gibt es  an Schule {i + 1} Lehrer, die auch an anderen Schulen unterrichten? Wenn ja - tippe j , wenn nein tippe n")
    if Lehrer_andere_Schule == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Schüler_andere_Schule = input(
        f"Gibt es  an Schule {i + 1} Schüler, die Fächer an anderen Schulen besuchen? Wenn ja - tippe j , wenn nein tippe n")
    if Schüler_andere_Schule == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    merkmalsliste.append(s_merkmale)
print("Haltestellennummern",Haltestellennummern)
print("merkmalsliste",merkmalsliste)

Versatze=[]
for i in range(anzahl_schulen_bus):
    while True:
        anzahl_busse = input(f"Wie viele Busse fahren zur Haltestelle {i + 1}? ")
        if anzahl_busse.isdigit():
            anzahl_busse=int(anzahl_busse)
            n_ava.append(anzahl_busse)
            break
    while True:
        Versatz = input(f" Was ist der größte Versatz bei Haltestelle {i + 1}?, der durch das Planen einer Anschlussfahrt entsteht ")
        if Versatz.isdigit():
            Versatz=int(Versatz)
            Versatze.append(Versatz)
            break

print("anzahl_busse je Haltestelle",n_ava)

busses_needed_without = sum(n_ava)  # Anzahl benötigter Busse ohne Staffelung

print("busses needed without",busses_needed_without)

Travel_times = []

for startpunkt in range(anzahl_schulen_bus):
    for zielpunkt in range(anzahl_schulen_bus):
        for header in range(n_ava[zielpunkt]):
            if startpunkt != zielpunkt:
                while True:
                    travel_time = input(f"Gib die Fahrzeit von Haltestelle {startpunkt + 1} über den Routenstart {header + 1} zur Haltestelle {zielpunkt + 1} an: ")
                    if travel_time.isdigit():
                        travel_time=int(travel_time)
                        travel_time=travel_time+ int(Versatze[zielpunkt])
                        Travel_times.append(travel_time)  # Speichere die Fahrzeit in der Liste
                        break
            else:
                Travel_times.append(100000000)


print("Traveltimes",Travel_times)
Busankunftszeiten_alle_Schulen_aktuell = []

for i in range(anzahl_schulen):
    Busankunft_aktuell=Startzeiten_aktuell[i]-Spaetere_Ankuenfte[i]-Weg_Bus_Schule[i]
    Busankunftszeiten_alle_Schulen_aktuell.append(Busankunft_aktuell)

# Hier wird für jede Schule gespeichert, in welchem Zeitkorridor der Bus an der Planungshaltestelle ankommen muss


print("Busankunftszeiten_alle_Schulen_aktuell",Busankunftszeiten_alle_Schulen_aktuell)
Busankunftszeiten_alle_schule_zulässig=[]
for i in range(anzahl_schulen):
    Busankunft_aktuell = Startzeiten_aktuell[i]
    Startzeiten_Korridor_zulässig = []

    if Startzeiten_aktuell[i] < 40:
        Startzeiten_Korridor_zulässig.extend([Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5, Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15, Busankunftszeiten_alle_Schulen_aktuell[i] + 20, Busankunftszeiten_alle_Schulen_aktuell[i] + 25, Busankunftszeiten_alle_Schulen_aktuell[i] + 30, Busankunftszeiten_alle_Schulen_aktuell[i] + 35, Busankunftszeiten_alle_Schulen_aktuell[i] + 40])
    elif Startzeiten_aktuell[i] >= 40 and Startzeiten_aktuell[i] < 55:
        Startzeiten_Korridor_zulässig.extend([Busankunftszeiten_alle_Schulen_aktuell[i] - 10, Busankunftszeiten_alle_Schulen_aktuell[i] - 5, Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5, Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15, Busankunftszeiten_alle_Schulen_aktuell[i] + 20])
    else:
        Startzeiten_Korridor_zulässig.extend([Busankunftszeiten_alle_Schulen_aktuell[i] - 10, Busankunftszeiten_alle_Schulen_aktuell[i] - 5, Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5, Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15])
    Busankunftszeiten_alle_schule_zulässig.append(Startzeiten_Korridor_zulässig)

print("Busankunftszeiten_alle_schule_zulässig",Busankunftszeiten_alle_schule_zulässig)

Busankunftszeit_Haltestelle = []


i=0
for i in range(anzahl_schulen):
    if Haltestellennummern.count(i+1) == 1:
        index = Haltestellennummern.index(i + 1)
        Busankunftszeit_Haltestelle.append(Busankunftszeiten_alle_schule_zulässig[index])
    else:
        ausgewählte_Busankunftszeiten = []
        for j, busankunftszeit in enumerate(Busankunftszeiten_alle_schule_zulässig):
            if Haltestellennummern[j] == i + 1:
                ausgewählte_Busankunftszeiten.append(busankunftszeit)
        if ausgewählte_Busankunftszeiten:
            # Berechne die Schnittmenge (Intersection) der ausgewählten Busankunftszeiten
            intersection_result = set(ausgewählte_Busankunftszeiten[0]).intersection(*ausgewählte_Busankunftszeiten[1:])
            Busankunftszeit_Haltestelle.append(list(intersection_result))


print("Busankunftszeit_Haltestelle",Busankunftszeit_Haltestelle)
matrizen= []
schoolstart_combination=[]
combinations = list(itertools.product(*Busankunftszeit_Haltestelle))

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

            print(f"combination: {combination}")
            print(f"Travel_times: {Travel_times}")
            print(f"col: {col}, t: {t}, zielpunkt: {zielpunkt}")
            print(f"combination[col]: {combination[col]}")
            print(f"combination[zielpunkt]: {combination[zielpunkt]}")

            if combination[col] + Travel_times[t] <= combination[zielpunkt]:
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

while True:
    Anzahl_Einwohner = input("Wie viele Menschen leben es im Untersuchungsgebiet? ")
    if Anzahl_Einwohner.isdigit():
        Anzahl_Einwohner = int(Anzahl_Einwohner)
        break

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


Var=[]
Durchläufe=0
# Ausgabe der Ergebnisse für die restlichen höchsten Werte
for Durchläufe in range(max_reuses-Busse_hohes_Einsparpotenzial+1):
    print(f"Mit folgenden Varianten werden {max_reuses - Durchläufe} Busse gespart")
    for q in indices_of_values[Durchläufe]:
        print(schoolstart_combination[q])
        Var.append(schoolstart_combination[q])

Gesamtmittelwerte=[]

print(Busankunftszeit_Haltestelle)
print(Counter(Haltestellennummern))


print(merkmalsliste)
Busankunft_alle_Schulen_neu=[]
for Variante in Var:
    s_change_values = []
    Busankunft_alle_Schulen_neu = []

    # Erstelle die Liste Busankunft_alle_Schulen_neu basierend auf den Haltestellennummern
    for nummer in Haltestellennummern:
        Busankunft_alle_Schulen_neu.append(Variante[nummer - 1])

    for i in range(len(Haltestellennummern)):
        index = Haltestellennummern[i]
        s_change = Busankunft_alle_Schulen_neu[i] + Spaetere_Ankuenfte[i % anzahl_schulen] + Weg_Bus_Schule[
            i % anzahl_schulen] - Startzeiten_aktuell[i % anzahl_schulen]
        s_change_values.append(s_change)

    print(s_change_values)
    # Bestimmung der Punkteanzahl für Auswirkungen Schülerleistungen
    Leistungen = []


    def get_index_Leistungen(s_change):
        if s_change <= -30:
            return 14
        elif -30 < s_change <= -20:
            return 15
        elif -20 < s_change <= -5:
            return 16
        elif -5 < s_change < 5:
            return 17
        elif 5 <= s_change <= 10:
            return 18
        elif 10 < s_change <= 20:
            return 19
        elif 20 < s_change <= 30:
            return 20
        else:
            return 21


    # Abhängigkeit des Unterrichtsbeginns
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Unterrichtsbeginn_Leistungen = d.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

        i = get_index_Leistungen(s_change)

        if Unterrichtsbeginn_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Unterrichtsbeginn_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Schüleranzahl
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueleranzahl_Leistungen = d.query('Schueleranzahl == @merkmale[1]')

        i = get_index_Leistungen(s_change)

        if Schueleranzahl_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueleranzahl_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung morgens
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_morgens_Leistungen = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

        i = get_index_Leistungen(s_change)

        if Betreuung_morgens_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Leistungen = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Leistungen(s_change)

        if Betreuung_mittags_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_mittags_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Mensa
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Mensa_Leistungen = d.query('Mensa == @merkmale[4]')

        i = get_index_Leistungen(s_change)

        if Mensa_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Mensa_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Lehrer an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Lehrer_Leistungen = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

        i = get_index_Leistungen(s_change)

        if Lehrer_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Lehrer_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Schüler an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueler_Leistungen = d.query('Schueler_an_anderer_Schule == @merkmale[6]')

        i = get_index_Leistungen(s_change)

        if Schueler_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueler_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Bestimmung der Punkteanzahl für Auswirkungen auf das Betreuungspersonal
    Betreuungspersonal = []


    def get_index_Betreuungspersonal(s_change):
        if s_change <= -30:
            return 28
        elif -30 < s_change <= -20:
            return 29
        elif -20 < s_change <= -5:
            return 30
        elif -5 < s_change < 5:
            return 31
        elif 5 <= s_change <= 10:
            return 32
        elif 10 < s_change <= 20:
            return 33
        elif 20 < s_change <= 30:
            return 34
        else:
            return 35


    # Abhängigkeit des Unterrichtsbeginns
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Unterrichtsbeginn_Betreuungspersonal = d.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

        i = get_index_Betreuungspersonal(s_change)

        if Unterrichtsbeginn_Betreuungspersonal.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Unterrichtsbeginn_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Schüleranzahl
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueleranzahl_Betreuungspersonal = d.query('Schueleranzahl == @merkmale[1]')

        i = get_index_Betreuungspersonal(s_change)

        if Schueleranzahl_Betreuungspersonal.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueleranzahl_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung morgens
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_morgens_Betreuungspersonal = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

        i = get_index_Betreuungspersonal(s_change)

        if Betreuung_morgens_Betreuungspersonal.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Betreuungspersonal = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Betreuungspersonal(s_change)

        if Betreuung_mittags_Betreuungspersonal.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_mittags_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Mensa
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Mensa_Betreuungspersonal = d.query('Mensa == @merkmale[4]')

        i = get_index_Betreuungspersonal(s_change)

        if Mensa_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Mensa_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Lehrer an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Lehrer_Betreuungspersonal = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

        i = get_index_Betreuungspersonal(s_change)

        if Lehrer_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Lehrer_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit Schüler an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueler_Betreuungspersonal = d.query('Schueler_an_anderer_Schule == @merkmale[6]')

        i = get_index_Betreuungspersonal(s_change)

        if Schueler_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueler_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Bestimmung der Punkteanzahl für Auswirkungen auf die Kinderbetreuung
    Kinderbetreuung = []


    def get_index_Kinderbetreuung(s_change):
        if s_change <= -30:
            return 40
        elif -30 < s_change <= -20:
            return 41
        elif -20 < s_change <= -5:
            return 42
        elif -5 < s_change < 5:
            return 43
        elif 5 <= s_change <= 10:
            return 44
        elif 10 < s_change <= 20:
            return 45
        elif 20 < s_change <= 30:
            return 46
        else:
            return 47


    # Abhängigkeit des Unterrichtsbeginns
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Unterrichtsbeginn_Kinderbetreuung = d.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

        i = get_index_Kinderbetreuung(s_change)

        if Unterrichtsbeginn_Kinderbetreuung.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Unterrichtsbeginn_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Schüleranzahl
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueleranzahl_Kinderbetreuung = d.query('Schueleranzahl == @merkmale[1]')

        i = get_index_Kinderbetreuung(s_change)

        if Schueleranzahl_Kinderbetreuung.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueleranzahl_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Betreuung morgens
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_morgens_Kinderbetreuung = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

        i = get_index_Kinderbetreuung(s_change)

        if Betreuung_morgens_Kinderbetreuung.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Betreuung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Kinderbetreuung = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Kinderbetreuung(s_change)

        if Betreuung_mittags_Kinderbetreuung.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_mittags_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Mensa
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Mensa_Kinderbetreuung = d.query('Mensa == @merkmale[4]')

        i = get_index_Kinderbetreuung(s_change)

        if Mensa_Kinderbetreuung.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Mensa_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Lehrer an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Lehrer_Kinderbetreuung = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

        i = get_index_Kinderbetreuung(s_change)

        if Lehrer_Kinderbetreuung.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Lehrer_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Schüler an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueler_Kinderbetreuung = d.query('Schueler_an_anderer_Schule == @merkmale[6]')

        i = get_index_Kinderbetreuung(s_change)

        if Schueler_Kinderbetreuung.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueler_Kinderbetreuung.iloc[:, i].mean()
            Kinderbetreuung.append(mean_value)
        else:
            Kinderbetreuung.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Bestimmung der Punkteanzahl für Auswirkungen auf die Kinder, die selbstaktiv zur Schule gehen
    Selbstaktiv = []


    def get_index_Selbstaktiv(s_change):
        if s_change <= -30:
            return 70
        elif -30 < s_change <= -20:
            return 71
        elif -20 < s_change <= -5:
            return 72
        elif -5 < s_change < 5:
            return 73
        elif 5 <= s_change <= 10:
            return 74
        elif 10 < s_change <= 20:
            return 75
        elif 20 < s_change <= 30:
            return 76
        else:
            return 77


    # Abhängigkeit des Unterrichtsbeginns
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Unterrichtsbeginn_Selbstaktiv = d.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

        i = get_index_Selbstaktiv(s_change)

        if Unterrichtsbeginn_Selbstaktiv.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Unterrichtsbeginn_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Schüleranzahl
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueleranzahl_Selbstaktiv = d.query('Schueleranzahl == @merkmale[1]')

        i = get_index_Selbstaktiv(s_change)

        if Schueleranzahl_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueleranzahl_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Betreuung morgens
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_morgens_Selbstaktiv = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

        i = get_index_Selbstaktiv(s_change)

        if Betreuung_morgens_Selbstaktiv.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Betreuung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Selbstaktiv = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Selbstaktiv(s_change)

        if Betreuung_mittags_Selbstaktiv.shape[
            1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_mittags_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Mensa
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Mensa_Selbstaktiv = d.query('Mensa == @merkmale[4]')

        i = get_index_Selbstaktiv(s_change)

        if Mensa_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Mensa_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Lehrer an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Lehrer_Selbstaktiv = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

        i = get_index_Selbstaktiv(s_change)

        if Lehrer_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Lehrer_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit Schüler an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueler_Selbstaktiv = d.query('Schueler_an_anderer_Schule == @merkmale[6]')

        i = get_index_Selbstaktiv(s_change)

        if Schueler_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueler_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    print("Leistungen" + str(Leistungen))
    print("Betreuungspersonal" + str(Betreuungspersonal))
    print("Kinderbetreuung" + str(Kinderbetreuung))
    print("Selbstaktiv" + str(Selbstaktiv))
    # Bereinigung der Listen
    Leistungen = [x for x in Leistungen if x is not None and not numpy.isnan(x)]
    Betreuungspersonal = [x for x in Betreuungspersonal if x is not None and not numpy.isnan(x)]
    Kinderbetreuung = [x for x in Kinderbetreuung if x is not None and not numpy.isnan(x)]
    Selbstaktiv = [x for x in Selbstaktiv if x is not None and not numpy.isnan(x)]

    # Berechnung der finalen Mittelwerte
    Leistungen_finaler_wert = statistics.mean(Leistungen)
    Betreuungspersonal_finaler_wert = statistics.mean(Betreuungspersonal)
    Kinderbetreuung_finaler_wert = statistics.mean(Kinderbetreuung)
    Selbstaktiv_finaler_wert = statistics.mean(Selbstaktiv)

    Gesamtmittelwert = statistics.mean(
        [Leistungen_finaler_wert, Betreuungspersonal_finaler_wert, Kinderbetreuung_finaler_wert,
         Selbstaktiv_finaler_wert])
    print("Variante", Variante)
    print("Auswirkungen auf Leistungen Gesamtwert:", Leistungen_finaler_wert)
    print("Auswirkungen auf Betreuungspersonal Gesamtwert:", Betreuungspersonal_finaler_wert)
    print("Auswirkungen auf Kinderbetreuung Gesamtwert:", Kinderbetreuung_finaler_wert)
    print("Auswirkungen auf Selbstaktivität Gesamtwert:", Selbstaktiv_finaler_wert)
    print("Gesamtmittelwert:", Gesamtmittelwert)
    Gesamtmittelwerte.append(Gesamtmittelwert)



max_punkte = max(Gesamtmittelwerte)
second_max_punkte = sorted(Gesamtmittelwerte)[-2]
thrird_max_punkte = sorted(Gesamtmittelwerte)[-3]
indices_of_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == max_punkte]
indices_of_second_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == second_max_punkte]
indices_of_third_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == thrird_max_punkte]

for index in indices_of_highest_value:
    print("Die höchste Punktzahl von", max_punkte, "kann mit dieser Variante",Var[index],"erreicht werden")

for index in indices_of_second_highest_value:
    print("Die zweithöchste Punktzahl von", second_max_punkte, "kann mit dieser Variante",Var[index],"erreicht werden")

for index in indices_of_third_highest_value:
    print("Die dritthöchste Punktzahl von", thrird_max_punkte, "kann mit dieser Variante",Var[index],"erreicht werden")