#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importieren von Biblotheken
import tkinter as tk
from tkinter import ttk
from threading import Thread
import pandas

# Import eigener Methoden
from Methode_Schulcharakteristika import schulcharakteristika_eingeben
from Methode_Eingabe_prüfen import eingabe_prüfen
from Methode_Werte_eintragen import Werte_eintragen
from Methode_Fahrzeiten_eingeben import fahrzeiten_eintragen
from Matrizenbearbeitung_GUI import matrizenbearbeitung
from Methode_Erstellung_gültiger_Kombinationen_Busankunft import erstellung_kombination_busankunft
from Methode_Akzeptanzbewertung import Akzeptanzbewertung_rechnen
from Methode_Matrizenerstellung import matrizenerstellung


d = pandas.read_csv('Daten_rating_system2.csv', sep=';')


# GUI-Rahmen festlegen
# Hauptfenster erstellen
root = tk.Tk()
root.title("Programm Unterrichtszeitenstaffelung")

# Tab-Control erstellen
notebook = ttk.Notebook(root)  # Organisation der Tabs

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)

notebook.add(tab1, text="Angaben zum Untersuchungsgebiet")
notebook.add(tab2, text="Angaben zu den Schulen")
notebook.add(tab3, text="Angaben zu den Haltestellen")
notebook.add(tab4, text="Angabe der Fahrzeiten")
notebook.add(tab6, text="Ergebnis Einsparung")
notebook.add(tab7, text="Ergebnis Akzeptanz")

# Tabs dem Hauptfenster hinzufügen
notebook.pack(expand=1, fill='both')


# Scrollable Frame class
class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        canvas = tk.Canvas(self)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=self.scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


# Erstellen eines scrollbaren Rahmens für jedes Tab
scrollable_tab1 = ScrollableFrame(tab1)
scrollable_tab2 = ScrollableFrame(tab2)
scrollable_tab3 = ScrollableFrame(tab3)
scrollable_tab4 = ScrollableFrame(tab4)
scrollable_tab5 = ScrollableFrame(tab5)
scrollable_tab6 = ScrollableFrame(tab6)
scrollable_tab7 = ScrollableFrame(tab7)

scrollable_tab1.pack(expand=1, fill='both')
scrollable_tab2.pack(expand=1, fill='both')
scrollable_tab3.pack(expand=1, fill='both')
scrollable_tab4.pack(expand=1, fill='both')
scrollable_tab5.pack(expand=1, fill='both')
scrollable_tab6.pack(expand=1, fill='both')
scrollable_tab7.pack(expand=1, fill='both')

# Globale Listen und Variablen
aktueller_unterrichtsbeginn_alle_schulen_entries = []
haltestellennummern_entries = []
versatz_ankunft_durch_anschlussfahrt_entries = []
n_ava = []
Travel_times = []
n_reuses = []
starts = []
startzeiten = []

entry_aktueller_Schulbeginn = 0
entry_travel_times = []
wegdauer_haltestelle_schule_entries = []
merkmalsliste = []
Var = []
check_var_liste1 = []
check_var_liste2 = []
check_var_liste3 = []
check_var_liste4 = []
check_var_liste5 = []
checkbuttons = []
schueleranzahlen = []

button_style = ttk.Style()
button_style.configure('Custom.TButton', font=('Helvetica', 10, "bold"))


# Buttonfunktionen Tab 2
def wechsel_tab1_tab2():
    notebook.select(tab2)
    button_wechsel_tab1_tab2.configure(state=tk.DISABLED)
    schulcharakteristika_eingeben(entry_anzahl_schulen, scrollable_tab2,
                                  aktueller_unterrichtsbeginn_alle_schulen_entries, haltestellennummern_entries,
                                  versatz_ankunft_durch_anschlussfahrt_entries, wegdauer_haltestelle_schule_entries,
                                  schueleranzahlen, checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3,
                                  check_var_liste4, check_var_liste5)

    entry_anzahl_schulen.config(state=tk.DISABLED)
    entry_Anzahl_Haltestellen.config(state=tk.DISABLED)
    entry_anzahl_bewohner.config(state=tk.DISABLED)


def eingabe_prüfen_main():
    eingabe_prüfen(aktueller_unterrichtsbeginn_alle_schulen_entries, versatz_ankunft_durch_anschlussfahrt_entries,
                   wegdauer_haltestelle_schule_entries, scrollable_tab2, button_werteingabe_bestaetigen,
                   button_eingabe_pruefen)


def werteingabe_bestätigen():
    Werte_eintragen(entry_anzahl_schulen, aktueller_unterrichtsbeginn_alle_schulen_entries, schueleranzahlen,
                    check_var_liste1, check_var_liste2, check_var_liste3, check_var_liste4, check_var_liste5,
                    merkmalsliste)

    button_werteingabe_bestaetigen.configure(state=tk.DISABLED)
    button_eingabe_pruefen.configure(state=tk.DISABLED)
    button_wechsel_tab2_tab3.configure(state=tk.NORMAL)
    for startzeiten_entry in aktueller_unterrichtsbeginn_alle_schulen_entries:
        startzeiten_entry.config(state="disabled")

    for wegdauer_haltestelle_schule_entries_entry in wegdauer_haltestelle_schule_entries:
        wegdauer_haltestelle_schule_entries_entry.config(state="disabled")

    for versatz_ankunft_durch_anschlussfahrt_entries_entry in versatz_ankunft_durch_anschlussfahrt_entries:
        versatz_ankunft_durch_anschlussfahrt_entries_entry.config(state="disabled")

    for haltestellennummern_entry in haltestellennummern_entries:
        haltestellennummern_entry.config(state="disabled")

    for schueleranzahlen_entry in schueleranzahlen:
        schueleranzahlen_entry.config(state="disabled")

    for checkbutton in checkbuttons:
        checkbutton.config(state="disabled")


# Eingabe Anzahl Busse pro Haltestelle - Tab 3
def wechsel_tab2_tab3():
    notebook.select(tab3)
    button_wechsel_tab2_tab3.configure(state=tk.DISABLED)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for i in range(anzahl_schulen_bus):
        row = i * 2  # Verwenden Sie die doppelte Zeilenzahl, um Platz für alle Widgets zu schaffen
        label_anzahl_busse_pro_haltestelle = ttk.Label(scrollable_tab3.scrollable_frame,
                                                       text=f'Anzahl Busse zu Haltestelle {i + 1}',
                                                       font=("Helvetica", 10))
        label_anzahl_busse_pro_haltestelle.grid(column=0, row=row, padx=5, pady=5)
        entry_anzahl_busse_pro_haltestelle = ttk.Entry(scrollable_tab3.scrollable_frame)
        entry_anzahl_busse_pro_haltestelle.grid(column=1, row=row, padx=5, pady=5)
        n_ava.append(entry_anzahl_busse_pro_haltestelle)


# Eingaben zu den Fahrzeiten Tab 4
def wechsel_tab3_tab4():
    for ein_entry_anzahl_busse_pro_haltestelle in n_ava:
        ein_entry_anzahl_busse_pro_haltestelle.config(state="disabled")
    notebook.select(tab4)
    button_wechsel_tab3_tab4.configure(state=tk.DISABLED)

    label_erklaerung_angabe_fahrzeit1 = ttk.Label(scrollable_tab4.scrollable_frame,
                                                  text="Die Fahrzeit von einer Schule zum Routenstart zu einer anderen"
                                                       " Schule muss mit einem Navigator ermittelt werden",
                                                  font=("Helvetica", 10))
    label_erklaerung_angabe_fahrzeit1.grid(column=0, row=0)
    label_erklaerung_angabe_fahrzeit2 = ttk.Label(scrollable_tab4.scrollable_frame, text="Dieser Wert wird mit der "
                                                                                         "Fahrzeit einer entsprechenden"
                                                                                         " Route addiert. Die "
                                                                                         "Routenzeit"
                                                                                         " muss dem aktuellen Fahrplan "
                                                                                         "entnommen werden.\n\n "
                                                                                         "-----------------------------"
                                                                                         "-----------------------------"
                                                                                         "---------------------------"
                                                                                         "---------------------------"
                                                                                         "----------------------------"
                                                                                         "-----------------------------"
                                                                                         "-----------------------------"
                                                                                         "-----------------------------"
                                                                                         "--------------------------",
                                                  font=("Helvetica", 10))
    label_erklaerung_angabe_fahrzeit2.grid(column=0, row=1)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    fahrzeiten_eintragen(anzahl_schulen_bus, n_ava, scrollable_tab4, entry_travel_times, Travel_times)


# Tab 4 Berechnungrn
def berechnung_starten_ladeprozess():
    t1 = Thread(target=berechnung_starten)
    t1.start()


def berechnung_starten():
    button_berechnung_starten.configure(state=tk.DISABLED)
    for entry_travel_time in entry_travel_times:
        entry_travel_time.config(state="disabled")
    notebook.select(tab6)

    label_es_laedt = ttk.Label(text="Es lädt ...", font=("Helvetica", 20, "bold"))
    label_es_laedt.pack()

    for i in range(len(Travel_times)):
        if Travel_times[i] == 0:
            Travel_times[i] = int(entry_travel_times.pop(0).get())

    busses_needed_without = sum(int(entry.get()) for entry in n_ava)
    combinations = erstellung_kombination_busankunft(anzahl_schulen, aktueller_unterrichtsbeginn_alle_schulen_entries,
                                                     versatz_ankunft_durch_anschlussfahrt_entries,
                                                     wegdauer_haltestelle_schule_entries, haltestellennummern_entries)

    n_ava_values = [int(entry.get()) for entry in n_ava]
    matrizen, schoolstart_combination = matrizenerstellung(combinations, anzahl_haltestellen_entry,
                                                           busses_needed_without, Travel_times, n_ava_values)

    for matrix in matrizen:

        max_anfahrten = []
        for i in range(len(n_ava_values)):
            max_anfahrten.append(0)
        n_reuse = 0
        n_ava_values = [int(entry.get()) for entry in n_ava]
        n_ava_unverbraucht = n_ava_values.copy()
        n_anfahrten = n_ava_values.copy()
        n_reuse_einzel = matrizenbearbeitung(matrix, n_ava_values, n_ava_unverbraucht, n_reuse, max_anfahrten,
                                             n_anfahrten)
        n_reuses.append(n_reuse_einzel)

    # Bestimmung eines hohen Einspapotenzials
    anzahl_einwohner = int(entry_anzahl_bewohner.get())
    teiler = 83300000 / anzahl_einwohner
    mindestbuseinsparung_hohe_einsparung = int(19600 * 1.15 / teiler) + 1

# Bestimmung der Inidzies für Varianten mit hohem Einspapotenzial
    max_reuses = max(n_reuses)
    indizes_busankunftsvarianten_hohe_einsparung = []

    # Berechnen und Ausgeben, solange die Einsparung nicht hoch genug ist
    for durchlaeufe1 in range(max_reuses - mindestbuseinsparung_hohe_einsparung + 1):
        # Neue Liste für jeden Durchlauf erstellen
        indices = [i for i, x in enumerate(n_reuses) if x == max_reuses - durchlaeufe1]
        indizes_busankunftsvarianten_hohe_einsparung.append(indices)

    #  - Ausgabe der Busankunftszeiten und Unterrichtsbeginnzeiten
    label_ergebnisse = ttk.Label(scrollable_tab6.scrollable_frame, text="Ergebnisse", font=("Helvetica", 12, "bold"))
    label_ergebnisse.grid()
    label_anzahl_busse_ohne_staffelung = ttk.Label(scrollable_tab6.scrollable_frame, text=f"Ohne Staffelung der "
                                                                                          f"Unterrichtszeiten werden "
                                                                                          f"{busses_needed_without} "
                                                                                          f"Busse benötigt",
                                                   font=("Helvetica", 10))
    label_anzahl_busse_ohne_staffelung.grid()
    label_maximale_einsparung = ttk.Label(scrollable_tab6.scrollable_frame, text=f"Es können maximal {max(n_reuses)} "
                                                                                 f"Busse eingespart werden",
                                          font=("Helvetica", 10))
    label_maximale_einsparung.grid()
    label_hohe_einsparung = ttk.Label(scrollable_tab6.scrollable_frame, text=f"Ein hohes Einsparpotenzial wird ab "
                                                                             f"{mindestbuseinsparung_hohe_einsparung} "
                                                                             f"Bussen erreicht", font=("Helvetica", 10))
    label_hohe_einsparung.grid()
    label_trennstrich = tk.Label(scrollable_tab6.scrollable_frame, text="-"*150, font=("Helvetica", 10))
    label_trennstrich.grid()
    label_erklaerung_buseinsparung1 = ttk.Label(scrollable_tab6.scrollable_frame, text="Die erste angegebene Zeit ist "
                                                                                       "die Busankunftszeit an "
                                                                                       "Haltestelle Nummer 1 "
                                                                                       "(angegeben in Minuten nach 7).",
                                                font=("Helvetica", 10))
    label_erklaerung_buseinsparung1.grid()
    label_erklaerung_buseinsparung2 = ttk.Label(scrollable_tab6.scrollable_frame, text="Es folgt die Busankunftszeit an"
                                                                                       " Haltestelle 2 usw.. Analog "
                                                                                       "dazu wird bei den "
                                                                                       "Unterrichtsbeginnzeiten als "
                                                                                       "erstes", font=("Helvetica", 10))
    label_erklaerung_buseinsparung2.grid()
    label_erklaerung_buseinsparung3 = ttk.Label(scrollable_tab6.scrollable_frame, font=("Helvetica", 10),
                                                text="der Unterrichtsbeginn an Schule 1, dann an Schule 2 usw." +
                                                     "(ebenfalls in Minuten nach 7) angegeben\n\n " +
                                                     "-"*150)
    label_erklaerung_buseinsparung3.grid()
    # Ausgabe der Ergebnisse für die restlichen höchsten Werte
    for durchlaeufe2 in range(max_reuses - mindestbuseinsparung_hohe_einsparung + 1):
        label_einsparungen = ttk.Label(scrollable_tab6.scrollable_frame, font=("Helvetica", 10, "bold"),
                                       text=f"Mit folgenden Varianten werden {max_reuses-durchlaeufe2} Busse gespart")
        label_einsparungen.grid()

        for q in indizes_busankunftsvarianten_hohe_einsparung[durchlaeufe2]:
            label_Kombinationen = ttk.Label(scrollable_tab6.scrollable_frame,
                                            text=f"Busankunftszeiten: {', '.join(map(str, schoolstart_combination[q]))}",
                                            font=("Helvetica", 10))
            label_Kombinationen.grid()
            Var.append(schoolstart_combination[q])

            Busankunft_Liste_Alle_Schulen_Kombinationen = []
            Unterrichtsbeginn_Kombinationen = []
            for inner_list in schoolstart_combination:

                # Füge die Elemente der inneren Liste so oft zur Zielliste hinzu, wie die Anzahl der Nummern
                Busankunft_Liste_Alle_Schulen = []
                Unterrichtsbeginn = []

                Haltestellennummern_int = [int(entry.get()) for entry in haltestellennummern_entries]

                for schule in range(int(anzahl_schulen.get())):
                    haltestelle = Haltestellennummern_int[schule] - 1
                    ankunftszeit = inner_list[haltestelle]
                    Busankunft_Liste_Alle_Schulen.append(ankunftszeit)
                    Unterrichtsbeginn_Aktuelle_Schule = int(wegdauer_haltestelle_schule_entries[schule].get()) + int(
                        versatz_ankunft_durch_anschlussfahrt_entries[schule].get()) + ankunftszeit
                    Unterrichtsbeginn.append(Unterrichtsbeginn_Aktuelle_Schule)

                Busankunft_Liste_Alle_Schulen_Kombinationen.append(Busankunft_Liste_Alle_Schulen)
                Unterrichtsbeginn_Kombinationen.append(Unterrichtsbeginn)

            label_Unterrichtsbeginn = ttk.Label(scrollable_tab6.scrollable_frame,
                                                text="Unterrichtsbeginn an den Schulen: " +
                                                     ', '.join(map(str, Unterrichtsbeginn_Kombinationen[q])),
                                                font=("Helvetica", 10))
            label_Unterrichtsbeginn.grid()
            label_Trennstrich = ttk.Label(scrollable_tab6.scrollable_frame,
                                          text="-"*81)
            label_Trennstrich.grid()

    label_es_laedt.destroy()
    button_akzeptanzbewertung_anzeigen.configure(state=tk.NORMAL)


def akzeptanzbewertung_anzeigen_ladeprozess():
    t2 = Thread(target=akzeptanzbewertung_anzeigen)
    t2.start()


def akzeptanzbewertung_anzeigen():
    notebook.select(tab7)

    button_akzeptanzbewertung_anzeigen.configure(state=tk.DISABLED)

    label_laedt_akzeptanz = ttk.Label(scrollable_tab7.scrollable_frame, text="Es lädt ...",
                                      font=("Helvetica", 20, "bold"))
    label_laedt_akzeptanz.pack()

    Gesamtmittelwerte = Akzeptanzbewertung_rechnen(d, merkmalsliste, Var, entry_anzahl_schulen,
                                                   haltestellennummern_entries,
                                                   versatz_ankunft_durch_anschlussfahrt_entries,
                                                   wegdauer_haltestelle_schule_entries,
                                                   aktueller_unterrichtsbeginn_alle_schulen_entries)
    max_punkte = max(Gesamtmittelwerte)
    max_punkte_gerundet = round(max_punkte, 3)
    indices_of_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == max_punkte]

    label_hoechste_punktzahl_akzeptanz = ttk.Label(scrollable_tab7.scrollable_frame,
                                                   text=f"Die höchste Akzeptanzpunktzhal beträgt {max_punkte_gerundet}."
                                                        f"Diese kann mit folgenden Varianten erreicht werden:",
                                                   font=("Helvetica", 10))
    label_hoechste_punktzahl_akzeptanz.pack()
    for index in indices_of_highest_value:
        label_busankunftszeiten = ttk.Label(scrollable_tab7.scrollable_frame,
                                            text=f"Busankunftszeiten: {', '.join(map(str, Var[index]))}",
                                            font=("Helvetica", 10))
        label_busankunftszeiten.pack()

    label_laedt_akzeptanz.destroy()


# Tab-Grundstruktur festlegen
# Tab1
anzahl_schulen_entry = tk.StringVar(value="0")
label_anzahl_Schulen = ttk.Label(scrollable_tab1.scrollable_frame,
                                 text="Anzahl Schulen, die vom Busverkehr bedient werden", font=("Helvetica", 10))
label_anzahl_Schulen.grid(column=0, row=0, padx=5, pady=5)
entry_anzahl_schulen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=anzahl_schulen_entry)
entry_anzahl_schulen.grid(column=0, row=1, padx=5, pady=5)
anzahl_schulen = entry_anzahl_schulen

anzahl_haltestellen_entry = tk.StringVar(value="0")
label_anzahl_haltestellen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Haltestellen für Schülerverker",
                                      font=("Helvetica", 10))
label_anzahl_haltestellen.grid(column=0, row=2, padx=5, pady=5)
label_anzahl_haltestellen_erklaerung1 = ttk.Label(scrollable_tab1.scrollable_frame,
                                                  text="(Wenn eine Haltestelle immer direkt als Anschlussfahrt von "
                                                       "einer", font=("Helvetica", 8))
label_anzahl_haltestellen_erklaerung1.grid(column=0, row=3)
label_anzahl_haltestellen_erklaerung2 = ttk.Label(scrollable_tab1.scrollable_frame,
                                                  text="anderen Haltestelle angefahren wird, wird diese hier NICHT "
                                                       "mitgezählt)", font=("Helvetica", 8))

label_anzahl_haltestellen_erklaerung2.grid(column=0, row=4)
entry_Anzahl_Haltestellen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=anzahl_haltestellen_entry)
entry_Anzahl_Haltestellen.grid(column=0, row=5, padx=5, pady=5)

anzahl_bewohner_entry = tk.StringVar(value="0")
label_anzahl_bewohner = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Bewohner im Untersuchungsgebiet",
                                  font=("Helvetica", 10))
label_anzahl_bewohner.grid(column=0, row=6, padx=5, pady=5)
entry_anzahl_bewohner = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=anzahl_bewohner_entry)
entry_anzahl_bewohner.grid(column=0, row=7, padx=5, pady=5)

button_wechsel_tab1_tab2 = ttk.Button(scrollable_tab1.scrollable_frame, text="Nächster Schritt",
                                      command=wechsel_tab1_tab2, style='Custom.TButton')
button_wechsel_tab1_tab2.grid(column=1, row=0, padx=5, pady=5)

# Tab2
button_eingabe_pruefen = ttk.Button(scrollable_tab2.scrollable_frame, text="Eingaben überprüfen",
                                    command=eingabe_prüfen_main, style='Custom.TButton')
button_eingabe_pruefen.grid(column=1, row=4)
button_werteingabe_bestaetigen = ttk.Button(scrollable_tab2.scrollable_frame, text="Werte eingetragen",
                                            command=werteingabe_bestätigen, state=tk.DISABLED, style='Custom.TButton')
button_werteingabe_bestaetigen.grid(column=2, row=4)
button_wechsel_tab2_tab3 = ttk.Button(scrollable_tab2.scrollable_frame, text="Nächster Schritt",
                                      command=wechsel_tab2_tab3, state=tk.DISABLED, style='Custom.TButton')
button_wechsel_tab2_tab3.grid(column=3, row=4, padx=5, pady=5)

# Tab3
button_wechsel_tab3_tab4 = ttk.Button(scrollable_tab3.scrollable_frame, text="Nächster Schritt",
                                      command=wechsel_tab3_tab4, style='Custom.TButton')
button_wechsel_tab3_tab4.grid(column=3, row=0, padx=5, pady=5)

# Tab4
button_berechnung_starten = ttk.Button(scrollable_tab4.scrollable_frame, text="Berechnung starten",
                                       command=berechnung_starten_ladeprozess, style='Custom.TButton')
button_berechnung_starten.grid(column=2,  padx=5, pady=5)

# Tab6
button_akzeptanzbewertung_anzeigen = ttk.Button(scrollable_tab6.scrollable_frame, text="Akzeptanzbewertung anzeigen",
                                                command=akzeptanzbewertung_anzeigen_ladeprozess, style='Custom.TButton',
                                                state=tk.DISABLED)
button_akzeptanzbewertung_anzeigen.grid(column=1)

# Hauptfenster ausführen
root.mainloop()
