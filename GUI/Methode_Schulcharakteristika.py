import tkinter as tk
from tkinter import ttk

def Schulcharakteristika_eingeben(notebook, tab2, entry_Anzahl_Schulen, scrollable_tab2,
                                 aktueller_unterrichtsbeginn_alle_Schulen_entries, Haltestellennummern, Spaetere_Ankuenfte,
                                 Weg_Bus_Schule, Schüleranzahlen, checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3,
                                 check_var_liste4, check_var_liste5):



    anzahl_Schulen = int(entry_Anzahl_Schulen.get())
    check_var_liste1.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste2.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste3.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste4.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste5.extend([tk.StringVar() for _ in range(anzahl_Schulen)])

    for i in range(anzahl_Schulen):
        label_Schule = ttk.Label(scrollable_tab2.scrollable_frame, text=f'Schule {i + 1}', font=("Helvetica",12, "bold"))
        label_Schule.grid()

        label_aktueller_Schulbeginn1 = ttk.Label(scrollable_tab2.scrollable_frame, text="Aktueller Unterrrichtsbeginn in Minuten nach 7 ", font=("Helvetica",10))
        label_aktueller_Schulbeginn1.grid()
        label_aktueller_Schulbeginn2 = ttk.Label(scrollable_tab2.scrollable_frame,
                                                 text="(Als Vielfaches von 5 angeben)", font=("Helvetica", 8))
        label_aktueller_Schulbeginn2.grid()
        entry_aktueller_Schulbeginn = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_aktueller_Schulbeginn.grid()
        aktueller_unterrichtsbeginn_alle_Schulen_entries.append(entry_aktueller_Schulbeginn)

        label_Haltestellennutzung1 = tk.Label(scrollable_tab2.scrollable_frame, text="Haltestellennummer",font=("Helvetica",10))
        label_Haltestellennutzung1.grid()
        label_Haltestellennutzung2 = tk.Label(scrollable_tab2.scrollable_frame,
                                             text="(Schulen, die dieselbe Haltestelle nutzen oder direkt nacheinander angefahren werden, erhalten"
                                                  "die selbe Nummer)", font=("Helvetica", 8))
        label_Haltestellennutzung2.grid()
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Haltestellennutzung.grid()
        Haltestellennummern.append(entry_Haltestellennutzung)

        label_spätere_Ankunft1 = tk.Label(scrollable_tab2.scrollable_frame, text=f"Bei Anschlussfahrt die Fahrzeit von der früheren zu dieser Haltestelle eintragen", font=("Helvetica",10))
        label_spätere_Ankunft1.grid()
        label_spätere_Ankunft2 = tk.Label(scrollable_tab2.scrollable_frame, text=" (Als Vielfaches von 5 angeben, ansonsten 0 eintragen)",
                                          font=("Helvetica", 8))
        label_spätere_Ankunft2.grid()
        entry_spätere_Ankunft = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_spätere_Ankunft.grid()
        Spaetere_Ankuenfte.append(entry_spätere_Ankunft)

        label_Weg_Bus_Schule1 = tk.Label(scrollable_tab2.scrollable_frame, text=f"Benötigte Zeit zwischen Busankunft und Unterichtsbeginn",font=("Helvetica",10))
        label_Weg_Bus_Schule1.grid()
        label_Weg_Bus_Schule2 = tk.Label(scrollable_tab2.scrollable_frame,
                                         text=f"(Als Vielfaches von 5 angeben)", font=("Helvetica", 8))
        label_Weg_Bus_Schule2.grid()
        entry_Weg_Bus_Schule = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Weg_Bus_Schule.grid()
        Weg_Bus_Schule.append(entry_Weg_Bus_Schule)

        label_Schüleranzahl = ttk.Label(scrollable_tab2.scrollable_frame, text="Anzahl Schüler",font=("Helvetica",10))
        label_Schüleranzahl.grid()
        Schüleranzahl = ttk.Entry(scrollable_tab2.scrollable_frame)
        Schüleranzahl.grid()
        Schüleranzahlen.append(Schüleranzahl)

        label_Betreuungsangebot_morgens = ttk.Label(scrollable_tab2.scrollable_frame, text="Betreuungsangebot vor Unterrichtsbeginn?",font=("Helvetica",10))
        label_Betreuungsangebot_morgens.grid()
        checkbutton_Betreuung_morgens = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste1[i])
        checkbutton_Betreuung_morgens.grid()
        checkbuttons.append(checkbutton_Betreuung_morgens)

        label_Betreuungsangebot_mittags = ttk.Label(scrollable_tab2.scrollable_frame, text="Betreuungsangebot nach Unterrichtsende?",font=("Helvetica",10))
        label_Betreuungsangebot_mittags.grid()
        checkbutton_Betreuung_mittags = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste2[i])
        checkbutton_Betreuung_mittags.grid()
        checkbuttons.append(checkbutton_Betreuung_mittags)

        label_Mensa = ttk.Label(scrollable_tab2.scrollable_frame, text="Mensa vorhanden?",font=("Helvetica",10))
        label_Mensa.grid()
        checkbutton_Mensa = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste3[i])
        checkbutton_Mensa.grid()
        checkbuttons.append(checkbutton_Mensa)

        label_andere_Lehrer = ttk.Label(scrollable_tab2.scrollable_frame, text="Lehrer, die  auch an anderen Schulen unterrichten?",font=("Helvetica",10))
        label_andere_Lehrer.grid()
        checkbutton_andere_Lehrer = ttk.Checkbutton(scrollable_tab2.scrollable_frame,  variable=check_var_liste4[i])
        checkbutton_andere_Lehrer.grid()
        checkbuttons.append(checkbutton_andere_Lehrer)

        label_andere_Schüler = ttk.Label(scrollable_tab2.scrollable_frame, text="Schüler, die auch Fächer an anderen Schulen besuchen?",font=("Helvetica",10))
        label_andere_Schüler.grid()
        checkbutton_andere_Schüler = ttk.Checkbutton(scrollable_tab2.scrollable_frame,  variable=check_var_liste5[i])
        checkbutton_andere_Schüler.grid()
        checkbuttons.append(checkbutton_andere_Schüler)
