# importieren von Biblotheken
import tkinter as tk
from tkinter import ttk
from threading import Thread
import pandas

# Import eigener Methoden
from Matrizenbearbeitung_GUI import matrizenbearbeitung
from Methode_Schulcharakteristika import Schulcharakteristika_eingeben
from Methode_Eingabe_prüfen import eingabe_prüfen
from Methode_Werte_eintragen import Werte_eintragen
from Methode_Fahrzeiten_eingeben import fahrzeiten_eintragen
from Methode_Erstellung_gültiger_Kombinationen_Busankunft import erstellung_kombination_busankunft
from Methode_Akzeptanzbewertung import Akzeptanzbewertung_rechnen
from Methode_Matrizenerstellung import matrizenerstellung


d=pandas.read_csv('Daten_rating_system2.csv', sep=';')


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
checkbuttons = []
Schüleranzahlen=[]
Gesamtmittelwerte =[]
spinner = None
button_style = ttk.Style()
button_style.configure('Custom.TButton', font=('Helvetica', 10, "bold"))



# Buttonfunktionen Tab 2

def tab1_2():
    notebook.select(tab2)
    button_nächster_Tab1.configure(state=tk.DISABLED)
    Schulcharakteristika_eingeben(notebook, tab2, entry_Anzahl_Schulen, scrollable_tab2,
                                  Startzeiten_aktuell, Haltestellennummern, Spaetere_Ankuenfte,
                                  Weg_Bus_Schule, Schüleranzahlen, checkbuttons, check_var_liste1, check_var_liste2, check_var_liste3,
                                 check_var_liste4, check_var_liste5)
    entry_Anzahl_Schulen.config(state=tk.DISABLED)
    entry_Anzahl_Haltestellen.config(state=tk.DISABLED)
    entry_Anzahl_Bewohner.config(state=tk.DISABLED)

def eingabe_prüfen_main():
    eingabe_prüfen(Startzeiten_aktuell, Spaetere_Ankuenfte, Weg_Bus_Schule, scrollable_tab2, button_Werte_eintragen, validate_button)



def button_werte_eintragen():
    Werte_eintragen(entry_Anzahl_Schulen, Startzeiten_aktuell, Schüleranzahlen, check_var_liste1, check_var_liste2,
                    check_var_liste3, check_var_liste4, check_var_liste5, merkmalsliste)

    button_Werte_eintragen.configure(state=tk.DISABLED)
    validate_button.configure(state=tk.DISABLED)
    button_nächster_Tab2.configure(state=tk.NORMAL)
    for startzeiten_entery in Startzeiten_aktuell:
        startzeiten_entery.config(state="disabled")

    for weg_Bus_Schule_entry in Weg_Bus_Schule:
        weg_Bus_Schule_entry.config(state="disabled")

    for spaetere_Ankuenfte_entry in Spaetere_Ankuenfte:
        spaetere_Ankuenfte_entry.config(state="disabled")

    for haltestellennummern_entry in Haltestellennummern:
        haltestellennummern_entry.config(state="disabled")

    for schüleranzahlen_entry in Schüleranzahlen:
        schüleranzahlen_entry.config(state="disabled")

    for checkbutton in checkbuttons:
        checkbutton.config(state="disabled")


# Eingabe Anzahl Busse pro Haltestelle - Tab 3
def tab2_3():
    notebook.select(tab3)
    button_nächster_Tab2.configure(state=tk.DISABLED)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for i in range(anzahl_schulen_bus):
        row = i * 2  # Verwenden Sie die doppelte Zeilenzahl, um Platz für alle Widgets zu schaffen
        label_Haltestelle = ttk.Label(scrollable_tab3.scrollable_frame,
                                      text=f'Anzahl Busse zu Haltestelle {i + 1}', font=("Helvetica",10))
        label_Haltestelle.grid(column=0, row=row, padx=5, pady=5)
        entry_Haltestellennutzung = ttk.Entry(scrollable_tab3.scrollable_frame)
        entry_Haltestellennutzung.grid(column=1, row=row, padx=5, pady=5)
        n_ava.append(entry_Haltestellennutzung)





# Eingaben zu den Fahrzeiten Tab 4
entry_travel_times=[]
def tab3_4():
    for ein_entry_Haltestellennutzung in n_ava:
        ein_entry_Haltestellennutzung.config(state="disabled")
    notebook.select(tab4)
    button_nächster_Tab3.configure(state=tk.DISABLED)

    label_Erklärung1 = ttk.Label(scrollable_tab4.scrollable_frame, text="Die Fahrzeit von einer Schule zum Routenstart zu einer anderen Schule muss mit einem Navigator ermittelt werden", font=("Helvetica",10))
    label_Erklärung1.grid(column=0,row=0)
    label_Erklärung2 = ttk.Label(scrollable_tab4.scrollable_frame,text= "Dieser Wert wird mit der Fahrzeit einer entsprechenden Route addiert. Die Routenzeit muss dem aktuellen Fahrplan entnommen werden.\n\n"
                                 "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("Helvetica",10))
    label_Erklärung2.grid(column=0,row=1)
    anzahl_schulen_bus = int(entry_Anzahl_Haltestellen.get())
    fahrzeiten_eintragen(anzahl_schulen_bus, n_ava, scrollable_tab4, entry_travel_times, Travel_times)



# Tab 4 Berechnungrn
def threading_Berechnung_starten():
    t1=Thread(target=Berechnung_starten)
    t1.start()

def Berechnung_starten():

    button_Berechnung_starten.configure(state=tk.DISABLED)
    for entry_travel_time in entry_travel_times:
        entry_travel_time.config(state="disabled")
    notebook.select(tab6)

    label_es_lädt=ttk.Label(text="Es lädt ...", font=("Helvetica",20, "bold"))
    label_es_lädt.pack()


    for i in range(len(Travel_times)):
        if Travel_times[i]==0:
            Travel_times[i]=int(entry_travel_times.pop(0).get())


    busses_needed_without = sum(int(entry.get()) for entry in n_ava)
    combinations=erstellung_kombination_busankunft(anzahl_schulen, Startzeiten_aktuell, Spaetere_Ankuenfte, Weg_Bus_Schule, Haltestellennummern)

    n_ava_values = [int(entry.get()) for entry in n_ava]
    matrizen, schoolstart_combination = matrizenerstellung (combinations, Anzahl_Haltestellen_entry_value, busses_needed_without, Travel_times, n_ava_values)

    for matrix in matrizen:

        max_anfahrten = []
        for i in range(len(n_ava_values)):
            max_anfahrten.append(0)
        n_reuse = 0
        n_ava_values = [int(entry.get()) for entry in n_ava]
        n_ava_unverbraucht = n_ava_values.copy()
        n_anfahrten = n_ava_values.copy()
        n_reuse_einzel = matrizenbearbeitung(matrix, n_ava_values, n_ava_unverbraucht, n_reuse, max_anfahrten, n_anfahrten)
        n_reuses.append(n_reuse_einzel)


    # Bestimmung eines hohen Einspapotenzials
    Anzahl_Einwohner = int(entry_Anzahl_Bewohner.get())
    Teiler = 83300000 / Anzahl_Einwohner
    Busse_hohes_Einsparpotenzial = int(19600 * 1.15 / Teiler) + 1

# Bestimmung der Inidzies für Varianten mit hohem Einspapotenzial
    max_reuses = max(n_reuses)
    indices_of_values = []

    # Berechnen und Ausgeben, solange die Einsparung nicht hoch genug ist
    for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial + 1):
        # Neue Liste für jeden Durchlauf erstellen
        indices = [i for i, x in enumerate(n_reuses) if x == max_reuses - Durchläufe]
        indices_of_values.append(indices)  # Diese Liste in indices_of_values sammeln



    #  - Ausgabe der Busankunftszeiten und Unterrichtsbeginnzeiten
    label_Ergebnisse =ttk.Label(scrollable_tab6.scrollable_frame, text="Ergebnisse", font=("Helvetica",12,"bold"))
    label_Ergebnisse.grid()
    label_anzahl_ohne_Staffelung=ttk.Label(scrollable_tab6.scrollable_frame, text=f"Ohne Staffelung der Unterrichtszeiten werden {busses_needed_without} Busse benötigt", font=("Helvetica",10))
    label_anzahl_ohne_Staffelung.grid()
    label_maximale_Einsparung = ttk.Label(scrollable_tab6.scrollable_frame,text=f"Es können maximal {max(n_reuses)} Busse eingespart werden", font=("Helvetica",10))
    label_maximale_Einsparung.grid()
    label_hohe_Einsparung = ttk.Label(scrollable_tab6.scrollable_frame,text=f"Ein hohes Einsparpotenzial wird ab{Busse_hohes_Einsparpotenzial} Bussen erreicht", font=("Helvetica",10))
    label_hohe_Einsparung.grid()
    label_trennstrich= tk.Label(scrollable_tab6.scrollable_frame,text="---------------------------------------------------------------------------------------------------------------------------------", font=("Helvetica",10))
    label_trennstrich.grid()
    label_Erklärung_Buseinsparung1= ttk.Label(scrollable_tab6.scrollable_frame,text="Die erste angegbenene Zeit ist die Busankunftszeit an Haltestelle Nummer 1 (angegeben in Minuten nach 7).", font=("Helvetica",10))
    label_Erklärung_Buseinsparung1.grid()
    label_Erklärung_Buseinsparung2 = ttk.Label(scrollable_tab6.scrollable_frame,
                                              text="Es folgt die Busankunftszeit an Haltestelle 2 usw.. Analog dazu wird bei den Unterrichtsbeginnzeiten als erstes", font=("Helvetica",10))
    label_Erklärung_Buseinsparung2.grid()
    label_Erklärung_Buseinsparung3 = ttk.Label(scrollable_tab6.scrollable_frame,text= "der Unterrichtsbeginn an Schule 1, dasnn an Schule 2 usw. (ebenfalls in Minuten nach 7) angegben\n\n"
                                      "---------------------------------------------------------------------------------------------------------------------------------", font=("Helvetica",10))
    label_Erklärung_Buseinsparung3.grid()
    Durchläufe = 0
    # Ausgabe der Ergebnisse für die restlichen höchsten Werte
    for Durchläufe in range(max_reuses - Busse_hohes_Einsparpotenzial + 1):
        label_Einsparungen=ttk.Label(scrollable_tab6.scrollable_frame,text=f"Mit folgenden Varianten werden {max_reuses - Durchläufe} Busse gespart",font=("Helvetica",10,"bold"))
        label_Einsparungen.grid()

        for q in indices_of_values[Durchläufe]:
            label_Kombinationen=ttk.Label(scrollable_tab6.scrollable_frame, text=f"Busankunftszeiten: {', '.join(map(str, schoolstart_combination[q]))}",font=("Helvetica",10))
            label_Kombinationen.grid()
            Var.append(schoolstart_combination[q])

            Busankunft_Liste_Alle_Schulen_Kombinationen= []
            Unterrichtsbeginn_Kombinationen= []
            for i, inner_list in enumerate(schoolstart_combination):


                # Füge die Elemente der inneren Liste so oft zur Zielliste hinzu, wie die Anzahl der Nummern
                Busankunft_Liste_Alle_Schulen= []
                Unterrichtsbeginn = []

                for i in range(int(anzahl_schulen.get())):
                    Haltestellennummern_int = [int(entry.get()) for entry in Haltestellennummern]

                for schule in range(int(anzahl_schulen.get())):
                    haltestelle = Haltestellennummern_int[schule] - 1
                    ankunftszeit = inner_list[haltestelle]
                    Busankunft_Liste_Alle_Schulen.append(ankunftszeit)
                    Unterrichtsbeginn_Aktuelle_Schule = int(Weg_Bus_Schule[schule].get())+int(Spaetere_Ankuenfte[schule].get())+ankunftszeit
                    Unterrichtsbeginn.append(Unterrichtsbeginn_Aktuelle_Schule)

                Busankunft_Liste_Alle_Schulen_Kombinationen.append(Busankunft_Liste_Alle_Schulen)
                Unterrichtsbeginn_Kombinationen.append(Unterrichtsbeginn)

            label_Unterrichtsbeginn=ttk.Label(scrollable_tab6.scrollable_frame, text=f"Unterrichtsbeginn an den Schulen: {', '.join(map(str, Unterrichtsbeginn_Kombinationen[q]))}",font=("Helvetica",10))
            label_Unterrichtsbeginn.grid()
            label_Trennstrich=ttk.Label(scrollable_tab6.scrollable_frame, text="---------------------------------------------------------------------------------")
            label_Trennstrich.grid()

    label_es_lädt.destroy()



def threading_Akzeptanzbewertung_anzeigen():
    t2=Thread(target=Akzeptanzbewertung_anzeigen)
    t2.start()

def Akzeptanzbewertung_anzeigen():
    notebook.select(tab7)

    label_lädt_akzeptanz = ttk.Label(scrollable_tab7.scrollable_frame, text="Es lädt ...", font=("Helvetica",20, "bold"))
    label_lädt_akzeptanz.pack()

    Gesamtmittelwerte = Akzeptanzbewertung_rechnen(d, merkmalsliste, Var, entry_Anzahl_Schulen, Haltestellennummern, Spaetere_Ankuenfte, Weg_Bus_Schule, Startzeiten_aktuell)
    max_punkte = max(Gesamtmittelwerte)
    max_punkte_gerundet = round(max_punkte,3)
    indices_of_highest_value = [i for i, x in enumerate(Gesamtmittelwerte) if x == max_punkte]



    label_höchste_Punktzahl =ttk.Label(scrollable_tab7.scrollable_frame, text=f"Die höchste Akzeptanzpunktzhal beträgt {max_punkte_gerundet}. Diese kann mit folgenden Varianten erreicht werden:",font=("Helvetica",10))
    label_höchste_Punktzahl.pack()
    for index in indices_of_highest_value:
        label_Variante = ttk.Label(scrollable_tab7.scrollable_frame, text=f"Busankunftszeiten: {', '.join(map(str, Var[index]))}",font=("Helvetica",10))
        label_Variante.pack()

    label_lädt_akzeptanz.destroy()



# Tab-Grundstruktur festlegen
# Tab1
Anzahl_Schulen_entry_value = tk.StringVar(value="0")
label_Anzahl_Schulen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Schulen, die vom Busverkehr bedient werden", font=("Helvetica",10))
label_Anzahl_Schulen.grid(column=0, row=0, padx=5, pady=5)
entry_Anzahl_Schulen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Schulen_entry_value)
entry_Anzahl_Schulen.grid(column=0, row=1, padx=5, pady=5)
anzahl_schulen=entry_Anzahl_Schulen

Anzahl_Haltestellen_entry_value = tk.StringVar(value="0")
label_Anzahl_Haltestellen = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Haltestellen für Schülerverker",  font=("Helvetica",10))
label_Anzahl_Haltestellen.grid(column=0, row=2, padx=5, pady=5)
label_Anzahl_Haltestellen_Erklärung1 = ttk.Label(scrollable_tab1.scrollable_frame,
                                      text="(Wenn eine Haltestelle immer direkt als Anschlussfahrt von einer", font=("Helvetica",8))
label_Anzahl_Haltestellen_Erklärung1.grid(column=0, row=3)
label_Anzahl_Haltestellen_Erklärung2 = ttk.Label(scrollable_tab1.scrollable_frame,
                                      text="anderen Haltestelle angefahren wird, wird diese hier NICHT mitgezählt)", font=("Helvetica",8))

label_Anzahl_Haltestellen_Erklärung2.grid(column=0, row=4)
entry_Anzahl_Haltestellen = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Haltestellen_entry_value)
entry_Anzahl_Haltestellen.grid(column=0, row=5, padx=5, pady=5)

Anzahl_Bewohner_entry_value = tk.StringVar(value="0")
label_Anzahl_Bewohner = ttk.Label(scrollable_tab1.scrollable_frame, text="Anzahl Bewohner im Untersuchungsgebiet",  font=("Helvetica",10))
label_Anzahl_Bewohner.grid(column=0, row=6, padx=5, pady=5)
entry_Anzahl_Bewohner = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=Anzahl_Bewohner_entry_value)
entry_Anzahl_Bewohner.grid(column=0, row=7, padx=5, pady=5)

button_nächster_Tab1 = ttk.Button(scrollable_tab1.scrollable_frame, text="Nächster Schritt", command=tab1_2, style='Custom.TButton')
button_nächster_Tab1.grid(column=1, row=0, padx=5, pady=5)

# Tab2
validate_button = ttk.Button(scrollable_tab2.scrollable_frame, text="Eingaben überprüfen", command=eingabe_prüfen_main, style='Custom.TButton')
validate_button.grid(column=1, row=4)
button_Werte_eintragen= ttk.Button(scrollable_tab2.scrollable_frame, text="Werte eingetragen",command= button_werte_eintragen, state=tk.DISABLED,style='Custom.TButton')
button_Werte_eintragen.grid(column=2, row=4)
button_nächster_Tab2 = ttk.Button(scrollable_tab2.scrollable_frame, text="Nächster Schritt", command=tab2_3, state=tk.DISABLED, style='Custom.TButton')
button_nächster_Tab2.grid(column=3, row=4, padx=5, pady=5)

# Tab3
button_nächster_Tab3 = ttk.Button(scrollable_tab3.scrollable_frame, text="Nächster Schritt", command=tab3_4, style='Custom.TButton')
button_nächster_Tab3.grid(column=3, row=0, padx=5, pady=5)

# Tab4
button_Berechnung_starten = ttk.Button(scrollable_tab4.scrollable_frame, text="Berechnung starten", command=threading_Berechnung_starten, style='Custom.TButton')
button_Berechnung_starten.grid(column=2,  padx=5, pady=5)

#Tab6
Akzeptanz_ergebnis_anzeigen =ttk.Button(scrollable_tab6.scrollable_frame, text="Akzeptanzbewertung anzeigen", command=threading_Akzeptanzbewertung_anzeigen, style='Custom.TButton')
Akzeptanz_ergebnis_anzeigen.grid(column=1)





# Hauptfenster ausführen
root.mainloop()
