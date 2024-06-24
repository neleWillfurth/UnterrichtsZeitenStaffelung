def matrizenbearbeitung(matrix, n_ava, n_ava_unverbraucht, n_reuse, max_anfahrten, n_anfahrten):
    print(matrix)
    print(n_ava)
    print(n_ava_unverbraucht)
    print(n_reuse)

    while any(value > 0 for value in n_ava):
        print("---------------------------------------")
        row_index = 0
        for row in matrix:
            row_sum = sum(row)

            if row_sum == 1:
                index2 = row.index(1)
                column_sums = [sum(matrix[i][index2] for i in range(row_index) if sum(matrix[i]) == 1)]
                print(index2)
                print("n_ava_index" + str(n_ava_unverbraucht[index2]))
                print(column_sums[0])

                if n_ava_unverbraucht[index2] > 0 and max_anfahrten[index2] < n_anfahrten[index2]:
                    n_reuse += 1
                    n_ava_unverbraucht[index2] -= 1
                    for i in range(len(row)):
                        row[i] = 0

                    print(index2)
                    print("max_Anfahrten")
                    print(max_anfahrten)

                    for a in range(len(n_ava)):
                        if a == 0 and row_index <= n_ava[a]:
                            max_anfahrten[a] += 1
                        elif a > 0 and row_index > n_ava[a - 1] and row_index <= n_ava[a]:
                            max_anfahrten[a] += 1
                        elif a == len(n_ava) - 1 and row_index > n_ava[a - 1]:
                            max_anfahrten[a] += 1

                    print(max_anfahrten)

                print("n_ava_index_nach" + str(n_ava_unverbraucht[index2]))
                print("Row_index" + str(row_index))
                print(max_anfahrten)
                print(n_reuse)
            row_index += 1

        # We decrease the number of buses available for re-use at the school represented by row j, n_availablej, by 1.
        for a in range(len(n_ava)):
            n_ava[a] -= 1

        print(n_ava)
        print(n_ava_unverbraucht)

        for i in range(len(n_ava)):
            row_index2 = 0
            if n_ava[i] is not None:
                if n_ava[i] == 0:
                    print("Hallo")
                    for zeile in matrix:
                        print("i" + str(i))
                        print(zeile[i])
                        index3 = zeile[i]
                        print(n_ava[i])
                        print(n_ava_unverbraucht[i])
                        print(row_index2)

                        if zeile[i] == 1 and n_ava_unverbraucht[i] > 0 and max_anfahrten[index3] < n_anfahrten[index3]:
                            print("hier")
                            print(zeile)
                            for j in range(len(zeile)):
                                zeile[j] = 0
                            print(zeile)
                            n_ava_unverbraucht[i] -= 1
                            if n_ava_unverbraucht[i] == 0:
                                n_ava_unverbraucht[i] = -1
                            print(n_ava_unverbraucht)
                            print("Max anfahrten_unten")
                            print(max_anfahrten)

                            for a in range(len(n_ava)):
                                if a == 0 and row_index2 <= n_ava[a]:
                                    max_anfahrten[a] += 1
                                elif a > 0 and row_index2 > n_ava[a - 1] and row_index2 <= n_ava[a]:
                                    max_anfahrten[a] += 1
                                elif a == len(n_ava) - 1 and row_index2 > n_ava[a - 1]:
                                    max_anfahrten[a] += 1

                            print(max_anfahrten)
                            n_reuse += 1

                        row_index2 += 1
                        print(row_index2)
        if n_ava[a] == 0:
            n_ava[a] = -1

        print(n_reuse)

        # Entfernen der Spalten aus der Matrix, wenn die Anzahl der verfügbaren Busse für eine Schule gleich 0 ist
        index = 0
        print(n_ava)

        while len(n_ava) > index:
            if n_ava[index] == 0:
                for row in matrix:
                    row[index] = 0
            index += 1
        print(matrix)
        print(n_reuse)
    # Ausgabe der gefilterten Daten

    return n_reuse
