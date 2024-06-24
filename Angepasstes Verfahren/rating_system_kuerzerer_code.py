import pandas as pd
import statistics
import numpy as np

# Daten einlesen
d = pd.read_csv('Daten_rating_system.csv', sep=';')

# Testkombination
Var = [50, 40, 30, 20, 10, 5, 10] # Variante, die bepunktet werden soll
Startzeiten = [20, 30, 60, 60, 10, 25, 40] #aktuelle Unterrichtszeiten

# Berechnung der zeitlichen Verschiebung
s_change_values = [v - s for v, s in zip(Var, Startzeiten)]

#Charakteristika der Schulen (Schultyp(Stufe1-5), aktueller Schulbeginn_Min.nach7, Schülerzahl (Klasse),Betreuungsangebot_morgens,Betreuungsangebot_mittags,Mensa,Lehrer(andere Schule), Schüler (andere Schule))

merkmalsliste = [
    [3, 60, 2, 0, 0, 1, 1, 1],
    [3, 45, 4, 1, 0, 0, 1, 1],
    [3, 30, 2, 1, 1, 1, 1, 1],
    [3, 60, 4, 0, 0, 0, 1, 1],
    [2, 20, 2, 0, 0, 1, 0, 0],
    [4, 50, 3, 0, 0, 1, 1, 0],
    [5, 60, 2, 0, 0, 1, 1, 1]
]

# Bestimmung des Index i basierend auf s_change
def get_index(s_change):
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

# Funktion zur Berechnung des Mittelwerts der Leistungen für ein Merkmal
def calculate_mean_performance(query_str, column_idx):
    Leistungen = []
    for idx, merkmale in enumerate(merkmalsliste):
        s_change = s_change_values[idx]
        data = d.query(query_str.format(merkmale))
        i = get_index(s_change)
        if data.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
            mean_value = data.iloc[:, i].mean()
            Leistungen.append(mean_value)
        else:
            Leistungen.append(None)
    return Leistungen

# Berechnungen für verschiedene Merkmale
Leistungen = []
queries = [
    'Schultyp == {}[0]',
    'Schulbeginn_Stunde1_7Uhr == {}[1]',
    'Schueleranzahl == {}[2]',
    'Betreuung_vor_Unterricht == {}[3]',
    'Betreuung_nach_Unterricht == {}[4]',
    'Mensa == {}[5]',
    'Lehrer_an_anderer_Schule == {}[6]',
    'Schueler_an_anderer_Schule == {}[7]'
]

for query in queries:
    Leistungen.extend(calculate_mean_performance(query, get_index))

# Filterung und Berechnung des finalen Werts
Leistungen = [x for x in Leistungen if x is not None and not np.isnan(x)]
Leistungen_finaler_wert = statistics.mean(Leistungen)
print("Auswirkungen auf Leistungen Gesamtwert", Leistungen_finaler_wert)
