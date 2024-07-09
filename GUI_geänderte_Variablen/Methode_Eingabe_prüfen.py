import tkinter as tk
from tkinter import ttk

def eingabe_prüfen(aktueller_unterrichtsbeginn_alle_Schulen_entries, Spaetere_Ankuenfte, Weg_Bus_Schule, scrollable_tab2, button_werteingabe_bestaetigen, button_eingabe_pruefen):
    results = []

    try:
        # Überprüfen, ob alle Elemente in aktueller_unterrichtsbeginn_alle_Schulen_entries durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in aktueller_unterrichtsbeginn_alle_Schulen_entries]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in Spaetere_Ankuenfte durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in Spaetere_Ankuenfte]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in Weg_Bus_Schule durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in Weg_Bus_Schule]):
            results.append(True)
        else:
            results.append(False)

    except Exception as e:
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war ungültig - bitte ändern sie die Zahlen",font=("Helvetica",10))
        label_fehler.grid()

    if not all(result for result in results):
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war ungültig - bitte ändern sie die Zahlen",font=("Helvetica",10))
        label_fehler.grid(column=1, row=5)
    else:
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war gültig",font=("Helvetica",10))
        label_fehler.grid(column=1, row=5, padx=10)
        button_werteingabe_bestaetigen.configure(state=tk.NORMAL)
        button_eingabe_pruefen.configure(state=tk.DISABLED)

    return results
