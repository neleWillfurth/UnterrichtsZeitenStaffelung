def matrizenbearbeitung(matrix, anzahl_busse_pro_haltestelle_liste, anzahl_busse_pro_haltestelle_liste_unverbraucht, anzahl_wiedergenutzer_busse, max_busanfahrten_pro_haltestelle, n_anfahrten):
    print(matrix)
    print(anzahl_busse_pro_haltestelle_liste)
    print(anzahl_busse_pro_haltestelle_liste_unverbraucht)
    print(anzahl_wiedergenutzer_busse)

    while any(int(value) > 0 for value in anzahl_busse_pro_haltestelle_liste):
        print("---------------------------------------")
        row_index = 0
        for row in matrix:
            row_sum = sum(row)

            if row_sum == 1:
                index2 = row.index(1)
                column_sums = [sum(matrix[i][index2] for i in range(row_index) if sum(matrix[i]) == 1)]
                print(index2)
                print("anzahl_busse_pro_haltestelle_liste_index" + str(anzahl_busse_pro_haltestelle_liste_unverbraucht[index2]))
                print(column_sums[0])

                if anzahl_busse_pro_haltestelle_liste_unverbraucht[index2] > 0 and max_busanfahrten_pro_haltestelle[index2] < n_anfahrten[index2]:
                    anzahl_wiedergenutzer_busse += 1
                    anzahl_busse_pro_haltestelle_liste_unverbraucht[index2] -= 1
                    for i in range(len(row)):
                        row[i] = 0

                    print(index2)
                    print("max_busanfahrten_pro_haltestelle")
                    print(max_busanfahrten_pro_haltestelle)

                    for a in range(len(anzahl_busse_pro_haltestelle_liste)):
                        if a == 0 and row_index <= anzahl_busse_pro_haltestelle_liste[a]:
                            max_busanfahrten_pro_haltestelle[a] += 1
                        elif a > 0 and row_index > anzahl_busse_pro_haltestelle_liste[a - 1] and row_index <= anzahl_busse_pro_haltestelle_liste[a]:
                            max_busanfahrten_pro_haltestelle[a] += 1
                        elif a == len(anzahl_busse_pro_haltestelle_liste) - 1 and row_index > anzahl_busse_pro_haltestelle_liste[a - 1]:
                            max_busanfahrten_pro_haltestelle[a] += 1

                    print(max_busanfahrten_pro_haltestelle)

                print("anzahl_busse_pro_haltestelle_liste_index_nach" + str(anzahl_busse_pro_haltestelle_liste_unverbraucht[index2]))
                print("Row_index" + str(row_index))
                print(max_busanfahrten_pro_haltestelle)
                print(anzahl_wiedergenutzer_busse)
            row_index += 1

        # We decrease the number of buses available for re-use at the school represented by row j, anzahl_busse_pro_haltestelle_listeilablej, by 1.
        for a in range(len(anzahl_busse_pro_haltestelle_liste)):
            anzahl_busse_pro_haltestelle_liste[a]-=1

        print(anzahl_busse_pro_haltestelle_liste)
        print(anzahl_busse_pro_haltestelle_liste_unverbraucht)

        for i in range(len(anzahl_busse_pro_haltestelle_liste)):
            row_index2 = 0
            if anzahl_busse_pro_haltestelle_liste[i] is not None:
                if anzahl_busse_pro_haltestelle_liste[i] == 0:
                    print("Hallo")
                    for zeile in matrix:
                        print("i" + str(i))
                        print(zeile[i])
                        index3 = zeile[i]
                        print(anzahl_busse_pro_haltestelle_liste[i])
                        print(anzahl_busse_pro_haltestelle_liste_unverbraucht[i])
                        print(row_index2)

                        if zeile[i] == 1 and anzahl_busse_pro_haltestelle_liste_unverbraucht[i] > 0 and max_busanfahrten_pro_haltestelle[index3] < n_anfahrten[index3]:
                            print("hier")
                            print(zeile)
                            for j in range(len(zeile)):
                                zeile[j] = 0
                            print(zeile)
                            anzahl_busse_pro_haltestelle_liste_unverbraucht[i] -= 1
                            if anzahl_busse_pro_haltestelle_liste_unverbraucht[i] == 0:
                                anzahl_busse_pro_haltestelle_liste_unverbraucht[i] = -1
                            print(anzahl_busse_pro_haltestelle_liste_unverbraucht)
                            print("Max anfahrten_unten")
                            print(max_busanfahrten_pro_haltestelle)

                            for a in range(len(anzahl_busse_pro_haltestelle_liste)):
                                if a == 0 and row_index2 <= anzahl_busse_pro_haltestelle_liste[a]:
                                    max_busanfahrten_pro_haltestelle[a] += 1
                                elif a > 0 and row_index2 > anzahl_busse_pro_haltestelle_liste[a - 1] and row_index2 <= anzahl_busse_pro_haltestelle_liste[a]:
                                    max_busanfahrten_pro_haltestelle[a] += 1
                                elif a == len(anzahl_busse_pro_haltestelle_liste) - 1 and row_index2 > anzahl_busse_pro_haltestelle_liste[a - 1]:
                                    max_busanfahrten_pro_haltestelle[a] += 1

                            print(max_busanfahrten_pro_haltestelle)
                            anzahl_wiedergenutzer_busse += 1

                        row_index2 += 1
                        print(row_index2)
        if anzahl_busse_pro_haltestelle_liste[a] == 0:
            anzahl_busse_pro_haltestelle_liste[a] = -1

        print(anzahl_wiedergenutzer_busse)

        # Entfernen der Spalten aus der Matrix, wenn die Anzahl der verfuegbaren Busse fuer eine Schule gleich 0 ist
        index = 0
        print(anzahl_busse_pro_haltestelle_liste)

        while len(anzahl_busse_pro_haltestelle_liste) > index:
            if anzahl_busse_pro_haltestelle_liste[index] == 0:
                for row in matrix:
                    row[index] = 0
            index += 1
        print(matrix)
        print(anzahl_wiedergenutzer_busse)
    # Ausgabe der gefilterten Daten

    return anzahl_wiedergenutzer_busse
