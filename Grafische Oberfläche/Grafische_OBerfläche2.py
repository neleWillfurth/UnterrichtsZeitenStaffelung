import tkinter as tk
from tkinter import ttk
import itertools
from collections import Counter
from Matrizenbearbeitung_GUI import matrizenbearbeitung
from tkinter import messagebox

# Hauptfenster erstellen
root = tk.Tk()
root.title("GUI mit 7 Tabs")

# Tab-Control erstellen
notebook = ttk.Notebook(root)  # Organisation der Tabs

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)

notebook.add(tab1, text="Allgemeine Angaben")
notebook.add(tab2, text="Angaben zu den Schulen")
notebook.add(tab3, text="Angaben zu den Haltestellen")
notebook.add(tab4, text="Angabe der Fahrzeiten")
notebook.add(tab5, text="Rechenfortschritt")
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
Haltestellennummern=[]
Weg_Bus_Schule= []
merkmalsliste = []
check_var1=tk.StringVar()
check_var2=tk.StringVar()
check_var3=tk.StringVar()
check_var4=tk.StringVar()
check_var5=tk.StringVar()
Schüleranzahl=0
# Funktionen zum Wechseln der Tabs
def tab1_2():
    notebook.select(tab2)
    anzahl_Schulen = int(entry_Anzahl_Schulen.get())
    for i in range(anzahl_Schulen):
        s_merkmale=[]

        label_Schule = ttk.Label(scrollable_tab2.scrollable_frame, text=f'Schule {i + 1}')
        label_Schule.grid()

        label_aktueller_Schulbeginn = ttk.Label(scrollable_tab2.scrollable_frame,text="Aktueller Schulbeginn in Minuten nach 7")
        label_aktueller_Schulbeginn.grid()
        entry_aktueller_Schulbeginn = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_aktueller_Schulbeginn.grid()
        Startzeiten_aktuell.append(entry_aktueller_Schulbeginn)

        label_Haltestellennutzung = tk.Label(scrollable_tab2.scrollable_frame,text="Welche Haltestelle nutzt die Schule?")
        label_Haltestellennutzung.grid()
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Haltestellennutzung.grid()
        Haltestellennummern.append(entry_Haltestellennutzung)

        label_spätere_Ankunft = tk.Label(scrollable_tab2.scrollable_frame, text=f"Muss der Schulstart an Schule {i + 1} später liegen ...")
        label_spätere_Ankunft.grid()
        entry_spätere_Ankunft = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_spätere_Ankunft.grid()
        Spaetere_Ankuenfte.append(entry_spätere_Ankunft)

        label_Weg_Bus_Schule = tk.Label(scrollable_tab2.scrollable_frame,text=f"Wie viel Zeit soll bei Schule {i + 1} ...")
        label_Weg_Bus_Schule.grid()
        entry_Weg_Bus_Schule = ttk.Entry(scrollable_tab2.scrollable_frame)
        entry_Weg_Bus_Schule.grid()
        Weg_Bus_Schule.append(entry_Weg_Bus_Schule)

        label_Schüleranzahl = ttk.Label(scrollable_tab2.scrollable_frame, text="Wie viele Schüler hat die Schule?")
        label_Schüleranzahl.grid()
        Schüleranzahl = ttk.Entry(scrollable_tab2.scrollable_frame)
        Schüleranzahl.grid()

        label_Betreuungsangebot_morgens = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es ein Betreuungsangebot morgens?")
        label_Betreuungsangebot_morgens.grid()
        checkbutton_Betreuung_morgens = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var1)
        checkbutton_Betreuung_morgens.grid()

        label_Betreuungsangebot_mittags = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es ein Betreuungsangebot mittags?")
        label_Betreuungsangebot_mittags.grid()
        checkbutton_Betreuung_mittags = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var2)
        checkbutton_Betreuung_mittags.grid()

        label_Mensa = ttk.Label(scrollable_tab2.scrollable_frame, text="Gibt es eine Mensa?")
        label_Mensa.grid()
        checkbutton_Mensa = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var3)
        checkbutton_Mensa.grid()

        label_andere_Lehrer = ttk.Label(scrollable_tab2.scrollable_frame, text="Gibt es Lehrer, die an anderen Schulen unterrichten?")
        label_andere_Lehrer.grid()
        checkbutton_andere_Lehrer = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var4)
        checkbutton_andere_Lehrer.grid()

        label_andere_Schüler = ttk.Label(scrollable_tab2.scrollable_frame,text="Gibt es Schüler, die auch Fächer an anderen Schulen besuchen?")
        label_andere_Schüler.grid()
        checkbutton_andere_Schüler = ttk.Checkbutton(scrollable_tab2.scrollable_frame, text="Ja",variable=check_var5)
        checkbutton_andere_Schüler.grid()

    s_merkmale_füllen()

def s_merkmale_füllen():
    s_merkmale=[]
    if Schüleranzahl < 300:
        s_merkmale.append(1)
    elif Schüleranzahl >= 300 and Schüleranzahl < 500:
        s_merkmale.append(2)
    elif Schüleranzahl >= 500 and Schüleranzahl < 700:
        s_merkmale.append(3)
    elif Schüleranzahl >= 700 and Schüleranzahl < 900:
        s_merkmale.append(4)
    elif Schüleranzahl >= 900 and Schüleranzahl < 1100:
        s_merkmale.append(5)
    else:
        s_merkmale.append(6)

    if check_var1.get() == "selected":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    if check_var2.get() == "selected":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    if check_var3.get() == "selected":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    if check_var4.get() == "selected":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    if check_var5.get() == "selected":
        s_merkmale.append(1)
    else:
        s_merkmale.append(0)
    merkmalsliste.append(s_merkmale)





def tab2_3():
    notebook.select(tab3)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for i in range(anzahl_schulen_bus):
        row = i * 2  # Verwenden Sie die doppelte Zeilenzahl, um Platz für alle Widgets zu schaffen
        label_Haltestelle = ttk.Label(scrollable_tab3.scrollable_frame,
                                      text=f'Wie viele Busse fahren zu Haltestelle {i + 1}')
        label_Haltestelle.grid(column=0, row=row, padx=5, pady=5)
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab3.scrollable_frame)
        entry_Haltestellennutzung.grid(column=1, row=row, padx=5, pady=5)
        n_ava.append(entry_Haltestellennutzung)




entry_travel_times=[]
def tab3_4():
    notebook.select(tab4)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for startpunkt in range(anzahl_schulen_bus):
        for zielpunkt in range(anzahl_schulen_bus):
            for header in range(int(n_ava[zielpunkt].get())):
                if startpunkt != zielpunkt:
                    while True:
                        label_Traveltime = ttk.Label(scrollable_tab4.scrollable_frame, text=f"Gib die Fahrzeit von Haltestelle {startpunkt + 1} über den Routenstart {header + 1} zur Haltestelle {zielpunkt + 1} an: ")
                        label_Traveltime.grid(column=0)
                        entry_Traveltime = ttk.Entry(scrollable_tab4.scrollable_frame)
                        entry_Traveltime.grid(column=1)
                        entry_travel_times.append(entry_Traveltime)
                        #travel_time = int(entry_Traveltime.get()) + Spaetere_Ankuenfte[zielpunkt].get()
                        Travel_times.append(0)  # Speichere die Fahrzeit in der Liste
                        break
                else:
                    Travel_times.append(100000000)


def Berechnung_starten():
    notebook.select(tab5)
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
    Var = []
    Durchläufe = 0
    # Ausgabe der Ergebnisse für die restlichen höchsten Werte
    for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial + 1):
        label_Einsparungen=ttk.Label(scrollable_tab6.scrollable_frame,text=f"Mit folgenden Varianten werden {max_reuses - Durchläufe} Busse gespart")
        label_Einsparungen.grid()
        for q in indices_of_values[Durchläufe]:
            label_Kombinationen=ttk.Label(scrollable_tab6.scrollable_frame, text= f"{schoolstart_combination[q]}")
            label_Kombinationen.grid()
            Var.append(schoolstart_combination[q])



# Tab1
Anzahl_Schulen_entry_value = tk.StringVar(value="0")
label_Anzahl_Schulen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Schulen im Untersuchungsgebiet")
label_Anzahl_Schulen.grid(column=0, row=0, padx=5, pady=5)
entry_Anzahl_Schulen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Schulen_entry_value)
entry_Anzahl_Schulen.grid(column=1, row=0, padx=5, pady=5)
anzahl_schulen=entry_Anzahl_Schulen

Anzahl_Haltestellen_entry_value = tk.StringVar(value="0")
label_Anzahl_Haltestellen = ttk.Label(scrollable_tab1.scrollable_frame,
                                      text="Anzahl Ankunftsthaltestelle für Schülerverkehr im Untersuchungsgebiet")
label_Anzahl_Haltestellen.grid(column=0, row=1, padx=5, pady=5)
entry_Anzahl_Haltestellen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Haltestellen_entry_value)
entry_Anzahl_Haltestellen.grid(column=1, row=1, padx=5, pady=5)

Anzahl_Bewohner_entry_value = tk.StringVar(value="0")
label_Anzahl_Bewohner = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Bewohner im Untersuchungsgebiet")
label_Anzahl_Bewohner.grid(column=0, row=2, padx=5, pady=5)
entry_Anzahl_Bewohner = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Bewohner_entry_value)
entry_Anzahl_Bewohner.grid(column=1, row=2, padx=5, pady=5)

button_nächster_Tab1 = ttk.Button(scrollable_tab1.scrollable_frame, text="Nächster Schritt", command=tab1_2)
button_nächster_Tab1.grid(column=2, row=3, padx=5, pady=5)

# Tab2
button_nächster_Tab2 = ttk.Button(scrollable_tab2.scrollable_frame, text="Nächster Schritt", command=tab2_3)
button_nächster_Tab2.grid(column=2, row=3, padx=5, pady=5)

# Tab3
button_nächster_Tab3 = ttk.Button(scrollable_tab3.scrollable_frame, text="Nächster Schritt", command=tab3_4)
button_nächster_Tab3.grid(column=2, row=3, padx=5, pady=5)

# Tab4
Berechnung_starten = ttk.Button(scrollable_tab4.scrollable_frame, text="Berechnung starten", command=Berechnung_starten)
Berechnung_starten.grid(column=2, row=3, padx=5, pady=5)





# Hauptfenster ausführen
root.mainloop()
