import tkinter as tk
from tkinter import ttk

# Hauptfenster erstellen
root = tk.Tk()
root.title("GUI mit 7 Tabs")

# Tab-Control erstellen
notebook = ttk.Notebook(root) # Organisation der Tabs

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



#Tab1
Versatz=[]
def tab1_2():
    notebook.select(tab2)
    anzahl_Schulen = int(entry_Anzahl_Schulen.get())
    for i in range(anzahl_Schulen):
        label_Schule = ttk.Label (tab2, text=f'Schule {i + 1}')
        label_Schule.grid()
        label_aktueller_Schulbeginn=ttk.Label(tab2, text="Aktueller Schulbeginn in Minuten nach 7")
        label_aktueller_Schulbeginn.grid()
        entry_aktueller_Schulbeginn=ttk.Entry(tab2)
        entry_aktueller_Schulbeginn.grid()
        label_Haltestellennutzung=tk.Label(tab2, text="Welche Haltestelle nutzt die Schule?")
        label_Haltestellennutzung.grid()
        entry_Haltestellennutzung=ttk.Entry(tab2)
        entry_Haltestellennutzung.grid()
        label_spätere_Ankunft = tk.Label(tab2, text=f"Muss der Schulstart an Schule {i + 1} später liegen, wie an der fühesten Schule, die diese Haltestelle nutzt, weil sie als Anschlussfahrt angefahren wird. Falls ja hier Minutenanzahl angeben, ansonsten 0 eingeben-als Vielfaches von 5 angeben")
        label_spätere_Ankunft.grid()
        Versatz.append(label_spätere_Ankunft)
        entry_spätere_Ankunft = ttk.Entry(tab2)
        entry_spätere_Ankunft.grid()
        label_Weg_Bus_Schule = tk.Label(tab2, text=f"Wie viel Zeit soll bei Schule {i + 1}  zwischen Busankunft und Schulbeginn liegen? - als Vielfaches von 5 angeben")
        label_Weg_Bus_Schule.grid()
        entry_Weg_Bus_Schule = ttk.Entry(tab2)
        entry_Weg_Bus_Schule.grid()
        label_Schüleranzahl = ttk.Label(tab2, text="Wie viele Schüler hat die Schule?")
        label_Schüleranzahl.grid()
        entry_Schüleranzahl = ttk.Entry(tab2)
        entry_Schüleranzahl.grid()
        label_Betreuungsangebot_morgens =ttk.Label(tab2, text="Gibt es ein Betreuungsangebot morgens?")
        label_Betreuungsangebot_morgens.grid()
        checkbutton_Betreuung_morgens=ttk.Checkbutton (tab2, text="Ja")
        checkbutton_Betreuung_morgens.grid()
        label_Betreuungsangebot_mittags = ttk.Label(tab2, text="Gibt es ein Betreuungsangebot mittags?")
        label_Betreuungsangebot_mittags.grid()
        checkbutton_Betreuung_mittags = ttk.Checkbutton(tab2, text="Ja")
        checkbutton_Betreuung_mittags.grid()
        label_Mensa = ttk.Label(tab2, text="Gibt es eine Mensa?")
        label_Mensa.grid()
        checkbutton_Mensa = ttk.Checkbutton(tab2, text="Ja")
        checkbutton_Mensa.grid()
        label_andere_Lehrer = ttk.Label(tab2, text="Gibt es Lehrer, die an anderen Schulen unterrichten??")
        label_andere_Lehrer.grid()
        checkbutton_andere_Lehrer = ttk.Checkbutton(tab2, text="Ja")
        checkbutton_andere_Lehrer.grid()
        label_andere_Schüler = ttk.Label(tab2, text="Gibt es Schüler, die auch Fächer an anderen Schulen besuchen??")
        label_andere_Schüler.grid()
        checkbutton_andere_Schüler = ttk.Checkbutton(tab2, text="Ja")
        checkbutton_andere_Schüler.grid()

n_ava=[]
def tab2_3():
    notebook.select(tab3)
    anzahl_Schulen_bus = int(entry_Anzahl_Haltestellen.get())
    for i in range(anzahl_Schulen_bus):
        label_Haltestelle=ttk.Label(tab3,text=f'Wie viele Busse fahren zu Haltestelle {i + 1}')
        label_Haltestelle.grid(column=0, row=i)
        entry_Haltestellennutzung=ttk.Entry(tab3)
        entry_Haltestellennutzung.grid(column=1, row=i)
        n_ava.append(entry_Haltestellennutzung)


Travel_times=[]
def tab3_4():
    notebook.select(tab4)
    for startpunkt in range(anzahl_schulen_bus):
        for zielpunkt in range(anzahl_schulen_bus):
            for header in range(n_ava[zielpunkt]):
                if startpunkt != zielpunkt:
                    label_Traveltime = ttk.Label(tab4, text= f"Gib die Fahrzeit von Haltestelle {startpunkt + 1} über den Routenstart {header + 1} zur Haltestelle {zielpunkt + 1} an: ")
                    label_Traveltime.grid(column=0)
                    entry_Traveltime=ttk.Entry(tab4)
                    entry_Traveltime.grid(column=1)
                    travel_time = entry_Traveltime + int(Versatz[zielpunkt])
                    Travel_times.append(travel_time)  # Speichere die Fahrzeit in der Liste

                else:
                    Travel_times.append(100000000)


Anzahl_Schulen_entry_value=tk.StringVar(value="0")
label_Anzahl_Schulen = ttk.Label (tab1, text="Anzahl Schulen im Untersuchungsgebiet")
label_Anzahl_Schulen.grid(column=0, row=0)
entry_Anzahl_Schulen =ttk.Entry (tab1, textvariable=Anzahl_Schulen_entry_value)
entry_Anzahl_Schulen.grid(column=1, row=0)
anzahl_Schulen=int(entry_Anzahl_Schulen.get())

Anzahl_Haltestellen_entry_value=tk.StringVar(value="0")
label_Anzahl_Haltestellen = ttk.Label (tab1, text="Anzahl Ankunftsthaltestelle für Schülerverkehr  im Untersuchungsgebiet")
label_Anzahl_Haltestellen.grid(column=0, row=1)
entry_Anzahl_Haltestellen =ttk.Entry (tab1, textvariable=Anzahl_Haltestellen_entry_value)
entry_Anzahl_Haltestellen.grid(column=1, row=1)
anzahl_schulen_bus=int(entry_Anzahl_Haltestellen.get())

Anzahl_Bewohner_entry_value=tk.StringVar(value="0")
label_Anzahl_Bewohner = ttk.Label (tab1, text="Anzahl Bewohner im Untersuchungsgebiet")
label_Anzahl_Bewohner.grid(column=0, row=2)
entry_Anzahl_Bewohner =ttk.Entry (tab1, textvariable=Anzahl_Bewohner_entry_value)
entry_Anzahl_Bewohner.grid(column=1, row=2)
Anzahl_Einwohner=int(entry_Anzahl_Bewohner.get())

button_nächster_Tab1= ttk.Button (tab1, text="Nächster Schritt", command=tab1_2)
button_nächster_Tab1.grid(column=2, row=3)

#Tab2
button_nächster_Tab2= ttk.Button (tab2, text="Nächster Schritt", command=tab2_3)
button_nächster_Tab2.grid(column=2, row=3)

#Tab3
button_nächster_Tab3= ttk.Button (tab3, text="Nächster Schritt", command=tab3_4)
button_nächster_Tab3.grid(column=2, row=3)






# Hauptfenster ausführen
root.mainloop()