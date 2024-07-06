import tkinter as tk
from tkinter import ttk
import itertools
from collections import Counter
from Matrizenbearbeitung_GUI import matrizenbearbeitung
from tkinter import messagebox
import csv
import pandas
import statistics
import numpy
d=pandas.read_csv('Daten_rating_system2.csv', sep=';')

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
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


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
Spaetere_Ankuenfte = []
n_ava = []
Travel_times = []
n_reuse = 0
n_reuses = []
starts = []
startzeiten = []
Startzeiten_aktuell = []
entry_aktueller_Schulbeginn = 0
Haltestellennummern=[]
Weg_Bus_Schule= []
merkmalsliste = []
Var = []
check_var_liste1=[]
check_var_liste2=[]
check_var_liste3=[]
check_var_liste4=[]
check_var_liste5=[]

Schüleranzahlen=[]
Gesamtmittelwerte =[]

def validate_and_submit():
    results = []

    try:
        # Überprüfen, ob alle Elemente in Startzeiten_aktuell durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in[int(entry.get()) for entry in Startzeiten_aktuell]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in Spaetere_Ankuenfte durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in[int(entry.get()) for entry in Spaetere_Ankuenfte]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in Weg_Bus_Schule durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in[int(entry.get()) for entry in Weg_Bus_Schule]):
            results.append(True)
        else:
            results.append(False)


    except Exception as e:
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war ungültig - bitte ändern sie die Zahlen")
        label_fehler.grid()
        del Startzeiten_aktuell[:]
        del Spaetere_Ankuenfte[:]
        del Weg_Bus_Schule[:]

    if not all (result for result in results):
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame,text="Die Eingabe war ungültig - bitte ändern sie die Zahlen")
        label_fehler.grid(column=1,row=5)
        del Startzeiten_aktuell[:]
        del Spaetere_Ankuenfte[:]
        del Weg_Bus_Schule[:]
    else:
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame,text="Die Eingabe war gültig")
        label_fehler.grid(column=1,row=5)
        merkmale_füllen.configure(state=tk.NORMAL)


    return results

# Funktionen zum Wechseln der Tabs


def tab1_2():
    notebook.select(tab2)

    anzahl_Schulen = int(entry_Anzahl_Schulen.get())
    global check_var_liste1, check_var_liste2, check_var_liste3, check_var_liste4, check_var_liste5
    check_var_liste1 = [tk.StringVar() for i in range(anzahl_Schulen)]
    check_var_liste2 = [tk.StringVar() for i in range(anzahl_Schulen)]
    check_var_liste3 = [tk.StringVar() for i in range(anzahl_Schulen)]
    check_var_liste4 = [tk.StringVar() for i in range(anzahl_Schulen)]
    check_var_liste5 = [tk.StringVar() for i in range(anzahl_Schulen)]


    for i in range(anzahl_Schulen):


        label_Schule = ttk.Label(scrollable_tab2.scrollable_frame, text=f'Schule {i + 1}')
        label_Schule.grid()

        label_aktueller_Schulbeginn = ttk.Label(scrollable_tab2.scrollable_frame,text="Aktueller Unterrrichtsbeginn in Minuten nach 7 - Dieser Wert muss durch 5 teilbar sein")
        label_aktueller_Schulbeginn.grid()
        entry_aktueller_Schulbeginn = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_aktueller_Schulbeginn.grid()
        Startzeiten_aktuell.append(entry_aktueller_Schulbeginn)


        label_Haltestellennutzung = tk.Label(scrollable_tab2.scrollable_frame,text="Welche Haltestelle nutzt die Schule? - Bitte die Angabe als Zahl eintragen "
                                                                                   "und darauf achten, dass Schulen, die die selbe Haltestelle nutzen oder direkt nacheinander angefahren werden"
                                                                                   "die selbe Nummer erhalten")
        label_Haltestellennutzung.grid()
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Haltestellennutzung.grid()
        Haltestellennummern.append(entry_Haltestellennutzung)

        label_spätere_Ankunft = tk.Label(scrollable_tab2.scrollable_frame, text=f"Muss der Unterrichtsbeginn an Schule {i + 1} später liegen, da die Haltestelle als direkte Anschlussfahrt"
                                                                                f"von einer anderen Schule angefahren wird? - Bitte als Vielfaches von 5 angeben, ansonsten 0 eintragen")
        label_spätere_Ankunft.grid()
        entry_spätere_Ankunft = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_spätere_Ankunft.grid()
        Spaetere_Ankuenfte.append(entry_spätere_Ankunft)

        label_Weg_Bus_Schule = tk.Label(scrollable_tab2.scrollable_frame,text=f"Wie viel Zeit soll bei Schule {i + 1} als Weg von der Bushaltestelle zur Schule eingeplant werden? - Bitte als Vielfaches von 5 angeben")
        label_Weg_Bus_Schule.grid()
        entry_Weg_Bus_Schule = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Weg_Bus_Schule.grid()
        Weg_Bus_Schule.append(entry_Weg_Bus_Schule)

        label_Schüleranzahl = ttk.Label(scrollable_tab2.scrollable_frame, text="Wie viele Schüler hat die Schule?")
        label_Schüleranzahl.grid()
        Schüleranzahl = ttk.Entry(scrollable_tab2.scrollable_frame)
        Schüleranzahl.grid()
        Schüleranzahlen.append(Schüleranzahl)

        label_Betreuungsangebot_morgens = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es an dieser Schule ein Betreuungsangebot vor Unterrichtsbeginn?")
        label_Betreuungsangebot_morgens.grid()
        checkbutton_Betreuung_morgens = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var_liste1[i])
        checkbutton_Betreuung_morgens.grid()

        label_Betreuungsangebot_mittags = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es an dieser Schule ein Betreuungsangebot nach Unterrichtsende?")
        label_Betreuungsangebot_mittags.grid()
        checkbutton_Betreuung_mittags = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var_liste2[i])
        checkbutton_Betreuung_mittags.grid()

        label_Mensa = ttk.Label(scrollable_tab2.scrollable_frame, text="Gibt es eine Mensa an dieser Schule?")
        label_Mensa.grid()
        checkbutton_Mensa = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var_liste3[i])
        checkbutton_Mensa.grid()

        label_andere_Lehrer = ttk.Label(scrollable_tab2.scrollable_frame, text= "Gibt es an dieser Schule auch Lehrer, die an anderen Schulen unterrichten?")
        label_andere_Lehrer.grid()
        checkbutton_andere_Lehrer = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var_liste4[i])
        checkbutton_andere_Lehrer.grid()

        label_andere_Schüler = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es an dieser Schule Schüler, die auch Fächer an anderen Schulen besuchen?")
        label_andere_Schüler.grid()
        checkbutton_andere_Schüler = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var_liste5[i])
        checkbutton_andere_Schüler.grid()

    validate_button = ttk.Button(scrollable_tab2.scrollable_frame, text="Eingaben überprüfen", command=validate_and_submit)
    validate_button.grid(column=1, row=4)


def s_merkmale_füllen():
    anzahl_Schulen = int(entry_Anzahl_Schulen.get())
    Startzeiten_aktuell_int  = []
    Startzeiten_aktuell_int = [int(entry.get()) for entry in Startzeiten_aktuell]
    Schüleranzahlen_int = [int(entry.get()) for entry in Schüleranzahlen]
    for i in range(anzahl_Schulen):
        s_merkmale=[]
        s_merkmale.append(Startzeiten_aktuell_int[i])

        if Schüleranzahlen_int[i] < 300:
            s_merkmale.append(1)
        elif Schüleranzahlen_int[i] >= 300 and Schüleranzahlen_int[i] < 500:
            s_merkmale.append(2)
        elif Schüleranzahlen_int[i] >= 500 and Schüleranzahlen_int[i] < 700:
            s_merkmale.append(3)
        elif Schüleranzahlen_int[i]  >= 700 and Schüleranzahlen_int[i]  < 900:
            s_merkmale.append(4)
        elif Schüleranzahlen_int[i]  >= 900 and Schüleranzahlen_int[i] < 1100:
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

    button_nächster_Tab2.configure(state=tk.NORMAL)





def tab2_3():
    notebook.select(tab3)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for i in range(anzahl_schulen_bus):
        row = i * 2  # Verwenden Sie die doppelte Zeilenzahl, um Platz für alle Widgets zu schaffen
        label_Haltestelle = ttk.Label(scrollable_tab3.scrollable_frame,
                                      text=f'Wie viele Busse fahren zu Haltestelle {i + 1} - bezogen auf den aktuellen Fahrplan')
        label_Haltestelle.grid(column=0, row=row, padx=5, pady=5)
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab3.scrollable_frame)
        entry_Haltestellennutzung.grid(column=1, row=row, padx=5, pady=5)
        n_ava.append(entry_Haltestellennutzung)




entry_travel_times=[]
def tab3_4():
    notebook.select(tab4)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    label_Erklärung = ttk.Label(scrollable_tab4.scrollable_frame, text="Die Fahrzeit von einer Schule zum Startpunkt einer Route zu einer anderen Route muss mit einem Navigator ermittelt werden."
                                                                       "Dieser Wert wird mit der Fahrzeit einer entsprechenden Route addiert. Dieser Wert wird aus den aktuellen Fahrplänen entnommen")
    for startpunkt in range(anzahl_schulen_bus):
        for zielpunkt in range(anzahl_schulen_bus):
            for header in range(int(n_ava[zielpunkt].get())):
                if startpunkt != zielpunkt:

                    while True:
                        label_Traveltime = ttk.Label(scrollable_tab4.scrollable_frame, text=f"Gib die Fahrzeit von Haltestelle {startpunkt + 1} über den Routenstart {header + 1} zur Haltestelle {zielpunkt + 1} an: ")
                        label_Traveltime.grid(column=0)
                        entry_Traveltime = ttk.Entry(scrollable_tab4.scrollable_frame)
                        entry_Traveltime.grid(column=0)
                        entry_travel_times.append(entry_Traveltime)
                        #travel_time = int(entry_Traveltime.get()) + Spaetere_Ankuenfte[zielpunkt].get()
                        Travel_times.append(0)  # Speichere die Fahrzeit in der Liste

                        break
                else:
                    Travel_times.append(100000000)


def Berechnung_starten():
    for i in range(len(Travel_times)):
        if Travel_times[i]==0:
            Travel_times[i]=int(entry_travel_times.pop(0).get())


    busses_needed_without = sum(int(entry.get()) for entry in n_ava)
    progress_var=0
    maximum=100#Zahl flexibel
    progress_bar=ttk.Progressbar(tab5, variable=progress_var, maximum=maximum)
    progress_bar.pack()

    Busankunftszeiten_alle_Schulen_aktuell = []

    for i in range(int(anzahl_schulen.get())):
        Busankunft_aktuell = int(Startzeiten_aktuell[i].get()) - int(Spaetere_Ankuenfte[i].get()) - int(Weg_Bus_Schule[i].get())
        Busankunftszeiten_alle_Schulen_aktuell.append(Busankunft_aktuell)

    # Hier wird für jede Schule gespeichert, in welchem Zeitkorridor der Bus an der Planungshaltestelle ankommen muss

    print("Busankunftszeiten_alle_Schulen_aktuell", Busankunftszeiten_alle_Schulen_aktuell)
    Busankunftszeiten_alle_schule_zulässig = []
    for i in range(int(anzahl_schulen.get())):
        Busankunft_aktuell = Startzeiten_aktuell[i]
        Startzeiten_Korridor_zulässig = []

        if int(Startzeiten_aktuell[i].get()) < 40:
            Startzeiten_Korridor_zulässig.extend(
                [Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 20, Busankunftszeiten_alle_Schulen_aktuell[i] + 25,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 30, Busankunftszeiten_alle_Schulen_aktuell[i] + 35,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 40])
        elif int(Startzeiten_aktuell[i].get()) >= 40 and int(Startzeiten_aktuell[i].get()) < 55:
            Startzeiten_Korridor_zulässig.extend(
                [Busankunftszeiten_alle_Schulen_aktuell[i] - 10, Busankunftszeiten_alle_Schulen_aktuell[i] - 5,
                 Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 20])
        else:
            Startzeiten_Korridor_zulässig.extend(
                [Busankunftszeiten_alle_Schulen_aktuell[i] - 10, Busankunftszeiten_alle_Schulen_aktuell[i] - 5,
                 Busankunftszeiten_alle_Schulen_aktuell[i], Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                 Busankunftszeiten_alle_Schulen_aktuell[i] + 10, Busankunftszeiten_alle_Schulen_aktuell[i] + 15])
        Busankunftszeiten_alle_schule_zulässig.append(Startzeiten_Korridor_zulässig)

    print("Busankunftszeiten_alle_schule_zulässig", Busankunftszeiten_alle_schule_zulässig)

    Busankunftszeit_Haltestelle = []

    i = 0
    for i in range(int(anzahl_schulen.get())):
        Haltestellennummern_int = [int(entry.get()) for entry in Haltestellennummern]
        if Haltestellennummern_int.count(i + 1) == 1:
            index = Haltestellennummern_int.index(i + 1)
            Busankunftszeit_Haltestelle.append(Busankunftszeiten_alle_schule_zulässig[index])
        else:
            ausgewählte_Busankunftszeiten = []
            for j, busankunftszeit in enumerate(Busankunftszeiten_alle_schule_zulässig):
                if Haltestellennummern_int[j] == i + 1:
                    ausgewählte_Busankunftszeiten.append(busankunftszeit)
            if ausgewählte_Busankunftszeiten:
                # Berechne die Schnittmenge (Intersection) der ausgewählten Busankunftszeiten
                intersection_result = set(ausgewählte_Busankunftszeiten[0]).intersection(
                    *ausgewählte_Busankunftszeiten[1:])
                Busankunftszeit_Haltestelle.append(list(intersection_result))

    print("Busankunftszeit_Haltestelle", Busankunftszeit_Haltestelle)
    matrizen = []
    schoolstart_combination = []
    combinations = list(itertools.product(*Busankunftszeit_Haltestelle))
    n_ava_values = [int(entry.get()) for entry in n_ava]


    for combination in combinations:
        print("Current combination:", combination)
        matrix = [[0 for _ in range(int(Anzahl_Haltestellen_entry_value.get()))] for _ in range(busses_needed_without)]
        t = 0

        for col in range(int(Anzahl_Haltestellen_entry_value.get())):  # Schleife über die Spalten
            zielpunkt = 0
            p = 0

            for row in range(busses_needed_without):  # Schleife über die Zeilen, begrenzt auf busses_needed_without
                if zielpunkt >= len(combination):
                    break

                print(f"combination: {combination}")
                print(f"Travel_times: {Travel_times}")
                print(f"col: {col}, t: {t}, zielpunkt: {zielpunkt}")
                print(f"combination[col]: {combination[col]}")
                print(f"combination[zielpunkt]: {combination[zielpunkt]}")

                if int(combination[col]) + int(Travel_times[t]) <= int(combination[zielpunkt]):
                    matrix[row][col] = 1  # Hier wird das Element gesetzt, Beachte die Zeilen und Spalten vertauschen
                    print("+1")
                t += 1

                p += 1
                if p == n_ava_values[zielpunkt]:
                    print("zielpunkt vor Erhöhung:", zielpunkt)
                    zielpunkt += 1
                    p = 0

        print(f"Combination: {combination}, Result: {matrix}")
        matrizen.append(matrix)
        schoolstart_combination.append(combination)

    from Matrizenbearbeitung_GUI import matrizenbearbeitung
    for matrix in matrizen:
        print('neuer Durchlauf')
        max_anfahrten = []
        for i in range(len(n_ava_values)):
            max_anfahrten.append(0)
        n_reuse = 0
        n_ava_values = [int(entry.get()) for entry in n_ava]
        n_ava_unverbraucht = n_ava_values.copy()
        n_anfahrten = n_ava_values.copy()
        n_reuse_einzel = matrizenbearbeitung(matrix, n_ava_values, n_ava_unverbraucht, n_reuse, max_anfahrten, n_anfahrten)
        n_reuses.append(n_reuse_einzel)

    print(n_reuses)

    Anzahl_Einwohner = int(entry_Anzahl_Bewohner.get())

    Teiler = 83300000 / Anzahl_Einwohner
    Busse_hohes_Einsparpotenzial = int(19600 * 1.15 / Teiler) + 1
    print(Busse_hohes_Einsparpotenzial)




    max_reuses = max(n_reuses)

    indices_of_values = []

    # Berechnen und Ausgeben, solange die Einsparung nicht hoch genug ist
    for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial + 1):
        # Neue Liste für jeden Durchlauf erstellen
        indices = [i for i, x in enumerate(n_reuses) if x == max_reuses - Durchläufe]
        indices_of_values.append(indices)  # Diese Liste in indices_of_values sammeln
        print("Durchläufe", Durchläufe)
        print("max_reuses-Busse hohes Einsparpotenzial", max_reuses - Busse_hohes_Einsparpotenzial)

    print(indices_of_values)





    Gesamtmittelwerte = []

    print(Busankunftszeit_Haltestelle)


    print(merkmalsliste)
    notebook.select(tab6)
    # Tab6
    label_anzahl_ohne_Staffelung=ttk.Label(scrollable_tab6.scrollable_frame, text=f"Ohne Staffelung der Unterrichtszeiten werden {busses_needed_without} Busse benötigt")
    label_anzahl_ohne_Staffelung.grid()
    label_maximale_Einsparung = ttk.Label(scrollable_tab6.scrollable_frame,text=f"Es können maximal {max(n_reuses)}Busse eingespart werden")
    label_maximale_Einsparung.grid()
    label_hohe_Einsparung = ttk.Label(scrollable_tab6.scrollable_frame,text=f"Ein hohes Einsparpotenzial wird ab{Busse_hohes_Einsparpotenzial} erreicht")
    label_hohe_Einsparung.grid()
    Durchläufe = 0
    # Ausgabe der Ergebnisse für die restlichen höchsten Werte
    for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial + 1):
        label_Einsparungen=ttk.Label(scrollable_tab6.scrollable_frame,text=f"Mit folgenden Varianten werden {max_reuses - Durchläufe} Busse gespart")
        label_Einsparungen.grid()

        for q in indices_of_values[Durchläufe]:
            label_Kombinationen=ttk.Label(scrollable_tab6.scrollable_frame, text= f"{"Busankunftszeiten:",schoolstart_combination[q]}")
            label_Kombinationen.grid()
            Var.append(schoolstart_combination[q])

            Unterrichtsbeginn=[]
            Busankunft_Liste_Alle_Schulen= []

            for i, inner_list in enumerate(schoolstart_combination):
                nummer = i + 1  # Nummern basieren auf dem Index
                anzahl = int(Haltestellennummern.get()).count(nummer)

                # Füge die Elemente der inneren Liste so oft zur Zielliste hinzu, wie die Anzahl der Nummern
                for _ in range(anzahl):
                    Busankunft_Liste_Alle_Schulen.extend(inner_list)

            print(Busankunft_Liste_Alle_Schulen)
            for i in range (int(entry_Anzahl_Schulen.get())):
                Unterrischtsbeginn_1_Schule = int(Weg_Bus_Schule[i].get())+int(Spaetere_Ankuenfte[i].get())+int(Busankunft_Liste_Alle_Schulen[i].get())
                Unterrichtsbeginn.append(Unterrischtsbeginn_1_Schule)

            label_Unterrichtsbeginn=ttk.Label(scrollable_tab6.scrollable_frame, text=f"Unterrichtsbeginn an den Schulen: {Unterrichtsbeginn}")
            label_Unterrichtsbeginn.grid()





def Akzeptanzbewertung_anzeigen():

    for Variante in Var:
        s_change_values = []
        anzahl_schulen=int(entry_Anzahl_Schulen.get())
        for i in range(anzahl_schulen):
            index = int(Haltestellennummern[i].get())
            s_change = Variante[index - 1] + int(Spaetere_Ankuenfte[i].get()) + int(Weg_Bus_Schule[i].get()) - int(Startzeiten_aktuell[i].get())
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

        # Ahängigkeit Lehrer an anderen Schule
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Lehrer_Leistungen = d.query('Lehrer_an_anderer_Schule == @merkmale[5]')

            i = get_index_Leistungen(s_change)

            if Lehrer_Leistungen.shape[1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Lehrer_Leistungen.iloc[:, i].mean()
                Leistungen.append(mean_value)
            else:
                Leistungen.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Ahängigkeit Schüler an anderen Schule
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

            if Schueleranzahl_Betreuungspersonal.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Schueleranzahl_Betreuungspersonal.iloc[:, i].mean()
                Betreuungspersonal.append(mean_value)
            else:
                Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Ahängigkeit der Betreeung morgens
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Betreuung_morgens_Betreuungspersonal = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

            i = get_index_Betreuungspersonal(s_change)

            if Betreuung_morgens_Betreuungspersonal.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Betreuung_morgens_Betreuungspersonal.iloc[:, i].mean()
                Betreuungspersonal.append(mean_value)
            else:
                Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Ahängigkeit der Betreeung mittags
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Betreuung_mittags_Betreuungspersonal = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

            i = get_index_Betreuungspersonal(s_change)

            if Betreuung_mittags_Betreuungspersonal.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

            if Lehrer_Betreuungspersonal.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Lehrer_Betreuungspersonal.iloc[:, i].mean()
                Betreuungspersonal.append(mean_value)
            else:
                Betreuungspersonal.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Ahängigkeit Schüler an anderen Schule
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Schueler_Betreuungspersonal = d.query('Schueler_an_anderer_Schule == @merkmale[6]')

            i = get_index_Betreuungspersonal(s_change)

            if Schueler_Betreuungspersonal.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

            if Schueleranzahl_Kinderbetreuung.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

            if Unterrichtsbeginn_Selbstaktiv.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Unterrichtsbeginn_Selbstaktiv.iloc[:, i].mean()
                Selbstaktiv.append(mean_value)
            else:
                Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Abhängigkeit der Schüleranzahl
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Schueleranzahl_Selbstaktiv = d.query('Schueleranzahl == @merkmale[1]')

            i = get_index_Selbstaktiv(s_change)

            if Schueleranzahl_Selbstaktiv.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Schueleranzahl_Selbstaktiv.iloc[:, i].mean()
                Selbstaktiv.append(mean_value)
            else:
                Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Abhängigkeit der Betreuung morgens
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Betreuung_morgens_Selbstaktiv = d.query('Betreuung_vor_Unterricht == @merkmale[2]')

            i = get_index_Selbstaktiv(s_change)

            if Betreuung_morgens_Selbstaktiv.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
                mean_value = Betreuung_morgens_Selbstaktiv.iloc[:, i].mean()
                Selbstaktiv.append(mean_value)
            else:
                Selbstaktiv.append(None)  # Wenn der Index außerhalb des Bereichs liegt, füge None hinzu

        # Abhängigkeit der Betreuung mittags
        for idx, merkmale in enumerate(merkmalsliste):
            s_change = s_change_values[idx]
            Betreuung_mittags_Selbstaktiv = d.query('Betreuung_nach_Unterricht == @merkmale[3]')

            i = get_index_Selbstaktiv(s_change)

            if Betreuung_mittags_Selbstaktiv.shape[
                1] > i:  # Sicherstellen, dass der Index innerhalb der Spaltenanzahl liegt
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

        print("Leistungen" + str(Leistungen))
        print("Betreuungspersonal" + str(Betreuungspersonal))
        print("Kinderbetreuung" + str(Kinderbetreuung))
        print("Selbstaktiv" + str(Selbstaktiv))
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

        Gesamtmittelwert = statistics.mean(
            [Leistungen_finaler_wert, Betreuungspersonal_finaler_wert, Kinderbetreuung_finaler_wert, Selbstaktiv_finaler_wert])
        print("Variante", Variante)
        print("Auswirkungen auf Leistungen Gesamtwert:", Leistungen_finaler_wert)
        print("Auswirkungen auf Betreuungspersonal Gesamtwert:", Betreuungspersonal_finaler_wert)
        print("Auswirkungen auf Kinderbetreuung Gesamtwert:", Kinderbetreuung_finaler_wert)
        print("Auswirkungen auf Selbstaktivität Gesamtwert:", Selbstaktiv_finaler_wert)
        print("Gesamtmittelwert:", Gesamtmittelwert)
        Gesamtmittelwerte.append(Gesamtmittelwert)

    max_punkte = max(Gesamtmittelwerte)

    indices_of_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == max_punkte]
    notebook.select(tab7)
    label_höchste_Punktzahl =ttk.Label(scrollable_tab7.scrollable_frame, text=f"Die höchste Akzeptanzpunktzhal lautet {max_punkte}. Diese kann mit folgenden Varianten erreicht werden:")
    label_höchste_Punktzahl.grid()
    for index in indices_of_highest_value:
        label_Variante = ttk.Label(scrollable_tab7.scrollable_frame, text=f"{Var[index]}")
        label_Variante.grid()




# Tab1
Anzahl_Schulen_entry_value = tk.StringVar(value="0")
label_Anzahl_Schulen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Schulen im Untersuchungsgebiet, die vom Busverkehr bedient werden", font=("Helvetica",10, "bold"))
label_Anzahl_Schulen.grid(column=0, row=0, padx=5, pady=5)
entry_Anzahl_Schulen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Schulen_entry_value)
entry_Anzahl_Schulen.grid(column=0, row=1, padx=5, pady=5)
anzahl_schulen=entry_Anzahl_Schulen

Anzahl_Haltestellen_entry_value = tk.StringVar(value="0")
label_Anzahl_Haltestellen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Haltestellen für Schülerverkehr im Untersuchungsgebiet ",  font=("Helvetica",10, "bold"))
label_Anzahl_Haltestellen.grid(column=0, row=2, padx=5, pady=5)
label_Anzahl_Haltestellen_Erklärung = ttk.Label(scrollable_tab1.scrollable_frame,
                                      text="(wenn eine Haltestelle immer direkt als Anschlussfahrt von einer anderen \n\n"
                                           "Haltestelleangefahren wird, wird diese hier NICHT mitgezählt)", font=("Helvetica",8))
label_Anzahl_Haltestellen_Erklärung.grid(column=0, row=3)
entry_Anzahl_Haltestellen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Haltestellen_entry_value)
entry_Anzahl_Haltestellen.grid(column=0, row=4, padx=5, pady=5)

Anzahl_Bewohner_entry_value = tk.StringVar(value="0")
label_Anzahl_Bewohner = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Bewohner im Untersuchungsgebiet",  font=("Helvetica",10, "bold"))
label_Anzahl_Bewohner.grid(column=0, row=5, padx=5, pady=5)
entry_Anzahl_Bewohner = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Bewohner_entry_value)
entry_Anzahl_Bewohner.grid(column=0, row=6, padx=5, pady=5)

button_nächster_Tab1 = ttk.Button(scrollable_tab1.scrollable_frame, text="Nächster Schritt", command=tab1_2)
button_nächster_Tab1.grid(column=1, row=0, padx=5, pady=5)

# Tab2
merkmale_füllen= ttk.Button(scrollable_tab2.scrollable_frame, text="Werte eingetragen",command=s_merkmale_füllen, state=tk.DISABLED)
merkmale_füllen.grid(column=2, row=4)
button_nächster_Tab2 = ttk.Button(scrollable_tab2.scrollable_frame, text="Nächster Schritt", command=tab2_3, state=tk.DISABLED)
button_nächster_Tab2.grid(column=3, row=4, padx=5, pady=5)

# Tab3
button_nächster_Tab3 = ttk.Button(scrollable_tab3.scrollable_frame, text="Nächster Schritt", command=tab3_4)
button_nächster_Tab3.grid(column=2, row=3, padx=5, pady=5)

# Tab4
Berechnung_starten = ttk.Button(scrollable_tab4.scrollable_frame, text="Berechnung starten", command=Berechnung_starten)
Berechnung_starten.grid(column=2, row=3, padx=5, pady=5)

#Tab6
Akzeptanz_ergebnis_anzeigen =ttk.Button(scrollable_tab6.scrollable_frame, text="Akzeptanzbewertung anzeigen", command=Akzeptanzbewertung_anzeigen)
Akzeptanz_ergebnis_anzeigen.grid()




# Hauptfenster ausführen
root.mainloop()
