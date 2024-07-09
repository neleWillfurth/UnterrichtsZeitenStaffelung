import itertools


def erstellung_kombination_busankunft (anzahl_schulen, aktueller_unterrichtsbeginn_alle_Schulen_entries, Spaetere_Ankuenfte, Weg_Bus_Schule,
                                Haltestellennummern):
    Busankunftszeiten_alle_Schulen_aktuell = []

    for i in range(int(anzahl_schulen.get())):
        Busankunft_aktuell = int(aktueller_unterrichtsbeginn_alle_Schulen_entries[i].get()) - int(Spaetere_Ankuenfte[i].get()) - int(
            Weg_Bus_Schule[i].get())
        Busankunftszeiten_alle_Schulen_aktuell.append(Busankunft_aktuell)

    print("Busankunftszeiten_alle_Schulen_aktuell", Busankunftszeiten_alle_Schulen_aktuell)

    Busankunftszeiten_alle_schule_zulässig = []
    for i in range(int(anzahl_schulen.get())):
        Busankunft_aktuell = int(aktueller_unterrichtsbeginn_alle_Schulen_entries[i].get())
        Startzeiten_Korridor_zulässig = []

        if Busankunft_aktuell < 40:
            Startzeiten_Korridor_zulässig.extend([
                Busankunftszeiten_alle_Schulen_aktuell[i],
                Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 10,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 15,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 20,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 25,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 30,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 35,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 40
            ])
        elif Busankunft_aktuell >= 40 and Busankunft_aktuell < 55:
            Startzeiten_Korridor_zulässig.extend([
                Busankunftszeiten_alle_Schulen_aktuell[i] - 10,
                Busankunftszeiten_alle_Schulen_aktuell[i] - 5,
                Busankunftszeiten_alle_Schulen_aktuell[i],
                Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 10,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 15,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 20
            ])
        else:
            Startzeiten_Korridor_zulässig.extend([
                Busankunftszeiten_alle_Schulen_aktuell[i] - 10,
                Busankunftszeiten_alle_Schulen_aktuell[i] - 5,
                Busankunftszeiten_alle_Schulen_aktuell[i],
                Busankunftszeiten_alle_Schulen_aktuell[i] + 5,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 10,
                Busankunftszeiten_alle_Schulen_aktuell[i] + 15
            ])

        Busankunftszeiten_alle_schule_zulässig.append(Startzeiten_Korridor_zulässig)

    print("Busankunftszeiten_alle_schule_zulässig", Busankunftszeiten_alle_schule_zulässig)

    Busankunftszeit_Haltestelle = []

    for i in range(int(anzahl_schulen.get())):
        Haltestellennummern_int = [int(entry.get()) for entry in Haltestellennummern]

        if Haltestellennummern_int.count(i + 1) == 1:
            index = Haltestellennummern_int.index(i + 1)
            Busankunftszeit_Haltestelle.append(Busankunftszeiten_alle_schule_zulässig[index])
        else:
            ausgewählte_Busankunftszeiten = [
                busankunftszeit for j, busankunftszeit in enumerate(Busankunftszeiten_alle_schule_zulässig)
                if Haltestellennummern_int[j] == i + 1
            ]

            if ausgewählte_Busankunftszeiten:
                intersection_result = set(ausgewählte_Busankunftszeiten[0]).intersection(
                    *ausgewählte_Busankunftszeiten[1:])
                Busankunftszeit_Haltestelle.append(list(intersection_result))

    combinations = list(itertools.product(*Busankunftszeit_Haltestelle))


    return combinations