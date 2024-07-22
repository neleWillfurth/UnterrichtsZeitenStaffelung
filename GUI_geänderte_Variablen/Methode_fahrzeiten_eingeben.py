from tkinter import ttk


def fahrzeiten_eintragen(entry_anzahl_haltestellen, anzahl_busse_je_haltestelle, scrollable_tab4,
                         entry_fahrzeiten, fahrzeiten):
    """
    Eingabe der Fahrzeit für alle möglichen Fahrtrelationen
    :param entry_anzahl_haltestellen: Anzahl Haltestellen im Untersuchungsgebiet
    :param anzahl_busse_je_haltestelle: je Haltestelle wird angegebenen, wie viele Busse dort hinfahren
    :param scrollable_tab4: tab in welchem die Felder dargestellt werden
    :param entry_fahrzeiten: Liste der Eingabewerte der einzelnen Fahrzeiten (Hilfliste, um mit entry-Feldern
    umzugehen)
    :param fahrzeiten: wird später Liste mit allen Fahrzeiten - jetzt Zwischenspeicher für 0 (Busfahrt ist zwischen
    unterschiedlichem Start- und Zielpunkt) und 100000000 (Busfahrt ist zwischen identischem Start- und Zielpunkt)
    """
    # für jede Fahrtrelation zwischen startpunkt und zielpunkt über alle Routenstartpunkte zum zielpunkt muss die
    # Fahrzeit eingetragen werden
    for startpunkt in range(int(entry_anzahl_haltestellen.get())):
        for zielpunkt in range(int(entry_anzahl_haltestellen.get())):
            for routenstart in range(int(anzahl_busse_je_haltestelle[zielpunkt].get())):
                # das Eintragen einer Fahrzeit ist nur erforderlich, wenn Start- und Zielpunkt unterschiedlich sind
                if startpunkt != zielpunkt:
                    label_fahrzeit = ttk.Label(scrollable_tab4.scrollable_frame,
                                               text=f"Fahrzeit von Haltestelle {startpunkt + 1} "
                                                    f"über den Routenstart {routenstart + 1} Haltestelle"
                                                    f" {zielpunkt + 1} ", font=("Helvetica", 10))
                    label_fahrzeit.grid(column=0)
                    entry_fahrzeit = ttk.Entry(scrollable_tab4.scrollable_frame)
                    entry_fahrzeit.grid(column=0)
                    # die eingegebenen Fahrzeiten werden in entry_fahrzeiten
                    entry_fahrzeiten.append(entry_fahrzeit)
                    # für alle Relationen bei denen start- und zielpunkt identisch sind, wird in der Liste fahrzeiten
                    # eine 0 ergänzt, um diese später systematisch zu ersetzten
                    fahrzeiten.append(0)
                else:
                    # sind start- und zielpunkt identisch wird dort eine sehr hohe Zahl als Fahrzeit eingegeben, um
                    # sicherzugehen, dass hier nie eine Wiedernutzung geplant wird, da start- und zielpunkt identisch
                    # sind
                    fahrzeiten.append(100000000)
