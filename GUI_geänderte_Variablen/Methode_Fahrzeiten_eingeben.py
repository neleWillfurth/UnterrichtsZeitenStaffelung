from tkinter import ttk

def fahrzeiten_eintragen(anzahl_schulen_bus, n_ava, scrollable_tab4, entry_travel_times, Travel_times):
    for startpunkt in range(anzahl_schulen_bus):
        for zielpunkt in range(anzahl_schulen_bus):
            for header in range(int(n_ava[zielpunkt].get())):
                if startpunkt != zielpunkt:
                    label_Traveltime = ttk.Label(scrollable_tab4.scrollable_frame, text=f"Gib die Fahrzeit von Haltestelle {startpunkt + 1} über den Routenstart {header + 1} zur Haltestelle {zielpunkt + 1} an: ", font=("Helvetica",10))
                    label_Traveltime.grid(column=0)
                    entry_Traveltime = ttk.Entry(scrollable_tab4.scrollable_frame)
                    entry_Traveltime.grid(column=0)
                    entry_travel_times.append(entry_Traveltime)
                    Travel_times.append(0)  # Speichere die Fahrzeit in der Liste
                else:
                    Travel_times.append(100000000)

