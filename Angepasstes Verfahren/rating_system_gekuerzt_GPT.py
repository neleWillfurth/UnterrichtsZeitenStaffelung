import csv
import pandas
import statistics
import numpy

# Daten einlesen
d = pandas.read_csv('Daten_rating_system.csv', sep=';')

# Bestimmung der zeitlichen Verschiebung jeder Schule
Var = [50,40,30,20,10,5,10]
Startzeiten = [20,30,60,60,10,25,40]
s_change_values = [Var[i] - Startzeiten[i] for i in range(len(Var))]

# #Charakteristika der Schulen (Schultyp(Stufe1-5), aktueller Schulbeginn_Min.nach7, Schülerzahl (Klasse),Betreuungsangebot_morgens,Betreuungsangebot_mittags,Mensa,Lehrer(andere Schule), Schüler (andere Schule))
merkmalsliste = [
    [1, 60, 2, 0, 0, 1, 1, 1],
    [2, 45, 4, 1, 0, 0, 1, 1],
    [3, 30, 2, 1, 1, 1, 1, 1],
    [3, 60, 4, 0, 0, 0, 1, 1],
    [2, 20, 2, 0, 0, 1, 0, 0],
    [4, 50, 3, 0, 0, 1, 1, 0],
    [5, 60, 2, 0, 0, 1, 1, 1]
]

def get_index(s_change, offset=14):
    if s_change <= -30:
        return offset
    elif -30 < s_change <= -20:
        return offset + 1
    elif -20 < s_change <= -5:
        return offset + 2
    elif -5 < s_change < 5:
        return offset + 3
    elif 5 <= s_change <= 10:
        return offset + 4
    elif 10 < s_change <= 20:
        return offset + 5
    elif 20 < s_change <= 30:
        return offset + 6
    elif 30 < s_change:
        return offset + 7

def calculate_mean_performance(query_str, offset=14):
    result = []
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        data = d.query(query_str.format(merkmale))
        i = get_index(s_change, offset)
        if data.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = data.iloc[:, i].mean()
            result.append(mean_value)
        else:
            result.append(None)
    return result

# Berechnung der Leistungen
Leistungen = calculate_mean_performance('Schultyp == @merkmale[0]')
Leistungen.extend(calculate_mean_performance('Schulbeginn_Stunde1_7Uhr == @merkmale[1]'))
Leistungen.extend(calculate_mean_performance('Schueleranzahl == @merkmale[2]'))
Leistungen.extend(calculate_mean_performance('Betreuung_vor_Unterricht == @merkmale[3]'))
Leistungen.extend(calculate_mean_performance('Betreuung_nach_Unterricht == @merkmale[4]'))
Leistungen.extend(calculate_mean_performance('Mensa == @merkmale[5]'))
Leistungen.extend(calculate_mean_performance('Lehrer_an_anderer_Schule == @merkmale[6]'))
Leistungen.extend(calculate_mean_performance('Schueler_an_anderer_Schule == @merkmale[7]'))

# Berechnung des Betreuungspersonals
Betreuungspersonal = calculate_mean_performance('Schultyp == @merkmale[0]', offset=28)
Betreuungspersonal.extend(calculate_mean_performance('Schulbeginn_Stunde1_7Uhr == @merkmale[1]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Schueleranzahl == @merkmale[2]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Betreuung_vor_Unterricht == @merkmale[3]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Betreuung_nach_Unterricht == @merkmale[4]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Mensa == @merkmale[5]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Lehrer_an_anderer_Schule == @merkmale[6]', offset=28))
Betreuungspersonal.extend(calculate_mean_performance('Schueler_an_anderer_Schule == @merkmale[7]', offset=28))

# Berechnung der Kinderbetreuung
Kinderbetreuung = calculate_mean_performance('Schultyp == @merkmale[0]', offset=40)
Kinderbetreuung.extend(calculate_mean_performance('Schulbeginn_Stunde1_7Uhr == @merkmale[1]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Schueleranzahl == @merkmale[2]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Betreuung_vor_Unterricht == @merkmale[3]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Betreuung_nach_Unterricht == @merkmale[4]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Mensa == @merkmale[5]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Lehrer_an_anderer_Schule == @merkmale[6]', offset=40))
Kinderbetreuung.extend(calculate_mean_performance('Schueler_an_anderer_Schule == @merkmale[7]', offset=40))

# Berechnung der Selbstaktivität
Selbstaktiv = calculate_mean_performance('Schultyp == @merkmale[0]', offset=70)
Selbstaktiv.extend(calculate_mean_performance('Schulbeginn_Stunde1_7Uhr == @merkmale[1]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Schueleranzahl == @merkmale[2]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Betreuung_vor_Unterricht == @merkmale[3]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Betreuung_nach_Unterricht == @merkmale[4]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Mensa == @merkmale[5]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Lehrer_an_anderer_Schule == @merkmale[6]', offset=70))
Selbstaktiv.extend(calculate_mean_performance('Schueler_an_anderer_Schule == @merkmale[7]', offset=70))



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

print("Auswirkungen auf Leistungen Gesamtwert:", Leistungen_finaler_wert)
print("Auswirkungen auf Betreuungspersonal Gesamtwert:", Betreuungspersonal_finaler_wert)
print("Auswirkungen auf Kinderbetreuung Gesamtwert:", Kinderbetreuung_finaler_wert)
print("Auswirkungen auf Selbstaktivität Gesamtwert:", Selbstaktiv_finaler_wert)
print("Gesamtmittelwert:", Gesamtmittelwert)
