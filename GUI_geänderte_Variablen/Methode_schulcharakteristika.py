import tkinter as tk
from tkinter import ttk


def schulcharakteristika_eingeben(entry_anzahl_schulen, scrollable_tab2,
                                  aktueller_unterrichtsbeginn_alle_schulen, haltestellennummern_alle_schulen,
                                  versatz_ankunft_anschlussfahrt, wegdauern_haltestelle_schule, schüleranzahlen,
                                  checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3, check_var_liste4,
                                  check_var_liste5):
    """
    Erstellung jener entry- und checkbuttonfelder, um Schulcharakterstiken einzugeben


    :param entry_anzahl_schulen: bestimmt wie oft ein entry- /checkbuttonfeld erstellt wird (für jede Schule wird jedes
    Feld einmal erstellt)
    :param scrollable_tab2: gibt an, wo die labels, entry- und checkbuttonfelder angezeigt werden
    :param aktueller_unterrichtsbeginn_alle_schulen: zum einen einer der Schulcharakteristiken zum anderen benötigt, um
    am Ende die Verschiebung des Unterrichtsbeginns (mit Unterrichtszeitenstaffelung) daraus zu berechnen
    :param haltestellennummern_alle_schulen: jeder Schule wird eine aufsteigende Haltestellennummer zugewiesen, wenn
    mehrere Schulen dieselbe Haltestelle nutzen oder eine Haltestelle direkt als Anschlussfahrt angefahren wird,
    erhalten sie dieselbe Nummer
    :param versatz_ankunft_anschlussfahrt: bei einer anschlussfahrt wird hier die benötigte Zeit von der früheren zur
    späteren Haltestelle mit der identischen Nummer eingegeben
    :param wegdauern_haltestelle_schule: gibt die benötigte Zeit zwischen Busankunft und Unterrichtsbeginn je
    Schule an
    :param schüleranzahlen: Eines der Schulcharakteristika, Schüleranzahl je Schule wird in Liste gespeichert
    :param checkbuttons: liste aus checkbuttons, um anzukreuzen, ob es etwas an einer bestimmten Schule gibt
    :param check_var_liste1: speichert, die Eingaben je Schule für den ersten Checkbutton, ob die Schule eine Betreuung
    vor Unterrichtsbeginn anbietet
    :param check_var_liste2: speichert, die Eingaben je Schule für den zweiten Checkbutton, ob die Schule eine Betreuung
    nach Unterrichtsende anbietet
    :param check_var_liste3: speichert, die Eingaben je Schule für den dritten Checkbutton, ob die Schule über eine
    Mensa verfügt
    :param check_var_liste4: speichert, die Eingaben je Schule für den vierten Checkbutton, ob die Schule Lehrer hat,
    die auch an anderen Schulen unterrichten
    :param check_var_liste5: speichert, die Eingaben je Schule für den fünften Checkbutton, ob die Schule Schüler hat,
    die für einzelne Fächer andere Schulen besuchen
    :return: Kein Rückgabewert, da diese Methode nur das Eingabelayout erstellt
    """

    # Umwandlung des entry-wertes in eine int.-variable
    anzahl_schulen = int(entry_anzahl_schulen.get())

    # Erstellung von Listen, um dort zu speichern, ob ein Button ausgewählt wurde
    check_var_liste1.extend([tk.StringVar() for _ in range(anzahl_schulen)])
    check_var_liste2.extend([tk.StringVar() for _ in range(anzahl_schulen)])
    check_var_liste3.extend([tk.StringVar() for _ in range(anzahl_schulen)])
    check_var_liste4.extend([tk.StringVar() for _ in range(anzahl_schulen)])
    check_var_liste5.extend([tk.StringVar() for _ in range(anzahl_schulen)])

    # für alle Schulen werden alle entry- und checkbuttonfelder erstellt
    for i in range(anzahl_schulen):
        label_schule = ttk.Label(scrollable_tab2.scrollable_frame, text=f'Schule {i + 1}',
                                 font=("Helvetica", 12, "bold"))
        label_schule.grid()

        label_aktueller_schulbeginn1 = ttk.Label(scrollable_tab2.scrollable_frame,
                                                 text="Aktueller Unterrichtsbeginn in Minuten nach 7 ",
                                                 font=("Helvetica", 10))
        label_aktueller_schulbeginn1.grid()
        label_aktueller_schulbeginn2 = ttk.Label(scrollable_tab2.scrollable_frame,
                                                 text="(Als Vielfaches von 5 angeben)", font=("Helvetica", 8))
        label_aktueller_schulbeginn2.grid()
        entry_aktueller_schulbeginn = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_aktueller_schulbeginn.grid()
        aktueller_unterrichtsbeginn_alle_schulen.append(entry_aktueller_schulbeginn)

        label_haltestellennutzung1 = tk.Label(scrollable_tab2.scrollable_frame,
                                              text="Haltestellennummer", font=("Helvetica", 10))
        label_haltestellennutzung1.grid()
        label_haltestellennutzung2 = tk.Label(scrollable_tab2.scrollable_frame,
                                              text="(Schulen, die dieselbe Haltestelle nutzen oder direkt nacheinander "
                                                   "angefahren werden, erhalten die selbe Nummer)",
                                              font=("Helvetica", 8))
        label_haltestellennutzung2.grid()
        entry_haltestellennumer = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_haltestellennumer.grid()
        haltestellennummern_alle_schulen.append(entry_haltestellennumer)

        label_spätere_ankunft1 = tk.Label(scrollable_tab2.scrollable_frame,
                                          text=f"Bei Anschlussfahrt die Fahrzeit von der früheren zu dieser "
                                               f"Haltestelle eintragen", font=("Helvetica", 10))
        label_spätere_ankunft1.grid()
        label_spätere_ankunft2 = tk.Label(scrollable_tab2.scrollable_frame,
                                          text="(Als Vielfaches von 5 angeben, ansonsten 0 eintragen)",
                                          font=("Helvetica", 8))
        label_spätere_ankunft2.grid()
        entry_spätere_ankunft = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_spätere_ankunft.grid()
        versatz_ankunft_anschlussfahrt.append(entry_spätere_ankunft)

        label_wegdauer_haltestelle_schule_1 = tk.Label(scrollable_tab2.scrollable_frame,
                                                       text=f"Benötigte Zeit zwischen Busankunft und Unterrichtsbeginn",
                                                       font=("Helvetica", 10))
        label_wegdauer_haltestelle_schule_1.grid()
        label_wegdauer_haltestelle_schule_2 = tk.Label(scrollable_tab2.scrollable_frame,
                                                       text=f"(Als Vielfaches von 5 angeben)",
                                                       font=("Helvetica", 8))
        label_wegdauer_haltestelle_schule_2.grid()
        entry_wegdauer_haltestelle_schule = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_wegdauer_haltestelle_schule.grid()
        wegdauern_haltestelle_schule.append(entry_wegdauer_haltestelle_schule)

        label_schüleranzahl = ttk.Label(scrollable_tab2.scrollable_frame, text="Anzahl Schüler", font=("Helvetica", 10))
        label_schüleranzahl.grid()
        entry_schüleranzahl = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_schüleranzahl.grid()
        schüleranzahlen.append(entry_schüleranzahl)

        label_betreuungsangebot_morgens = ttk.Label(scrollable_tab2.scrollable_frame,
                                                    text="Betreuungsangebot vor Unterrichtsbeginn?",
                                                    font=("Helvetica", 10))
        label_betreuungsangebot_morgens.grid()
        checkbutton_betreuung_morgens = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste1[i])
        checkbutton_betreuung_morgens.grid()
        checkbuttons.append(checkbutton_betreuung_morgens)

        label_betreuungsangebot_mittags = ttk.Label(scrollable_tab2.scrollable_frame,
                                                    text="Betreuungsangebot nach Unterrichtsende?",
                                                    font=("Helvetica", 10))
        label_betreuungsangebot_mittags.grid()
        checkbutton_betreuung_mittags = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste2[i])
        checkbutton_betreuung_mittags.grid()
        checkbuttons.append(checkbutton_betreuung_mittags)

        label_mensa = ttk.Label(scrollable_tab2.scrollable_frame, text="Mensa vorhanden?", font=("Helvetica", 10))
        label_mensa.grid()
        checkbutton_mensa = ttk.Checkbutton(scrollable_tab2.scrollable_frame, variable=check_var_liste3[i])
        checkbutton_mensa.grid()
        checkbuttons.append(checkbutton_mensa)

        label_andere_lehrer = ttk.Label(scrollable_tab2.scrollable_frame, text="Lehrer, die  auch an anderen Schulen "
                                                                               "unterrichten?", font=("Helvetica", 10))
        label_andere_lehrer.grid()
        checkbutton_andere_lehrer = ttk.Checkbutton(scrollable_tab2.scrollable_frame,  variable=check_var_liste4[i])
        checkbutton_andere_lehrer.grid()
        checkbuttons.append(checkbutton_andere_lehrer)

        label_andere_schüler = ttk.Label(scrollable_tab2.scrollable_frame, font=("Helvetica", 10),
                                         text="Schüler, die auch Fächer an anderen Schulen besuchen?")

        label_andere_schüler.grid()
        checkbutton_andere_schüler = ttk.Checkbutton(scrollable_tab2.scrollable_frame,  variable=check_var_liste5[i])
        checkbutton_andere_schüler.grid()
        checkbuttons.append(checkbutton_andere_schüler)
