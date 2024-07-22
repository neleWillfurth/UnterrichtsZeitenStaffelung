#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importieren von Bibliotheken
import tkinter as tk
from tkinter import ttk
from threading import Thread

# Import eigener Methoden
from Methode_schulcharakteristika import schulcharakteristika_eingeben
from Methode_eingabe_prüfen import eingabe_prüfen
from Methode_werte_eintragen import werte_eintragen
from Methode_fahrzeiten_eingeben import fahrzeiten_eintragen
from Methode_matrizenbearbeitung import matrizenbearbeitung
from Methode_erstellung_kombinationen_busankunft import erstellung_kombination_busankunft
from Methode_akzeptanzbewertung import akzeptanzbewertung_rechnen
from Methode_matrizenerstellung import matrizenerstellung

# Zu Beginn wird die Grundstruktur der GUI erstellt
# Hauptfenster der GUI erstellen
root = tk.Tk()
root.title("Programm Unterrichtszeitenstaffelung")

# Verschiedene Tabs zur GUI ergänzen
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)

notebook.add(tab1, text="Angaben zum Untersuchungsgebiet")
notebook.add(tab2, text="Angaben zu den Schulen")
notebook.add(tab3, text="Angaben zu den Haltestellen")
notebook.add(tab4, text="Angabe der Fahrzeiten")
notebook.add(tab5, text="Ergebnis Einsparung")
notebook.add(tab6, text="Ergebnis Akzeptanz")

# Tabs dem Hauptfenster hinzufügen
notebook.pack(expand=1, fill='both')


# Scrollmöglichkeit den Tabs hinzufügen
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


scrollable_tab1 = ScrollableFrame(tab1)
scrollable_tab2 = ScrollableFrame(tab2)
scrollable_tab3 = ScrollableFrame(tab3)
scrollable_tab4 = ScrollableFrame(tab4)
scrollable_tab5 = ScrollableFrame(tab5)
scrollable_tab6 = ScrollableFrame(tab6)

scrollable_tab1.pack(expand=1, fill='both')
scrollable_tab2.pack(expand=1, fill='both')
scrollable_tab3.pack(expand=1, fill='both')
scrollable_tab4.pack(expand=1, fill='both')
scrollable_tab5.pack(expand=1, fill='both')
scrollable_tab6.pack(expand=1, fill='both')


# Globale Listen und Variablen
# Listen mit Werten für alle Schulen
aktueller_unterrichtsbeginn_alle_schulen = []  # beinhaltet den aktuellen Schulbeginn für jede Schule
haltestellennummern_alle_schulen = []  # beinhaltet die Haltestellennummer für jede Schule
versatz_ankunft_anschlussfahrt = []  # benötigte Zeit von der früheren zur späteren Haltestelle (wenn mehrere Schulen
# sich eine Haltestelle teilen)
wegdauern_haltestelle_schule = []  # benötigte Zeit zwischen Busankunft und Unterrichtsbeginn
schüleranzahlen = []  # beinhaltet die Klasse an Schülerzahlen (1-6)
check_var_liste1 = []  # beinhaltet die Eingaben je Schule für den ersten Checkbutton, ob die Schule eine Betreuung
# vor Unterrichtsbeginn anbietet
check_var_liste2 = []  # beinhaltet die Eingaben je Schule für den zweiten Checkbutton, ob die Schule eine Betreuung
# nach Unterrichtsende anbietet
check_var_liste3 = []  # beinhaltet die Eingaben je Schule für den dritten Checkbutton, ob die Schule über eine Mensa
# verfügt
check_var_liste4 = []  # beinhaltet die Eingaben je Schule für den vierten Checkbutton, ob die Schule Lehrer hat,
# die auch an anderen Schulen unterrichten
check_var_liste5 = []  # beinhaltet die Eingaben je Schule für den fünften Checkbutton, ob die Schule Schüler hat,
# die für einzelne Fächer andere Schulen besuchen

# Die Merkmalslisten der einzelnen Schulen werden zusammengefasst in der Liste
merkmale_alle_schulen = []

# Listen Fahrzeiten
entry_fahrzeiten = []  # Zwischenliste für entry-Eingaben der Fahrzeiten
fahrzeiten = []  # Liste mit allen Fahrzeiten
anzahl_busse_je_haltestelle = []

# Weitere Listen
checkbuttons = []  # liste aller Checkbuttons
busse_wiedernutzbar = []  # Liste mit der Anzahl wiedernutzbarer Busse je Kombination an Busankunftszeiten
kombinationen_buseinkünfte_hohe_einsparung = []  # Liste mit allen Kombinationen an Busankunftszeiten mit denen eine
# hohe Einsparung erreicht wird

# Festlegen des Aussehens der Buttons
button_style = ttk.Style()
button_style.configure('Custom.TButton', font=('Helvetica', 10, "bold"))

# Im Folgenden werden alle Methoden beschrieben


# Diese Methode wird aufgerufen, wenn von Tab 1 zu 2 gewechselt wird
def wechsel_tab1_tab2():
    notebook.select(tab2)
    button_wechsel_tab1_tab2.configure(state=tk.DISABLED)
    # die Methode schulcharakteristika_eingeben wird aufgerufen, um jede Schule zu charakterisieren
    schulcharakteristika_eingeben(entry_anzahl_schulen, scrollable_tab2,
                                  aktueller_unterrichtsbeginn_alle_schulen, haltestellennummern_alle_schulen,
                                  versatz_ankunft_anschlussfahrt, wegdauern_haltestelle_schule,
                                  schüleranzahlen, checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3,
                                  check_var_liste4, check_var_liste5)

    # alle entry-Felder aus Tab1 können nicht mehr geändert werden
    entry_anzahl_schulen.config(state=tk.DISABLED)
    entry_anzahl_haltestellen.config(state=tk.DISABLED)
    entry_anzahl_bewohner.config(state=tk.DISABLED)


# nach eingabe der Schulcharakteristika müssen die Eingaben per Buttonklick auf button_eingabe_prüfen geprüft werden
def eingabe_prüfen_main():
    eingabe_prüfen(aktueller_unterrichtsbeginn_alle_schulen, versatz_ankunft_anschlussfahrt,
                   wegdauern_haltestelle_schule, scrollable_tab2, button_werteingabe_bestätigen,
                   button_eingabe_prüfen)


def werteingabe_bestätigen():
    # mit dieser Funktion werden die eingegebenen Daten zur Weiterverarbeitung gespeichert
    werte_eintragen(entry_anzahl_schulen, aktueller_unterrichtsbeginn_alle_schulen, schüleranzahlen,
                    check_var_liste1, check_var_liste2, check_var_liste3, check_var_liste4, check_var_liste5,
                    merkmale_alle_schulen)

    # der button_werteingabe_bestätigen und button_eingabe_prüfen werden unnutzbar gemacht uns der
    # button_wechsel_tab2_tab3 wird freigeschalten
    button_werteingabe_bestätigen.configure(state=tk.DISABLED)
    button_eingabe_prüfen.configure(state=tk.DISABLED)
    button_wechsel_tab2_tab3.configure(state=tk.NORMAL)
    # alle entry-Felder in tab 2 werden ausgegraut, um zu verdeutlichen, dass man die Werte nicht mehr ändern kann
    for startzeiten_entry in aktueller_unterrichtsbeginn_alle_schulen:
        startzeiten_entry.config(state="disabled")

    for wegdauer_haltestelle_schule_entry in wegdauern_haltestelle_schule:
        wegdauer_haltestelle_schule_entry.config(state="disabled")

    for versatz_ankunft_anschlussfahrt_entry in versatz_ankunft_anschlussfahrt:
        versatz_ankunft_anschlussfahrt_entry.config(state="disabled")

    for haltestellennummern_entry in haltestellennummern_alle_schulen:
        haltestellennummern_entry.config(state="disabled")

    for schüleranzahl_entry in schüleranzahlen:
        schüleranzahl_entry.config(state="disabled")

    for checkbutton in checkbuttons:
        checkbutton.config(state="disabled")


# Diese Methode wird aufgerufen, wenn von Tab 2 zu 3 gewechselt wird
def wechsel_tab2_tab3():
    notebook.select(tab3)
    button_wechsel_tab2_tab3.configure(state=tk.DISABLED)
    # für jede Haltestelle muss angegeben werden, wie viele Busse zu dieser Haltestelle fahren diese Angaben werden
    # in der Liste anzahl_busse_je_haltestelle gespeichert
    for i in range(int(entry_anzahl_haltestellen.get())):
        label_anzahl_busse_pro_haltestelle = ttk.Label(scrollable_tab3.scrollable_frame,
                                                       text=f'Anzahl Busse zu Haltestelle {i + 1}',
                                                       font=("Helvetica", 10))
        label_anzahl_busse_pro_haltestelle.grid(column=0, row=i, padx=5, pady=5)
        entry_anzahl_busse_pro_haltestelle = ttk.Entry(scrollable_tab3.scrollable_frame)
        entry_anzahl_busse_pro_haltestelle.grid(column=1, row=i, padx=5, pady=5)
        anzahl_busse_je_haltestelle.append(entry_anzahl_busse_pro_haltestelle)


# mit dem button_wechsel_tab3_tab4 wird Tab4 geöffnet in welchem die Fahrzeiten eingetragen werden
def wechsel_tab3_tab4():
    # die entry-Felder aus Tab3 werden ausgegraut
    for entry_anzahl_busse_pro_haltestelle in anzahl_busse_je_haltestelle:
        entry_anzahl_busse_pro_haltestelle.config(state="disabled")
    notebook.select(tab4)
    button_wechsel_tab3_tab4.configure(state=tk.DISABLED)
    # Erklärungen zur korrekten Angabe der Fahrzeiten
    label_erklärung_angabe_fahrzeit1 = ttk.Label(scrollable_tab4.scrollable_frame,
                                                 text="Die Fahrzeit von einer Schule zum Routenstart zu einer anderen"
                                                      " Schule muss mit einem Navigator ermittelt werden",
                                                 font=("Helvetica", 10))
    label_erklärung_angabe_fahrzeit1.grid(column=0, row=0)
    label_erklärung_angabe_fahrzeit2 = ttk.Label(scrollable_tab4.scrollable_frame,
                                                 text="Dieser Wert wird mit der Fahrzeit einer entsprechenden "
                                                      "Routenzeit addiert. Diese muss dem aktuellen Fahrplan entnommen"
                                                      " werden.\n\n " + "-"*180, font=("Helvetica", 10))

    label_erklärung_angabe_fahrzeit2.grid(column=0, row=1)
    # Die eigentliche Angabe der Fahrzeiten erfolgt mit dieser Methode
    fahrzeiten_eintragen(entry_anzahl_haltestellen, anzahl_busse_je_haltestelle, scrollable_tab4, entry_fahrzeiten,
                         fahrzeiten)


# Mit dem button_berechnung_starten in tab 4 wird diese Methode gestartet
def berechnung_starten_ladeprozess():
    # dies ermöglicht, dass der Prozess trotz langem Ladens nicht abstürzt die methode berechnung_starten wird
    # automatisch mitgestartet
    t1 = Thread(target=berechnung_starten)
    t1.start()


def berechnung_starten():
    # der Button und die entry-Felder in Tab 4 werden ausgegraut
    button_berechnung_starten.configure(state=tk.DISABLED)
    for entry_fahrzeit in entry_fahrzeiten:
        entry_fahrzeit.config(state="disabled")
    notebook.select(tab5)

    # das label_es_lädt wird angezeigt bis alle Ergebnisse (Busankunftskombinationen und Unterrichtsbgeinnkombinationen
    # mit hoher Buseinaprung) dargestellt sind
    label_es_lädt = ttk.Label(text="Es lädt ...", font=("Helvetica", 20, "bold"))
    label_es_lädt.pack()

    # die Liste fahrzeiten wird finalisiert, indem die zuvor gesetzten Platzhalter "0" durch die entry-Werte ersetzt
    # werden
    for i in range(len(fahrzeiten)):
        if fahrzeiten[i] == 0:
            fahrzeiten[i] = int(entry_fahrzeiten.pop(0).get())

    anzahl_busse_ohne_staffelung = sum(int(entry.get()) for entry in anzahl_busse_je_haltestelle)
    # mit dieser Methode werden alle Kombinationen an busankunftszeiten erstellt, die zulässig sind
    zulässige_kombinationen_busankünfte = erstellung_kombination_busankunft(anzahl_schulen,
                                                                            aktueller_unterrichtsbeginn_alle_schulen,
                                                                            versatz_ankunft_anschlussfahrt,
                                                                            wegdauern_haltestelle_schule,
                                                                            haltestellennummern_alle_schulen)

    anzahl_busse_je_haltestelle_int = [int(entry.get()) for entry in anzahl_busse_je_haltestelle]
    # mit dieser Methode wird für jede zulässige kombination an busankunftszeiten eine matrix erstellt
    matrizen = matrizenerstellung(zulässige_kombinationen_busankünfte, entry_anzahl_haltestellen,
                                  anzahl_busse_ohne_staffelung, fahrzeiten, anzahl_busse_je_haltestelle_int)

    # für jede Matrix wird berechnet wie viele Busse mit dieser eingespart werden können
    for matrix in matrizen:
        anzahl_busse_je_haltestelle_zählvariable = []
        for i in range(len(anzahl_busse_je_haltestelle_int)):
            anzahl_busse_je_haltestelle_zählvariable.append(0)
        anzahl_wiedergenutzer_busse = 0
        anzahl_busse_je_haltestelle_int = [int(entry.get()) for entry in anzahl_busse_je_haltestelle]
        anzahl_busse_je_haltestelle_unverbraucht = anzahl_busse_je_haltestelle_int.copy()
        anzahl_busse_je_haltstelle_maximal = anzahl_busse_je_haltestelle_int.copy()
        anzahl_busse_wiedernutzbar_je_kombination = matrizenbearbeitung(matrix, anzahl_busse_je_haltestelle_int,
                                                                        anzahl_busse_je_haltestelle_unverbraucht,
                                                                        anzahl_busse_je_haltestelle_zählvariable,
                                                                        anzahl_busse_je_haltstelle_maximal,
                                                                        anzahl_wiedergenutzer_busse)
        busse_wiedernutzbar.append(anzahl_busse_wiedernutzbar_je_kombination)

    # Bestimmung ab wann eine Buseinsparung hoch ist
    anzahl_einwohner = int(entry_anzahl_bewohner.get())
    teiler = 83300000 / anzahl_einwohner
    mindestbuseinsparung_hohe_einsparung = int(19600 * 1.15 / teiler) + 1

    # Bestimmung der Inidzies für Varianten mit hohem Einspapotenzial
    busse_wiedernutzbar_maximalwerte = max(busse_wiedernutzbar)
    indizes_busankunftsvarianten_hohe_einsparung = []  # die Liste erhält nach der for-Schleife die Indizes für die
    # Kombinationen hoher Buseinsparpotenzials. Die Angaben sind als Listen in Listen gespeichert (eine Liste pro Anzahl
    # wiedernutzbarer Busse)
    for durchläufe1 in range(busse_wiedernutzbar_maximalwerte - mindestbuseinsparung_hohe_einsparung + 1):
        # Neue Liste für jeden Durchlauf erstellen
        indices = [i for i, x in enumerate(busse_wiedernutzbar) if x == busse_wiedernutzbar_maximalwerte - durchläufe1]
        indizes_busankunftsvarianten_hohe_einsparung.append(indices)

    #  Ausgabe der Busankunftszeiten und Unterrichtsbeginnzeiten
    label_ergebnisse = ttk.Label(scrollable_tab5.scrollable_frame, text="Ergebnisse", font=("Helvetica", 12, "bold"))
    label_ergebnisse.grid()
    # Allgemeinen Ergebnisse
    label_anzahl_busse_ohne_staffelung = ttk.Label(scrollable_tab5.scrollable_frame,
                                                   text=f"Ohne Staffelung der Unterrichtszeiten werden "
                                                        f"{anzahl_busse_ohne_staffelung} Busse benötigt",
                                                   font=("Helvetica", 10))
    label_anzahl_busse_ohne_staffelung.grid()
    label_maximale_einsparung = ttk.Label(scrollable_tab5.scrollable_frame, font=("Helvetica", 10),
                                          text=f"Es können maximal {max(busse_wiedernutzbar)} Busse eingespart werden")
    label_maximale_einsparung.grid()
    label_hohe_einsparung = ttk.Label(scrollable_tab5.scrollable_frame, text=f"Ein hohes Einsparpotenzial wird ab "
                                                                             f"{mindestbuseinsparung_hohe_einsparung} "
                                                                             f"Bussen erreicht", font=("Helvetica", 10))
    label_hohe_einsparung.grid()
    label_trennstrich = tk.Label(scrollable_tab5.scrollable_frame, text="-"*150, font=("Helvetica", 10))
    label_trennstrich.grid()
    # Erklärung zum Verständnis der Ausgaben
    label_erklärung_buseinsparung1 = ttk.Label(scrollable_tab5.scrollable_frame,
                                               text="Die erste angegebene Zeit ist die Busankunftszeit an Haltestelle "
                                                    "Nummer 1 (angegeben in Minuten nach 7).", font=("Helvetica", 10))
    label_erklärung_buseinsparung1.grid()
    label_erklärung_buseinsparung2 = ttk.Label(scrollable_tab5.scrollable_frame,
                                               text="Es folgt die Busankunftszeit an Haltestelle 2 usw.. Analog dazu "
                                                    "wird bei den Unterrichtsbeginnzeiten als erstes",
                                               font=("Helvetica", 10))
    label_erklärung_buseinsparung2.grid()
    label_erklärung_buseinsparung3 = ttk.Label(scrollable_tab5.scrollable_frame, font=("Helvetica", 10),
                                               text="der Unterrichtsbeginn an Schule 1, dann an Schule 2 usw." +
                                                    "(ebenfalls in Minuten nach 7) angegeben\n\n " + "-"*150)
    label_erklärung_buseinsparung3.grid()
    # Ausgabe der Busankunftszeiten und Unterrrichtszeiten für hohes Einsarpotenzial
    for durchlaeufe2 in range(busse_wiedernutzbar_maximalwerte - mindestbuseinsparung_hohe_einsparung + 1):
        # zu allen Kombinationen wird angegeben, wie viele Busse eingespart werden können
        label_einsparungen = ttk.Label(scrollable_tab5.scrollable_frame, font=("Helvetica", 10, "bold"),
                                       text=f"Mit folgenden Varianten werden {busse_wiedernutzbar_maximalwerte - 
                                                                              durchlaeufe2} Busse gespart")
        label_einsparungen.grid()
        # Ausgabe der Busankunftszeiten
        for q in indizes_busankunftsvarianten_hohe_einsparung[durchlaeufe2]:
            label_kombinationen = ttk.Label(scrollable_tab5.scrollable_frame, font=("Helvetica", 10),
                                            text=f"Busankunftszeiten:"
                                                 f" {', '.join(map(str, zulässige_kombinationen_busankünfte[q]))}")
            label_kombinationen.grid()
            kombinationen_buseinkünfte_hohe_einsparung.append(zulässige_kombinationen_busankünfte[q])

            kombinationen_unterrichtsbeginnzeiten = []
            for inner_list in zulässige_kombinationen_busankünfte:

                # erstellt eine Liste mit busankunftszeiten für alle Schulen
                busankunftszeiten_alle_schulen = []
                unterrichtsbeginn_alle_schulen_eine_kombination = []

                haltestellennummern_int = [int(entry.get()) for entry in haltestellennummern_alle_schulen]

                # für jede Schule wird basierend auf die Ankunftszeit, den Versatz und die Wegezeit die neue
                # Unterrichtszeit bestimmt
                for schule in range(int(anzahl_schulen.get())):
                    haltestelle = haltestellennummern_int[schule] - 1
                    ankunftszeit = inner_list[haltestelle]
                    busankunftszeiten_alle_schulen.append(ankunftszeit)
                    unterrichtsbeginn_aktuelle_schule = int(wegdauern_haltestelle_schule[schule].get()) + int(
                        versatz_ankunft_anschlussfahrt[schule].get()) + ankunftszeit
                    unterrichtsbeginn_alle_schulen_eine_kombination.append(unterrichtsbeginn_aktuelle_schule)
                kombinationen_unterrichtsbeginnzeiten.append(unterrichtsbeginn_alle_schulen_eine_kombination)

            # Ausgabe der Unterrichtsbeginnzeiten
            label_unterrichtsbeginn = ttk.Label(scrollable_tab5.scrollable_frame,
                                                text="Unterrichtsbeginn an den Schulen: " +
                                                     ', '.join(map(str, kombinationen_unterrichtsbeginnzeiten[q])),
                                                font=("Helvetica", 10))
            label_unterrichtsbeginn.grid()
            label_trennstrich = ttk.Label(scrollable_tab5.scrollable_frame,
                                          text="-"*81)
            label_trennstrich.grid()

    # der Ladeprozess ist abgeschlossen und der button_akzeptanzbewertung_anzeigen wird freigeschalten
    label_es_lädt.destroy()
    button_akzeptanzbewertung_anzeigen.configure(state=tk.NORMAL)


def akzeptanzbewertung_anzeigen_ladeprozess():
    # button_akzeptanzbewertung_anzeigen startet erstmal diesen Prozess, damit die Akzeptanzbewertung nicht abstürzt
    t2 = Thread(target=akzeptanzbewertung_anzeigen)
    t2.start()


def akzeptanzbewertung_anzeigen():
    # wird indirekt über den button_akzeptanzbewertung_anzeigen gestartet, da diese Methode mit der Methode
    # "akzeptanzbewertung_anzeigen_ladeprozess" auch startet
    notebook.select(tab6)
    button_akzeptanzbewertung_anzeigen.configure(state=tk.DISABLED)

    # wird während dem Ladeprozess angezeigt
    label_lädt_akzeptanz = ttk.Label(scrollable_tab6.scrollable_frame, text="Es lädt ...",
                                     font=("Helvetica", 20, "bold"))
    label_lädt_akzeptanz.pack()

    # Methode gibt eine Liste mit den Akzeptanzmittelwerten aller getesteten varianten aus
    gesamtmittelwerte_akzeptanzbewertung = akzeptanzbewertung_rechnen(merkmale_alle_schulen,
                                                                      kombinationen_buseinkünfte_hohe_einsparung,
                                                                      entry_anzahl_schulen,
                                                                      haltestellennummern_alle_schulen,
                                                                      versatz_ankunft_anschlussfahrt,
                                                                      wegdauern_haltestelle_schule,
                                                                      aktueller_unterrichtsbeginn_alle_schulen)
    # bestimmt den höchsten Wert der Akzeptanzbepunktung
    max_punkte = max(gesamtmittelwerte_akzeptanzbewertung)
    max_punkte_gerundet = round(max_punkte, 3)
    # bestimmt die Indizes der Stellen an denen der maximale Wert erreicht wird
    indices_of_highest_value = [i for i, x in enumerate(gesamtmittelwerte_akzeptanzbewertung) if x == max_punkte]

    # Ausgabe der Akzeptanzbepunktung
    label_höchste_punktzahl_akzeptanz = ttk.Label(scrollable_tab6.scrollable_frame,
                                                  text=f"Die höchste Akzeptanzpunktzahl beträgt {max_punkte_gerundet}."
                                                       f"Diese kann mit folgenden Varianten erreicht werden:",
                                                  font=("Helvetica", 10))
    label_höchste_punktzahl_akzeptanz.pack()
    for index in indices_of_highest_value:
        label_busankunftszeiten = ttk.Label(scrollable_tab6.scrollable_frame,
                                            text=f"Busankunftszeiten: "
                                                 f"{', '.join(map(str, 
                                                                  kombinationen_buseinkünfte_hohe_einsparung[index]))}",
                                            font=("Helvetica", 10))
        label_busankunftszeiten.pack()

    label_lädt_akzeptanz.destroy()


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
label_anzahl_haltestellen_erklärung1 = ttk.Label(scrollable_tab1.scrollable_frame,
                                                 text="(Wenn eine Haltestelle immer direkt als Anschlussfahrt von "
                                                      "einer", font=("Helvetica", 8))
label_anzahl_haltestellen_erklärung1.grid(column=0, row=3)
label_anzahl_haltestellen_erklärung2 = ttk.Label(scrollable_tab1.scrollable_frame,
                                                 text="anderen Haltestelle angefahren wird, wird diese hier NICHT "
                                                      "mitgezählt)", font=("Helvetica", 8))

label_anzahl_haltestellen_erklärung2.grid(column=0, row=4)
entry_anzahl_haltestellen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=anzahl_haltestellen_entry)
entry_anzahl_haltestellen.grid(column=0, row=5, padx=5, pady=5)

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
button_eingabe_prüfen = ttk.Button(scrollable_tab2.scrollable_frame, text="Eingaben überprüfen",
                                   command=eingabe_prüfen_main, style='Custom.TButton')
button_eingabe_prüfen.grid(column=1, row=4)
button_werteingabe_bestätigen = ttk.Button(scrollable_tab2.scrollable_frame, text="Werte eingetragen",
                                           command=werteingabe_bestätigen, state=tk.DISABLED, style='Custom.TButton')
button_werteingabe_bestätigen.grid(column=2, row=4)
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

# tab5
button_akzeptanzbewertung_anzeigen = ttk.Button(scrollable_tab5.scrollable_frame, text="Akzeptanzbewertung anzeigen",
                                                command=akzeptanzbewertung_anzeigen_ladeprozess, style='Custom.TButton',
                                                state=tk.DISABLED)
button_akzeptanzbewertung_anzeigen.grid(column=1)

# Hauptfenster ausführen
root.mainloop()
