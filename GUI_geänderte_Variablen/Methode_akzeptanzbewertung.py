import statistics
import numpy
import pandas


def akzeptanzbewertung_rechnen(merkmale_alle_schulen, kombinationen_buseinkünfte_hohe_einsparung,
                               entry_anzahl_schulen, haltestellennummern_alle_schulen, versatz_ankunft_anschlussfahrt,
                               wegdauer_haltestelle_schule, aktueller_unterrichtsbeginn_alle_schulen):
    """
    Durchführung der Akzeptanzbepunktung

    :param merkmale_alle_schulen: Liste bestehend aus einer Liste pro Schule mit den Schulcharakteristiken
    :param kombinationen_buseinkünfte_hohe_einsparung: alle Kombinationen an Busankunftszeiten mit welchen eine hohe
    Buseinsparung erreicht wird
    :param entry_anzahl_schulen: Anzahl Schulen
    :param haltestellennummern_alle_schulen: Liste, die für jede Schule die Haltestellennummer beinhaltet
    :param versatz_ankunft_anschlussfahrt: bei einer anschlussfahrt wird hier die benötigte Zeit von der früheren zur
    späteren Haltestelle mit der identischen Nummer eingegeben
    :param wegdauer_haltestelle_schule: gibt die benötigte Zeit zwischen Busankunft und Unterrichtsbeginn je
    Schule an
    :param aktueller_unterrichtsbeginn_alle_schulen: Liste mit den Unterrichtsbeginnzeiten aller Schulen (in Minuten
    nach 7:00 angegeben)
    :return: gesamtmittelwerte_akzeptanzbewertung - liste mit der Akzeptanzpunktzahl für jede Kombination an
    Busankunftszeiten mit hoher Buseinsparung
    """
    daten_befragung = pandas.read_csv('Befragungsdaten.csv', sep=';')

    gesamtmittelwerte_akzeptanzbewertung = []

    # die Akzeptanzbepunktung wird für jede Kombination an Busankunftszeiten mit hoher Buseinsaprung durchgeführt
    for combination in kombinationen_buseinkünfte_hohe_einsparung:
        verschiebungen_unterrichtsbeginn = []
        anzahl_schulen = int(entry_anzahl_schulen.get())
        # für jede Schule wird bestimmt um wie viel sich der Unterrichtsbeginn bei der entsprechenden Kombination
        # verschieben würde
        for i in range(anzahl_schulen):
            index = int(haltestellennummern_alle_schulen[i].get())
            verschiebung_unterrichtsbeginn = (combination[index - 1] + int(versatz_ankunft_anschlussfahrt[i].get()) +
                                              int(wegdauer_haltestelle_schule[i].get()) -
                                              int(aktueller_unterrichtsbeginn_alle_schulen[i].get()))
            # die einzelnen verschiebungen werden zu einer Liste zusammengeführt
            verschiebungen_unterrichtsbeginn.append(verschiebung_unterrichtsbeginn)

        # Bestimmung der Punkteanzahl für Auswirkungen Schülerleistungen
        akzeptanzeinzelwerte_leistung = []

        # basierend auf die Stärke der Verschiebung des Unterrichtsbeginns wird ein anderer Index zurückgegeben, welcher
        # dafür entscheidend ist, auf welche Spalte der Umfragedaten zugegriffen wird (in den entsprechenden Spalten
        # stehen die entsprechenden Werte wie eine entsprechende Verschiebung des Unterrichtsbeginns in Bezug auf
        # Leistungsauswirkungen bepunktet wird

        def spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn):
            if verschiebung_unterrichtsbeginn <= -30:
                return 14  # in Spalte 15 der Daten stehen die Befragungsergebnisse darauf, wie sich die Leistung der
                # Schüler durch eine Verschiebung des Unterrichtsbeginns um mindestens 30 Minuten nach vorne ändert
            elif -30 < verschiebung_unterrichtsbeginn <= -20:
                return 15
            elif -20 < verschiebung_unterrichtsbeginn <= -5:
                return 16
            elif -5 < verschiebung_unterrichtsbeginn < 5:
                return 17
            elif 5 <= verschiebung_unterrichtsbeginn <= 10:
                return 18
            elif 10 < verschiebung_unterrichtsbeginn <= 20:
                return 19
            elif 20 < verschiebung_unterrichtsbeginn <= 30:
                return 20
            else:
                return 21

        # basierend auf den aktuellen Unterrichtsbeginn werden die Akzeptanzwerte für die Auswirkungen auf die Leistung
        # bestimmt
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen mit dem identischen Unterrichtsbeginn
            # weiter berücksichtigt werden
            einfluss_unterrichtsbeginn_leistungen = daten_befragung.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_unterrichtsbeginn_leistungen.shape[1] > i:
                # der Mittelwert der Daten aus Spalte i wird bestimmt und der Liste akzeptanzeinzelwerte_leistung
                # hinzugefügt
                mean_value = einfluss_unterrichtsbeginn_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # basierend auf die Schüleranzahl werden die Akzeptanzwerte für die Auswirkungen auf die Leistung bestimmt
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen in der identischen Schüleranzahlklasse
            # weiter berücksichtigt werden
            einfluss_schueleranzahl_leistungen = daten_befragung.query('Schueleranzahl == @merkmale[1]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_schueleranzahl_leistungen.shape[1] > i:
                # der Mittelwert der Daten aus Spalte i wird bestimmt und der Liste akzeptanzeinzelwerte_leistung
                # hinzugefügt
                mean_value = einfluss_schueleranzahl_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # basierend, ob es eine Betreuung vor Unterrichtsbeginn gibt, werden die Akzeptanzwerte für die Auswirkungen
        # auf die Leistung bestimmt
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung bieten weiter berücksichtigt werden
            einfluss_betreuung_morgens_leistungen = daten_befragung.query('Betreuung_vor_Unterricht == @merkmale[2]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_morgens_leistungen.shape[1] > i:
                mean_value = einfluss_betreuung_morgens_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # Ahängigkeit der Betreeung mittags
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung nach Unterrichtsende bieten, weiter berücksichtigt werden
            einfluss_betreuung_mittags_leistungen = daten_befragung.query('Betreuung_nach_Unterricht == @merkmale[3]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_mittags_leistungen.shape[1] > i:
                mean_value = einfluss_betreuung_mittags_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # Abhängigkeit vom Vorhandensein einer Mensa
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls eine Mensa bzw. keine
            # Mensa haben, weiter berücksichtigt werden
            einfluss_mensa_leistungen = daten_befragung.query('Mensa == @merkmale[4]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_mensa_leistungen.shape[1] > i:
                mean_value = einfluss_mensa_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # Abhängigkeit davon, ob Lehrer auch an anderen Schulen unterrichten
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Lehrer haben, die an
            # anderen Schulen unterrichten bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_lehrer_leistungen = daten_befragung.query('Lehrer_an_anderer_Schule == @merkmale[5]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_lehrer_leistungen.shape[1] > i:
                mean_value = einfluss_lehrer_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # Abhängigkeit davon, ob Schüler auch Fächer an anderen Schulen besuchen
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Schüler haben, die an
            # Fächer an anderen Schulen besuchen bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_schüler_leistungen = daten_befragung.query('Schueler_an_anderer_Schule == @merkmale[6]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = spaltenindex_leistungen_erhalten(verschiebung_unterrichtsbeginn)

            if einfluss_schüler_leistungen.shape[1] > i:
                mean_value = einfluss_schüler_leistungen.iloc[:, i].mean()
                akzeptanzeinzelwerte_leistung.append(mean_value)
            else:
                akzeptanzeinzelwerte_leistung.append(None)

        # Bestimmung der Punkteanzahl für Auswirkungen auf das akzeptanzeinzelwerte_betreuungspersonal
        akzeptanzeinzelwerte_betreuungspersonal = []

        # basierend auf die Stärke der Verschiebung des Unterrichtsbeginns wird ein anderer Index zurückgegeben, welcher
        # dafür entscheidend ist, auf welche Spalte der Umfragedaten zugegriffen wird (in den entsprechenden Spalten
        # stehen die entsprechenden Werte wie eine entsprechende Unterrichtsberscgiebung in Bezug auf
        # die Auswirkungen auf das Betreuungspersonal bepunktet wird
        def get_index_betreuungspersonal(verschiebung_unterrichtsbeginn):
            if verschiebung_unterrichtsbeginn <= -30:
                return 28
            elif -30 < verschiebung_unterrichtsbeginn <= -20:
                return 29
            elif -20 < verschiebung_unterrichtsbeginn <= -5:
                return 30
            elif -5 < verschiebung_unterrichtsbeginn < 5:
                return 31
            elif 5 <= verschiebung_unterrichtsbeginn <= 10:
                return 32
            elif 10 < verschiebung_unterrichtsbeginn <= 20:
                return 33
            elif 20 < verschiebung_unterrichtsbeginn <= 30:
                return 34
            else:
                return 35

        # Abhängigkeit des Unterrichtsbeginns
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen mit dem identischen Unterrichtsbeginn
            # weiter berücksichtigt werden
            einfluss_unterrichtsbeginn_betreuungspersonal = (daten_befragung.query
                                                             ('Schulbeginn_Stunde1_7Uhr == @merkmale[0]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_unterrichtsbeginn_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_unterrichtsbeginn_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # In Abhängigkeit der Schüleranzahl
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen in der identischen Schüleranzahlklasse
            # weiter berücksichtigt werden
            einfluss_schueleranzahl_betreuungspersonal = daten_befragung.query('Schueleranzahl == @merkmale[1]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_schueleranzahl_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_schueleranzahl_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Ahängigkeit der Betreeung morgens
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung bieten weiter berücksichtigt werden
            einfluss_betreuung_morgens_betreuungspersonal = (daten_befragung.query
                                                             ('Betreuung_vor_Unterricht == @merkmale[2]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_morgens_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_betreuung_morgens_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Ahängigkeit der Betreeung mittags
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung nach Unterrichtsende bieten, weiter berücksichtigt werden
            einfluss_betreuung_mittags_betreuungspersonal = (daten_befragung.query
                                                             ('Betreuung_nach_Unterricht == @merkmale[3]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_mittags_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_betreuung_mittags_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Abhängigkeit Mensa
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls eine Mensa bzw. keine
            # Mensa haben, weiter berücksichtigt werden
            einfluss_mensa_betreuungspersonal = daten_befragung.query('Mensa == @merkmale[4]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_mensa_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_mensa_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Abhängigkeit davon, ob Lehrer auch an anderen Schulen unterrichten
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            einfluss_lehrer_betreuungspersonal = daten_befragung.query('Lehrer_an_anderer_Schule == @merkmale[5]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_lehrer_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_lehrer_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Abhängigkeit davon, ob Schüler auch Fächer an anderen Schulen besuchen
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Schüler haben, die an
            # Fächer an anderen Schulen besuchen bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_schüler_betreuungspersonal = daten_befragung.query('Schueler_an_anderer_Schule == @merkmale[6]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_betreuungspersonal(verschiebung_unterrichtsbeginn)

            if einfluss_schüler_betreuungspersonal.shape[1] > i:
                mean_value = einfluss_schüler_betreuungspersonal.iloc[:, i].mean()
                akzeptanzeinzelwerte_betreuungspersonal.append(mean_value)
            else:
                akzeptanzeinzelwerte_betreuungspersonal.append(None)

        # Bestimmung der Punkteanzahl für Auswirkungen auf die Kinderbetreuung
        akzeptanzeinzelwerte_kinderbetreuung = []

        # basierend auf die Stärke der Verschiebung des Unterrichtsbeginns wird ein anderer Index zurückgegeben, welcher
        # dafür entscheidend ist, auf welche Spalte der Umfragedaten zugegriffen wird (in den entsprechenden Spalten
        # stehen die entsprechenden Werte wie eine entsprechende Unterrichtsberscgiebung in Bezug auf
        # die Auswirkungen auf die Kinderbetreuung in den Familien bepunktet wird
        def get_index_kinderbetreuung(verschiebung_unterrichtsbeginn):
            if verschiebung_unterrichtsbeginn <= -30:
                return 40
            elif -30 < verschiebung_unterrichtsbeginn <= -20:
                return 41
            elif -20 < verschiebung_unterrichtsbeginn <= -5:
                return 42
            elif -5 < verschiebung_unterrichtsbeginn < 5:
                return 43
            elif 5 <= verschiebung_unterrichtsbeginn <= 10:
                return 44
            elif 10 < verschiebung_unterrichtsbeginn <= 20:
                return 45
            elif 20 < verschiebung_unterrichtsbeginn <= 30:
                return 46
            else:
                return 47

        # Abhängigkeit des Unterrichtsbeginns
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen mit dem identischen Unterrichtsbeginn
            # weiter berücksichtigt werden
            einfluss_unterrichtsbeginn_kinderbetreuung = (daten_befragung.query
                                                          ('Schulbeginn_Stunde1_7Uhr == @merkmale[0]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_unterrichtsbeginn_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_unterrichtsbeginn_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit der Schüleranzahl
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen in der identischen Schüleranzahlklasse
            # weiter berücksichtigt werden
            einfluss_schueleranzahl_kinderbetreuung = daten_befragung.query('Schueleranzahl == @merkmale[1]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_schueleranzahl_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_schueleranzahl_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit der Betreuung morgens
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung bieten weiter berücksichtigt werden
            einfluss_betreuung_morgens_kinderbetreuung = (daten_befragung.query
                                                          ('Betreuung_vor_Unterricht == @merkmale[2]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_morgens_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_betreuung_morgens_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit der Betreuung mittags
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung nach Unterrichtsende bieten, weiter berücksichtigt werden
            einfluss_betreuung_mittags_kinderbetreuung = (daten_befragung.query
                                                          ('Betreuung_nach_Unterricht == @merkmale[3]'))

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_mittags_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_betreuung_mittags_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit Mensa
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls eine Mensa bzw. keine
            # Mensa haben, weiter berücksichtigt werden
            einfluss_mensa_kinderbetreuung = daten_befragung.query('Mensa == @merkmale[4]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_mensa_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_mensa_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit davon, ob Lehrer auch an anderen Schulen unterrichten
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Lehrer haben, die an
            # anderen Schulen unterrichten bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_lehrer_kinderbetreuung = daten_befragung.query('Lehrer_an_anderer_Schule == @merkmale[5]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_lehrer_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_lehrer_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Abhängigkeit davon, ob Schüler auch Fächer an anderen Schulen besuchen
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Schüler haben, die an
            # Fächer an anderen Schulen besuchen bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_schüler_kinderbetreuung = daten_befragung.query('Schueler_an_anderer_Schule == @merkmale[6]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_kinderbetreuung(verschiebung_unterrichtsbeginn)

            if einfluss_schüler_kinderbetreuung.shape[1] > i:
                mean_value = einfluss_schüler_kinderbetreuung.iloc[:, i].mean()
                akzeptanzeinzelwerte_kinderbetreuung.append(mean_value)
            else:
                akzeptanzeinzelwerte_kinderbetreuung.append(None)

        # Bestimmung der Punkteanzahl für Auswirkungen auf die Kinder, die selbstaktiv zur Schule gehen
        akzeptanzeinzelwerte_selbstaktive_schüler = []

        # basierend auf die Stärke der Verschiebung des Unterrichtsbeginns wird ein anderer Index zurückgegeben, welcher
        # dafür entscheidend ist, auf welche Spalte der Umfragedaten zugegriffen wird (in den entsprechenden Spalten
        # stehen die entsprechenden Werte wie eine entsprechende Unterrichtsberscgiebung in Bezug auf
        # die Auswirkungen auf Schüler, die selbstaktiv zur Schule kommen, bepunktet wird
        def get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn):
            if verschiebung_unterrichtsbeginn <= -30:
                return 70
            elif -30 < verschiebung_unterrichtsbeginn <= -20:
                return 71
            elif -20 < verschiebung_unterrichtsbeginn <= -5:
                return 72
            elif -5 < verschiebung_unterrichtsbeginn < 5:
                return 73
            elif 5 <= verschiebung_unterrichtsbeginn <= 10:
                return 74
            elif 10 < verschiebung_unterrichtsbeginn <= 20:
                return 75
            elif 20 < verschiebung_unterrichtsbeginn <= 30:
                return 76
            else:
                return 77

        # Abhängigkeit des Unterrichtsbeginns
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen mit dem identischen Unterrichtsbeginn
            # weiter berücksichtigt werden
            einfluss_unterrichtsbeginn_selbstaktiv = daten_befragung.query('Schulbeginn_Stunde1_7Uhr == @merkmale[0]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            if einfluss_unterrichtsbeginn_selbstaktiv.shape[1] > i:
                mean_value = einfluss_unterrichtsbeginn_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit der Schüleranzahl
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen in der identischen Schüleranzahlklasse
            # weiter berücksichtigt werden
            einfluss_schueleranzahl_selbstaktiv = daten_befragung.query('Schueleranzahl == @merkmale[1]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            if einfluss_schueleranzahl_selbstaktiv.shape[1] > i:
                mean_value = einfluss_schueleranzahl_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit der Betreuung morgens
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung bieten weiter berücksichtigt werden
            einfluss_betreuung_morgens_selbstaktiv = daten_befragung.query('Betreuung_vor_Unterricht == @merkmale[2]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_morgens_selbstaktiv.shape[1] > i:
                mean_value = einfluss_betreuung_morgens_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit der Betreuung mittags
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Betreuung bzw. keine
            # Betreuung nach Unterrichtsende bieten, weiter berücksichtigt werden
            einfluss_betreuung_mittags_selbstaktiv = daten_befragung.query('Betreuung_nach_Unterricht == @merkmale[3]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            if einfluss_betreuung_mittags_selbstaktiv.shape[1] > i:
                mean_value = einfluss_betreuung_mittags_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit Mensa
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls eine Mensa bzw. keine
            # Mensa haben, weiter berücksichtigt werden
            einfluss_mensa_selbstaktiv = daten_befragung.query('Mensa == @merkmale[4]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            if einfluss_mensa_selbstaktiv.shape[1] > i:
                mean_value = einfluss_mensa_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit davon, ob Lehrer auch an anderen Schulen unterrichten
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Lehrer haben, die an
            # anderen Schulen unterrichten bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_lehrer_selbstaktiv = daten_befragung.query('Lehrer_an_anderer_Schule == @merkmale[5]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            if einfluss_lehrer_selbstaktiv.shape[1] > i:
                mean_value = einfluss_lehrer_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Abhängigkeit davon, ob Schüler auch Fächer an anderen Schulen besuchen
        for idx, merkmale in enumerate(merkmale_alle_schulen):
            verschiebung_unterrichtsbeginn = verschiebungen_unterrichtsbeginn[idx]
            # die Daten werden so gefiltert, dass nur noch Datensätze von Schulen die ebenfalls Schüler haben, die an
            # Fächer an anderen Schulen besuchen bzw. dies nicht haben, weiter berücksichtigt werden
            einfluss_schüler_selbstaktiv = daten_befragung.query('Schueler_an_anderer_Schule == @merkmale[6]')

            # i entscheidet welche Spalte der Befragungsdaten ausgelesen werden
            i = get_index_selbstaktive_schüler(verschiebung_unterrichtsbeginn)

            if einfluss_schüler_selbstaktiv.shape[1] > i:
                mean_value = einfluss_schüler_selbstaktiv.iloc[:, i].mean()
                akzeptanzeinzelwerte_selbstaktive_schüler.append(mean_value)
            else:
                akzeptanzeinzelwerte_selbstaktive_schüler.append(None)

        # Bereinigung der Listen
        akzeptanzeinzelwerte_leistung = [x for x in akzeptanzeinzelwerte_leistung
                                         if x is not None and not numpy.isnan(x)]
        akzeptanzeinzelwerte_betreuungspersonal = [x for x in akzeptanzeinzelwerte_betreuungspersonal
                                                   if x is not None and not numpy.isnan(x)]
        akzeptanzeinzelwerte_kinderbetreuung = [x for x in akzeptanzeinzelwerte_kinderbetreuung
                                                if x is not None and not numpy.isnan(x)]
        akzeptanzeinzelwerte_selbstaktive_schüler = [x for x in akzeptanzeinzelwerte_selbstaktive_schüler
                                                     if x is not None and not numpy.isnan(x)]

        # Berechnung der finalen Mittelwerte
        einfluss_leistungen_finaler_wert = statistics.mean(akzeptanzeinzelwerte_leistung)
        einfluss_betreuungspersonal_finaler_wert = statistics.mean(akzeptanzeinzelwerte_betreuungspersonal)
        einfluss_kinderbetreuung_finaler_wert = statistics.mean(akzeptanzeinzelwerte_kinderbetreuung)
        einfluss_selbstaktive_schüler_finaler_wert = statistics.mean(akzeptanzeinzelwerte_selbstaktive_schüler)

        # Bestimmung des Gesamtmittelswerts aus den Mittelwerten der Kategorien
        gesamtmittelwert_eine_variante = statistics.mean([einfluss_leistungen_finaler_wert,
                                                          einfluss_betreuungspersonal_finaler_wert,
                                                          einfluss_kinderbetreuung_finaler_wert,
                                                          einfluss_selbstaktive_schüler_finaler_wert])
        print("Variante", combination)
        print("Auswirkungen auf Leistungen Gesamtwert:",
              einfluss_leistungen_finaler_wert)
        print("Auswirkungen auf akzeptanzeinzelwerte_betreuungspersonal Gesamtwert:",
              einfluss_betreuungspersonal_finaler_wert)
        print("Auswirkungen auf Kinderbetreuung Gesamtwert:",
              einfluss_kinderbetreuung_finaler_wert)
        print("Auswirkungen auf Selbstaktivität Gesamtwert:",
              einfluss_selbstaktive_schüler_finaler_wert)
        print("Gesamtmittelwert:", gesamtmittelwert_eine_variante)

        gesamtmittelwerte_akzeptanzbewertung.append(gesamtmittelwert_eine_variante)

    # zurückgegeben wird eine Liste mit den Gesamtmittelwerten für alle untersuchten Varianten
    return gesamtmittelwerte_akzeptanzbewertung
