def matrizenerstellung (combinations, anzahl_haltestellen_entry, busses_needed_without, Travel_times, n_ava_values):
    matrizen = []
    schoolstart_combination = []

    for combination in combinations:
        print("Current combination:", combination)
        matrix = [[0 for _ in range(int(anzahl_haltestellen_entry.get()))] for _ in range(busses_needed_without)]
        t = 0

        for col in range(int(anzahl_haltestellen_entry.get())):  # Schleife über die Spalten
            zielpunkt = 0
            p = 0

            for row in range(busses_needed_without):  # Schleife über die Zeilen, begrenzt auf busses_needed_without
                if zielpunkt >= len(combination):
                    break


                if int(combination[col]) + int(Travel_times[t]) <= int(combination[zielpunkt]):
                    matrix[row][col] = 1  # Hier wird das Element gesetzt, Beachte die Zeilen und Spalten vertauschen
                t += 1

                p += 1
                if p == n_ava_values[zielpunkt]:

                    zielpunkt += 1
                    p = 0

        print(f"Combination: {combination}, Result: {matrix}")
        matrizen.append(matrix)
        schoolstart_combination.append(combination)

    return matrizen, schoolstart_combination