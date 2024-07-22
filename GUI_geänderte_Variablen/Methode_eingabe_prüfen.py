import tkinter as tk
from tkinter import ttk


def eingabe_prüfen(aktueller_unterrichtsbeginn_alle_schulen, versatz_ankunft_anschlussfahrt,
                   wegdauer_haltestelle_schule, scrollable_tab2, button_werteingabe_bestätigen,
                   button_eingabe_prüfen):
    """
    Prüfung, ob eingegebene Werte tatsächlich durch 5 teilbar sind

    :param aktueller_unterrichtsbeginn_alle_schulen: wird in Minuten nach 7:00 angegeben und muss durch 5 teilbar sein
    :param versatz_ankunft_anschlussfahrt: bei einer anschlussfahrt wird hier die benötigte Zeit von der früheren zur
    späteren Haltestelle mit der identischen Haltestellennummer eingegeben (muss durch 5 teilbar sein)
    :param wegdauer_haltestelle_schule: benötigte Zeit zwischen Busankunft und Unterrichtsbeginn je Schule (muss durch
    5 teilbar sein)
    :param scrollable_tab2: Prüfergebnis wird dort angezeigt
    :param button_werteingabe_bestätigen: wird bei erfolgreicher Prüfung aktiviert und ermöglicht nächsten Schritt
    :param button_eingabe_prüfen: wird nach erfolgreicher Prüfung ausgegraut
    :return: kein Rückgabewert
    """
    results = []

    try:
        # Überprüfen, ob alle Elemente in aktueller_unterrichtsbeginn_alle_Schulen durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in
                                                                    aktueller_unterrichtsbeginn_alle_schulen]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in versatz_ankunft_anschlussfahrt durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in
                                                                    versatz_ankunft_anschlussfahrt]):
            results.append(True)
        else:
            results.append(False)

        # Überprüfen, ob alle Elemente in wegdauer_haltestelle_schule durch 5 teilbar sind
        if all(isinstance(x, (int, float)) and x % 5 == 0 for x in [int(entry.get()) for entry in
                                                                    wegdauer_haltestelle_schule]):
            results.append(True)
        else:
            results.append(False)

    except Exception as e:
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war ungültig - bitte ändern sie "
                                                                        "die Zahlen", font=("Helvetica", 10))
        label_fehler.grid()

    # sobald ein Wert "False" ist, wir die gesamte Eingabe ungültig
    if not all(result for result in results):
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame, text="Die Eingabe war ungültig - bitte ändern sie "
                                                                        "die Zahlen", font=("Helvetica", 10))
        label_fehler.grid(column=1, row=5)
    else:
        # bei gültiger Eingabe wird die Gültigkeit ausgegeben und der Button zur Bestätigung der Werteingabe
        # aktiviert sowie der Prüfbutton deaktiviert
        label_fehler = ttk.Label(scrollable_tab2.scrollable_frame,
                                 text="Die Eingabe war gültig", font=("Helvetica", 10))
        label_fehler.grid(column=1, row=5, padx=100)
        button_werteingabe_bestätigen.configure(state=tk.NORMAL)
        button_eingabe_prüfen.configure(state=tk.DISABLED)
