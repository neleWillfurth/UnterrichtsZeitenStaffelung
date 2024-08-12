def matrizenbearbeitung(matrix, anzahl_busse_pro_haltestelle_liste, anzahl_busse_je_haltestelle_unverbraucht,
                        anzahl_busse_je_haltestelle_zählvariable, anzahl_busse_je_haltestelle_maximal,
                        anzahl_wiedergenutzter_busse):
    """
    Für jede Matrix wird bestimmt, wie viele Busse bei dieser Matrix wiedergenutzt werden können

    :param matrix: ist eine matrix aus der Matrizenliste
    :param anzahl_busse_pro_haltestelle_liste: gibt an, wie viele Busse zu jeder Haltestelle fahren
    :param anzahl_busse_je_haltestelle_unverbraucht: ist am Anfang identisch zu anzahl_busse_pro_haltestelle_liste
    allerdings wird bei jeder Wiedernutzung eines Busses der Wert am entsprechenden Index um 1 verringert
    :param anzahl_busse_je_haltestelle_zählvariable: die Liste hat zu Beginn den Wert 0 für jede Haltestelle, mit jeder
    Fahrt zu einer Haltestelle wird der Wert, um 1 erhöht, um sicherzugehen, dass zu einer Haltestelle nicht mehr als
    die benötigte Anzahl an Bussen fährt
    :param anzahl_busse_je_haltestelle_maximal: ist am Anfang identisch zu anzahl_busse_pro_haltestelle_liste und dient
    dazu zu vergleichen, ob anzahl_busse_je_haltestelle_zählvariable kleiner ist, wie die maximale Busanzahl zu einer
    Haltestelle
    :param anzahl_wiedergenutzter_busse: Anzahl an Bussen, die bei dieser Matrix wiedergenutzt (also eingespart werden
    können)
    :return: anzahl_wiedergenutzer_busse
    """
    while any(int(value) > 0 for value in anzahl_busse_pro_haltestelle_liste):
        row_index = 0
        # man geht die Matrix Zeile für Zeile durch
        for row in matrix:
            row_sum = sum(row)

            # Wenn in einer Zeile nur einmal der Wert 1 vorkommt bedeutet dies, dass die entsprechende Fahrt (von einem
            # Routenstartpunkt zu einem Zielpunkt nur als Anschlussfahrt von einer bestimmten Schule gemacht werden kann
            if row_sum == 1:
                index2 = row.index(1)

                # Wenn die Zielhaltestelle noch Busse benötigt und die Starthaltestelle noch Busse zu Anschlussnutzung
                # übrig hat, wird anzahl_wiedergenutzter_busse um 1 erhöht
                if (anzahl_busse_je_haltestelle_unverbraucht[index2] > 0 and
                        anzahl_busse_je_haltestelle_zählvariable[index2] < anzahl_busse_je_haltestelle_maximal[index2]):
                    anzahl_wiedergenutzter_busse += 1
                    # die Anzahl unvebrauchter Busse nimmt durch die Wiedernutzung um 1 ab
                    anzahl_busse_je_haltestelle_unverbraucht[index2] -= 1
                    for i in range(len(row)):
                        row[i] = 0

                    # Aktualisiere die max_busanfahrten_pro_haltestelle Liste
                    for a in range(len(anzahl_busse_pro_haltestelle_liste)):
                        if a == 0 and row_index <= anzahl_busse_pro_haltestelle_liste[a]:
                            anzahl_busse_je_haltestelle_zählvariable[a] += 1
                        elif a > 0 and row_index > anzahl_busse_pro_haltestelle_liste[a - 1]:
                            anzahl_busse_je_haltestelle_zählvariable[a] += 1
                        elif (a == len(anzahl_busse_pro_haltestelle_liste) - 1
                              and row_index > anzahl_busse_pro_haltestelle_liste[a - 1]):
                            anzahl_busse_je_haltestelle_zählvariable[a] += 1

            row_index += 1
        # Reduziere die Anzahl der Busse pro Haltestelle um 1 (dies ermöglicht ein kontinuierliches Weiterlaufen des
        # Prozesses
        for a in range(len(anzahl_busse_pro_haltestelle_liste)):
            anzahl_busse_pro_haltestelle_liste[a] -= 1

        for i in range(len(anzahl_busse_pro_haltestelle_liste)):
            row_index2 = 0
            # Wenn an einer Haltestelle durch die Reduzierung um 1 der Wert 0 erreicht wird, wird jeder Zeile der
            # Matrix durchgegangen
            if anzahl_busse_pro_haltestelle_liste[i] == 0:
                for zeile in matrix:
                    index3 = zeile[i]

                    # wenn ich von der Schule kommend noch unverbrauchte Busse habe und die Fahrten zum entsprechenden
                    # Zielpunkt noch nicht die maximale Anzahl an Bussen zu diesem Zielpunkt erreicht ist, steigt die
                    # Anzahl wiedergenutzer Busse um 1
                    if (zeile[i] == 1 and anzahl_busse_je_haltestelle_unverbraucht[i] > 0
                            and anzahl_busse_je_haltestelle_zählvariable[index3] <
                            anzahl_busse_je_haltestelle_maximal[index3]):
                        anzahl_wiedergenutzter_busse += 1
                        for j in range(len(zeile)):
                            zeile[j] = 0
                        # durch die Wiedernutzung wird die Anzahl unverbrauchter Busse um 1 reduziert
                        anzahl_busse_je_haltestelle_unverbraucht[i] -= 1
                        if anzahl_busse_je_haltestelle_unverbraucht[i] == 0:
                            anzahl_busse_je_haltestelle_unverbraucht[i] = -1

                        # Aktualisiere die max_busanfahrten_pro_haltestelle Liste
                        for a in range(len(anzahl_busse_pro_haltestelle_liste)):
                            if a == 0 and row_index2 <= anzahl_busse_pro_haltestelle_liste[a]:
                                anzahl_busse_je_haltestelle_zählvariable[a] += 1
                            elif a > 0 and row_index2 > anzahl_busse_pro_haltestelle_liste[a - 1]:
                                anzahl_busse_je_haltestelle_zählvariable[a] += 1
                            elif (a == len(anzahl_busse_pro_haltestelle_liste) - 1
                                  and row_index2 > anzahl_busse_pro_haltestelle_liste[a - 1]):
                                anzahl_busse_je_haltestelle_zählvariable[a] += 1

                    row_index2 += 1
        if anzahl_busse_pro_haltestelle_liste[a] == 0:
            anzahl_busse_pro_haltestelle_liste[a] = -1

        index = 0
        while len(anzahl_busse_pro_haltestelle_liste) > index:
            # Wenn bei einer Schule die Zählvariable 0 erreicht, wird diese Spalte auf 0 gesetzt (durch die Zeilen 62-88
            # wird sichergestellt, dass keine möglichen Wiedernutzungen nicht berücksichtigt werden, bevor die Spalte
            # auf 0 gesetzt wird. Durch dieses auf 0 setzten, wird der Prozess am Laufen gehalten, da es nun neue Zeilen
            # gibt, die eine Zeilensumme von 1 haben (Z. 29)
            if anzahl_busse_pro_haltestelle_liste[index] == 0:
                for row in matrix:
                    row[index] = 0
            index += 1

    return anzahl_wiedergenutzter_busse
