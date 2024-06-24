# Initialisierung der Listen
s1_start = []
s2_start = []
s3_start = []
s4_start = []
s5_start = []
s6_start = []
s7_start = []

# Startuhrzeiten der Schulen festlegen in Minuten ab 7:00
startzeiten = [
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 1 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 2 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 3 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 4 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 5 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 6 startet ")),
    int(input("Gib an um wie viele Minuten nach 7:00 Schule 7 startet "))
]

# Listen in eine Liste zusammenfassen
starts = [s1_start, s2_start, s3_start, s4_start, s5_start, s6_start, s7_start]

# Schleife durch die Listen und Startzeiten
for i in range(len(starts)):
    start_aktuell = startzeiten[i]
    current_list = starts[i]

    if start_aktuell < 40:
        current_list.extend([start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20, start_aktuell + 25, start_aktuell + 30, start_aktuell + 35, start_aktuell + 40])
    elif start_aktuell >= 40 and start_aktuell < 55:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15, start_aktuell + 20])
    elif start_aktuell >= 55:
        current_list.extend([start_aktuell - 10, start_aktuell - 5, start_aktuell, start_aktuell + 5, start_aktuell + 10, start_aktuell + 15])

# Ausgabe der Listen zur Überprüfung
for i in range(len(starts)):
    print(f"s{i+1}_start: {starts[i]}")
