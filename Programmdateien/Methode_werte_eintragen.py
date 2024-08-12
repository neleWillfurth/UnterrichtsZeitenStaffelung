def werte_eintragen(entry_anzahl_schulen, aktueller_unterrichtsbeginn_alle_schulen, schüleranzahlen, check_var_liste1,
                    check_var_liste2, check_var_liste3, check_var_liste4, check_var_liste5, merkmale_alle_schulen):
    """
    alle eingegebenen Schulcharakteristika werden je Schule in einer Liste gespeichert, welche wiederum in einer
    Liste zusammengeführt werden

    :param entry_anzahl_schulen: bestimmt wie häufig, die for-Schleife durchlaufen wird, um dies für jede Schule einmal
    durchzuführen
    :param aktueller_unterrichtsbeginn_alle_schulen: eines der Schulcharakteristika
    :param schüleranzahlen: eines der Schulcharakteristika (wird in Klassen 1-6 zusammengefasst)
    :param check_var_liste1: beinhaltet, die Eingaben je Schule für den ersten Checkbutton, ob die Schule eine Betreuung
    vor Unterrichtsbeginn anbietet
    :param check_var_liste2: beinhaltet, die Eingaben je Schule für den zweiten Checkbutton, ob die Schule eine
    Betreuung nach Unterrichtsende anbietet
    :param check_var_liste3: beinhaltet, die Eingaben je Schule für den dritten Checkbutton, ob die Schule über eine
    Mensa verfügt
    :param check_var_liste4: beinhaltet, die Eingaben je Schule für den vierten Checkbutton, ob die Schule Lehrer hat,
    die auch an anderen Schulen unterrichten
    :param check_var_liste5: beinhaltet, die Eingaben je Schule für den fünften Checkbutton, ob die Schule Schüler hat,
    die für einzelne Fächer andere Schulen besuchen
    :param merkmale_alle_schulen: speichert die alle Schulcharakteristiken aller Schulen als eine Liste von Listen
    :return: merkmale_alle_schulen
    """

    for i in range(int(entry_anzahl_schulen.get())):
        # für jede Schule wird eine neue Liste erstellt, um die Merkmale darin zu speichern, je Liste ist der erste Wert
        # der aktuelle Schulbeginn
        merkmale_eine_schule = [int(aktueller_unterrichtsbeginn_alle_schulen[i].get())]
        # die Schüleranzahl wird als Klasse zwischen 1 und 6 der Liste merkmale_eine_schule hinzugefügt
        schüleranzahl = int(schüleranzahlen[i].get())

        if schüleranzahl < 300:
            merkmale_eine_schule.append(1)
        elif schüleranzahl < 500:
            merkmale_eine_schule.append(2)
        elif schüleranzahl < 700:
            merkmale_eine_schule.append(3)
        elif schüleranzahl < 900:
            merkmale_eine_schule.append(4)
        elif schüleranzahl < 1100:
            merkmale_eine_schule.append(5)
        else:
            merkmale_eine_schule.append(6)

        # Je nachdem, ob für eine Schule ein entsprechender Button ausgewählt wurde, wird eine 1 (trifft zu) oder eine
        # 0 (trifft nicht zu) der Liste merkmale_eine_schule hinzugefügt
        if check_var_liste1[i].get() == "1":
            merkmale_eine_schule.append(1)
        else:
            merkmale_eine_schule.append(0)
        if check_var_liste2[i].get() == "1":
            merkmale_eine_schule.append(1)
        else:
            merkmale_eine_schule.append(0)
        if check_var_liste3[i].get() == "1":
            merkmale_eine_schule.append(1)
        else:
            merkmale_eine_schule.append(0)
        if check_var_liste4[i].get() == "1":
            merkmale_eine_schule.append(1)
        else:
            merkmale_eine_schule.append(0)
        if check_var_liste5[i].get() == "1":
            merkmale_eine_schule.append(1)
        else:
            merkmale_eine_schule.append(0)

        # die Listen für jede Schule werden der Gesamtliste hinzugefügt
        merkmale_alle_schulen.append(merkmale_eine_schule)

    return merkmale_alle_schulen
