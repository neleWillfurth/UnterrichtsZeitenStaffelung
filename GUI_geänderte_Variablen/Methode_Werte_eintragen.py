def Werte_eintragen(entry_anzahl_schulen, aktueller_unterrichtsbeginn_alle_Schulen_entries, schueleranzahlen, check_var_liste1, check_var_liste2, check_var_liste3,
                    check_var_liste4, check_var_liste5, merkmalsliste):

    anzahl_Schulen = int(entry_anzahl_schulen.get())
    aktueller_unterrichtsbeginn_alle_Schulen_entries_int = [int(entry.get()) for entry in aktueller_unterrichtsbeginn_alle_Schulen_entries]
    Schüleranzahlen_int = [int(entry.get()) for entry in schueleranzahlen]
    for i in range(anzahl_Schulen):
        s_merkmale = [aktueller_unterrichtsbeginn_alle_Schulen_entries_int[i]]

        if Schüleranzahlen_int[i] < 300:
            s_merkmale.append(1)
        elif Schüleranzahlen_int[i] < 500:
            s_merkmale.append(2)
        elif Schüleranzahlen_int[i] < 700:
            s_merkmale.append(3)
        elif Schüleranzahlen_int[i] < 900:
            s_merkmale.append(4)
        elif Schüleranzahlen_int[i] < 1100:
            s_merkmale.append(5)
        else:
            s_merkmale.append(6)

        if check_var_liste1[i].get() == "1":
            s_merkmale.append(1)
        else:
            s_merkmale.append(0)
        if check_var_liste2[i].get() == "1":
            s_merkmale.append(1)
        else:
            s_merkmale.append(0)
        if check_var_liste3[i].get() == "1":
            s_merkmale.append(1)
        else:
            s_merkmale.append(0)
        if check_var_liste4[i].get() == "1":
            s_merkmale.append(1)
        else:
            s_merkmale.append(0)
        if check_var_liste5[i].get() == "1":
            s_merkmale.append(1)
        else:
            s_merkmale.append(0)
        merkmalsliste.append(s_merkmale)

    return merkmalsliste
