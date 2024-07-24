def matrizenerstellung(zulässige_kombinationen_busankünfte, entry_anzahl_haltestellen, anzahl_busse_ohne_staffelung,
                       fahrzeiten, anzahl_busse_je_haltestelle_int):
    """
    für jede zulässige Kombination an Busankunftszeiten wird eine Matrix erstellt. Für jede Zelle der Matrix wird
    geprüft, ob eine Anschlussfahrt möglich ist. Wenn eine entsprechende Anschlussfahrt möglich ist, wird eine 1 in die
     Zelle geschrieben. Für Routen zwischen Startpunkt und Zielpunkt, welche nicht als Anschlussfahrt gefahren werden
     können, bleibt eine 0 in der Zelle stehen
    :param zulässige_kombinationen_busankünfte: Liste aus einer Liste mit allen gültigen Busankunftszeiten (basierend
    auf der Methode erstellung_kombination_busankunft)
    :param entry_anzahl_haltestellen: wird benötigt, um für jede Haltestelle eine Spalte in der Matrix zu erstellen
    :param anzahl_busse_ohne_staffelung: entspricht der Anzahl Zeilen der Matrix, da für jede aktuelle Fahrt von einem
    Routenstartpunkt zu einem Zielpunkt eine Zeile benötigt wird
    :param fahrzeiten: Liste aller Fahrzeiten zwischen den Startpunkten (entspricht Spalten) und den Routensatrtpunkten
    zu den Zielpunkten
    :param anzahl_busse_je_haltestelle_int:
    :return: matrizen - für jede kombination an zulässigen busankünften wird eine Matrix erstellt, die in dieser Liste
    zusammengeführt werden
    """
    matrizen = []

    for combination in zulässige_kombinationen_busankünfte:
        # Erstellung einer Matrix mit ausschließlich dem Wert 0 - Anzahl Spalten: Anzahl an Haltestellen; Anzahl Zeilen:
        # Anzahl benötigter Busse ohne Staffelung
        matrix = [[0 for _ in range(int(entry_anzahl_haltestellen.get()))] for _ in range(anzahl_busse_ohne_staffelung)]
        t = 0

        # Diese For-Schleife wird Haltestelle für Haltestelle durchlaufen
        for startpunkt in range(int(entry_anzahl_haltestellen.get())):
            zielpunkt = 0
            p = 0
            # Diese for-Schleife wird Route für Route durchlaufen (für jede Haltestelle nacheinander)
            for row in range(anzahl_busse_ohne_staffelung):
                if zielpunkt >= len(combination):
                    break

                # Hier wird geprüft, ob die Busankunftszeit der aktuellen Variante vom aktuellen startpunkt + die
                # Fahrzeit vom aktuellen Startpunkt über den aktuellen Routenstart zum aktuellen Zielpunkt (in der
                # Liste fahrzeiten) gespeichert kleiner ist, als die Busankunftszeit am Zielpunkt bei der entsprechenden
                # Kombination
                if int(combination[startpunkt]) + int(fahrzeiten[t]) <= int(combination[zielpunkt]):
                    # wird die Bedingung erfüllt, erhält die Matrix an der entsprechenden Stelle eine 1
                    matrix[row][startpunkt] = 1
                # mit jedem Durchgang wird t, um 1 erhöht, um immer auf die nächste Fahrzeit zuzugreifen
                t += 1
                # zudem wird mit jedem Durchgang p um 1 erhöht
                p += 1
                # wenn p der Anzahl an Bussen zu einer entsprechenden Schule entspricht, ist man mit den Fahrten zu
                # diesem Zielpunkt fertig und macht mit dem nächsten Zielpunkt (zielpunkt += 1) weiter
                if p == anzahl_busse_je_haltestelle_int[zielpunkt]:
                    zielpunkt += 1
                    p = 0

        # jede erstellte Matrix für jede Kombination an Busankunftszeiten wird einer Gesamtliste mit allen Matrizen
        # hinzugefügt
        matrizen.append(matrix)

    return matrizen
