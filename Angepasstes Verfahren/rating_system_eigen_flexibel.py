import csv
import pandas
import statistics
import numpy
d=pandas.read_csv('Daten_rating_system.csv', sep=';')
Gesamtmittelwerte =[]

#Bestimmung der zeitlichen Verschebung jeder Schule
# händisch eingegebene Testkombination
Var = [
    [15, 25, 10, 40, 30, 45, 55]]

Startzeiten_aktuell = []
Haltestellennummern= []
Spätere_Ankünfte = []
anzahl_schulen= int(input("Wie viele Schulen gibt es im Untersuchungsgebiet? "))
for i in range(anzahl_schulen): # Beim Zusammenführen wieder ohne aktuell, damit nur einmal werte eingegben werden müssen
    Startzeit_aktuell = int(input(f"Um wie viele Minuten nach 7 startet Schule {i+1}"))
    Startzeiten_aktuell.append(Startzeit_aktuell)
    Haltestellennummer= int(input(f"Welche Haltestelle nutzt Schule {i+1}"))
    Haltestellennummern.append(Haltestellennummer)
    Spätere_Ankunft=int(input(f"Muss der Schulstart an Schule {i+1} später liegen, wie an der fühesten Schule, die diese Haltestelle nutzt, weil sie als Anschlussfahrt angefahren wird oder der Fußweg länger ist. Falls ja hier Minutenanzahl angeben, ansonsten 0 eingeben"))
    Spätere_Ankünfte.append(Spätere_Ankunft)

print(Startzeiten_aktuell)
print(Haltestellennummern)
print(Spätere_Ankünfte)

# Charakteristika der Schulen , aktueller Schulbeginn_Min.nach7, Schülerzahl (Klasse),Betreuungsangebot_morgens,Betreuungsangebot_mittags,Mensa,Lehrer(andere Schule), Schüler (andere Schule))

merkmalsliste = []
for i in range (anzahl_schulen):
    s_merkmale = []
    Startzeit_aktuell = int(input(f"Um wie viele Minuten nach 7 startet Schule {i + 1}"))
    s_merkmale.append(Startzeit_aktuell)
    Schüleranzahl = int(input(f"Wie viele Schüler hat Schule {i + 1}"))
    if Schüleranzahl < 300:
        s_merkmale.append(1)
    elif Schüleranzahl >= 300 and Schüleranzahl<500:
        s_merkmale.append(2)
    elif Schüleranzahl >= 500 and Schüleranzahl<700:
        s_merkmale.append(3)
    elif Schüleranzahl >= 700 and Schüleranzahl<900:
        s_merkmale.append(4)
    elif Schüleranzahl >= 900 and Schüleranzahl<1100:
        s_merkmale.append(5)
    else:
        s_merkmale.append(6)
    Betreuungangebot_morgens = input(f"Gibt es ein Betreuungsangebot morgens vor Unterrichtsbeginn an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n" )
    if Betreuungangebot_morgens =="j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    Betreuungangebot_mittags = input(f"Gibt es ein Betreuungsangebot mittags nach Unterrichtsende an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n")
    if Betreuungangebot_mittags == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Mensa = input(f"Gibt es eine Mensa an Schule {i + 1} Wenn ja - tippe j , wenn nein tippe n")
    if Mensa == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Lehrer_andere_Schule = input(f"Gibt es  an Schule {i + 1} Lehrer, die auch an anderen Schulen unterrichten? Wenn ja - tippe j , wenn nein tippe n")
    if Lehrer_andere_Schule == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    Schüler_andere_Schule = input(f"Gibt es  an Schule {i + 1} Schüler, die Fächer an anderen Schulen besuchen? Wenn ja - tippe j , wenn nein tippe n")
    if Schüler_andere_Schule == "j":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)

    merkmalsliste.append(s_merkmale)
print(merkmalsliste)


for Variante in Var:
    s_change_values = []
    for i in range(anzahl_schulen):
        index = Haltestellennummern[i]
        s_change = Variante[index-1] + Spätere_Ankünfte[i] - Startzeiten_aktuell[i]
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

    #Ahängigkeit Lehrer an anderen Schule
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Lehrer_Leistungen = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

        i = get_index_Leistungen(s_change)

        if Lehrer_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Lehrer_Leistungen.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    #Ahängigkeit Schüler an anderen Schule
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

        if Unterrichtsbeginn_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Unterrichtsbeginn_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Schüleranzahl
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Schueleranzahl_Betreuungspersonal = d.query('Schueleranzahl == @merkmale[1]')

        i = get_index_Betreuungspersonal(s_change)

        if Schueleranzahl_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Schueleranzahl_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung morgens
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_morgens_Betreuungspersonal = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

        i = get_index_Betreuungspersonal(s_change)

        if Betreuung_morgens_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Betreuungspersonal.iloc[:, i].mean()
            Betreuungspersonal.append(mean_value)
        else:
            Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Ahängigkeit der Betreeung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Betreuungspersonal = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Betreuungspersonal(s_change)

        if Betreuung_mittags_Betreuungspersonal.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

        if Schueleranzahl_Kinderbetreuung.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

        if Unterrichtsbeginn_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

        if Betreuung_morgens_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = Betreuung_morgens_Selbstaktiv.iloc[:, i].mean()
            Selbstaktiv.append(mean_value)
        else:
            Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

    # Abhängigkeit der Betreuung mittags
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        Betreuung_mittags_Selbstaktiv = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

        i = get_index_Selbstaktiv(s_change)

        if Betreuung_mittags_Selbstaktiv.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

    print("Leistungen"+str(Leistungen))
    print("Betreuungspersonal"+str(Betreuungspersonal))
    print("Kinderbetreuung"+str(Kinderbetreuung))
    print("Selbstaktiv"+str(Selbstaktiv))
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

    Gesamtmittelwert = statistics.mean([Leistungen_finaler_wert, Betreuungspersonal_finaler_wert, Kinderbetreuung_finaler_wert, Selbstaktiv_finaler_wert])
    print ("Variante",Variante)
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