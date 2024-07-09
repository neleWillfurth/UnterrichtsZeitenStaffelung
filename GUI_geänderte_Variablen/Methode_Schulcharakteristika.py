import tkinter as tk
from tkinter import ttk


def schulcharakteristika_eingeben(entry_anzahl_schulen, scrollable_tab2,
                                  aktueller_unterrichtsbeginn_alle_schulen_entries, haltestellennummern_entries,
                                  versatz_ankunft_durch_anschlussfahrt_entries,
                                  wegdauer_haltestelle_schule_entries,
                                  schueleranzahlen, checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3,
                                  check_var_liste4, check_var_liste5):
    """
    Berechnung der Schulcharakteristika unter Berückschtiugngn abalblalalba


    :param entry_anzahl_schulen:
    :param scrollable_tab2:
    :param aktueller_unterrichtsbeginn_alle_schulen_entries:
    :param haltestellennummern_entries:
    :param versatz_ankunft_durch_anschlussfahrt_entries:
    :param wegdauer_haltestelle_schule_entries:
    :param schueleranzahlen:
    :param checkbuttons:
    :param check_var_liste1: aasdasdasdasd
    :param check_var_liste2:
    :param check_var_liste3:
    :param check_var_liste4:
    :param check_var_liste5:
    :return: Kein Rückgabewert, die übergebenen Variablen werden direkt geändert
    """

    anzahl_Schulen = int(entry_anzahl_schulen.get())
    check_var_liste1.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste2.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste3.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste4.extend([tk.StringVar() for _ in range(anzahl_Schulen)])
    check_var_liste5.extend([tk.StringVar() for _ in range(anzahl_Schulen)])

    for i in range(anzahl_Schulen):
        label_Schule = ttk.Label(scrollable_tab2.scrollable_frame, text=f'Schule {i + 1}',
                                 font=("Helvetica", 12, "bold"))
        label_Schule.grid()

        label_aktueller_schulbeginn1 = ttk.Label(scrollable_tab2.scrollable_frame,
                                                 text="Aktueller Unterrrichtsbeginn in Minuten nach 7 ",
                                                 font=("Helvetica", 10))
        label_aktueller_schulbeginn1.grid()
        label_aktueller_schulbeginn2 = ttk.Label(scrollable_tab2.scrollable_frame,
                                                 text="(Als Vielfaches von 5 angeben)", font=("Helvetica", 8))
        label_aktueller_schulbeginn2.grid()
        entry_aktueller_Schulbeginn = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_aktueller_Schulbeginn.grid()
        aktueller_unterrichtsbeginn_alle_schulen_entries.append(entry_aktueller_Schulbeginn)

        label_haltestellennutzung1 = tk.Label(scrollable_tab2.scrollable_frame, text="Haltestellennummer",
                                              font=("Helvetica", 10))
        label_haltestellennutzung1.grid()
        label_haltestellennutzung2 = tk.Label(scrollable_tab2.scrollable_frame,
                                              text="(Schulen, die dieselbe Haltestelle nutzen oder direkt nacheinander "
                                                   "angefahren werden, erhalten die selbe Nummer)",
                                              font=("Helvetica", 8))
        label_haltestellennutzung2.grid()
        entry_anzahl_busse_pro_haltestelle = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_anzahl_busse_pro_haltestelle.grid()
        haltestellennummern_entries.append(entry_anzahl_busse_pro_haltestelle)

        label_spaetere_ankunft1 = tk.Label(scrollable_tab2.scrollable_frame, text=f"Bei Anschlussfahrt die Fahrzeit von"
                                                                                  f" der früheren zu dieser Haltestelle"
                                                                                  f" eintragen", font=("Helvetica", 10))
        label_spaetere_ankunft1.grid()
        label_spaetere_ankunft2 = tk.Label(scrollable_tab2.scrollable_frame, text="(Als Vielfaches von 5 angeben, "
                                                                                  "ansonsten 0 eintragen)",
                                           font=("Helvetica", 8))
        label_spaetere_ankunft2.grid()
        entry_spätere_Ankunft = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_spätere_Ankunft.grid()
        versatz_ankunft_durch_anschlussfahrt_entries.append(entry_spätere_Ankunft)

        label_wegdauer_haltestelle_schule_entries1 = tk.Label(scrollable_tab2.scrollable_frame,
                                                              text=f"Benötigte Zeit zwischen Busankunft und "
                                                                   f"Unterichtsbeginn",
                                                              font=("Helvetica", 10))
        label_wegdauer_haltestelle_schule_entries1.grid()
        label_wegdauer_haltestelle_schule_entries2 = tk.Label(scrollable_tab2.scrollable_frame,
                                         text=f"(Als Vielfaches von 5 angeben)", font=("Helvetica", 8))
        label_wegdauer_haltestelle_schule_entries2.grid()
        entry_wegdauer_haltestelle_schule_entries = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_wegdauer_haltestelle_schule_entries.grid()
        wegdauer_haltestelle_schule_entries.append(entry_wegdauer_haltestelle_schule_entries)

        label_schueleranzahl = ttk.Label(scrollable_tab2.scrollable_frame, text="Anzahl Schüler",
                                         font=("Helvetica", 10))
        label_schueleranzahl.grid()
        entry_schueleranzahl = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_schueleranzahl.grid()
        schueleranzahlen.append(entry_schueleranzahl)

        label_betreuungsangebot_morgens = ttk.Label(scrollable_tab2.scrollable_frame,
                                                    text="Betreuungsangebot vor Unterrichtsbeginn?",
                                                    font=("Helvetica", 10))
        label_betreuungsangebot_morgens.grid()
        checkbutton_betreuung_morgens = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste1[i])
        checkbutton_betreuung_morgens.grid()
        checkbuttons.append(checkbutton_betreuung_morgens)

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
