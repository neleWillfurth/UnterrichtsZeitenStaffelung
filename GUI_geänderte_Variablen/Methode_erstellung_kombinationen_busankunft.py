import itertools


def erstellung_kombination_busankunft(anzahl_schulen, aktueller_unterrichtsbeginn_alle_schulen,
                                      versatz_ankunft_anschlussfahrt, wegdauern_haltestelle_schule,
                                      haltestellennummern_alle_schulen):
    """
    Erstellung aller Kombinationen an Busankunftszeiten an den Haltestellen, die prinzipiell zulässig sind

    :param anzahl_schulen: ermöglicht es die for-Schleifen für jede Schule einmal durchzuführen
    :param aktueller_unterrichtsbeginn_alle_schulen:
    :param versatz_ankunft_anschlussfahrt: bei einer anschlussfahrt wird hier die benötigte Zeit von der früheren zur
    späteren Haltestelle mit der identischen Nummer eingegeben
    :param wegdauern_haltestelle_schule: gibt die benötigte Zeit zwischen Busankunft und Unterrichtsbeginn je
    Schule an
    :param haltestellennummern_alle_schulen: Liste mit der Haltestellennummer je Schule
    :return: zulässige_kombinationen_busankünfte
    """

    # basierend aus dem aktuellen Unterrichtsbeginn der Schulen einem möglichen Versatz durch eine Anschlussfahrt und
    # der Dauer zwischen Busankunft und Unterrichtsbeginn wird für jede Schule rückwärts die aktuelle Busankunftszeit
    # berechnet. Diese Werte werden in der Liste busankunftszeiten_alle_schulen_aktuell gespeichert
    busankunftszeiten_alle_schulen_aktuell = []

    for i in range(int(anzahl_schulen.get())):
        busankunft_eine_schule_aktuell = (int(aktueller_unterrichtsbeginn_alle_schulen[i].get()) -
                                          int(versatz_ankunft_anschlussfahrt[i].get()) -
                                          int(wegdauern_haltestelle_schule[i].get()))

        busankunftszeiten_alle_schulen_aktuell.append(busankunft_eine_schule_aktuell)

    # basierend auf den aktuellen Unterrichtsbeginn für eine Schule wird bestimmt, welche Zeiten für die Busankunft
    # an der Haltestelle einer Schule prinzipiell zulässig sind
    zulässige_busankünfte_alle_schulen = []
    for i in range(int(anzahl_schulen.get())):
        unterrichtsbeginn_aktuell = int(aktueller_unterrichtsbeginn_alle_schulen[i].get())
        # für jede Schule wird eine Liste mit Zeiten für zulässige Busankünfte erstellt
        zulässige_busankunft_eine_schule = []

        # liegt der Unterrichtsbeginn an einer Schule aktuell vor 7:40 ist eine Verschiebung des Unterrichtsbeginns
        # (daraus resultierend auch der Busankunft) bis 40 Minuten nach hinten zulässig
        if unterrichtsbeginn_aktuell < 40:
            zulässige_busankunft_eine_schule.extend([
                busankunftszeiten_alle_schulen_aktuell[i],
                busankunftszeiten_alle_schulen_aktuell[i] + 5,
                busankunftszeiten_alle_schulen_aktuell[i] + 10,
                busankunftszeiten_alle_schulen_aktuell[i] + 15,
                busankunftszeiten_alle_schulen_aktuell[i] + 20,
                busankunftszeiten_alle_schulen_aktuell[i] + 25,
                busankunftszeiten_alle_schulen_aktuell[i] + 30,
                busankunftszeiten_alle_schulen_aktuell[i] + 35,
                busankunftszeiten_alle_schulen_aktuell[i] + 40
            ])
        # liegt der Unterrichtsbeginn an einer Schule aktuell zwischen 7:40 und 7:55 ist eine Verschiebung des
        # Unterrichtsbeginns (daraus resultierend auch der Busankunft) zwischen 10 Minuten nach vorne und 20 Minuten
        # nach hinten zulässig
        elif unterrichtsbeginn_aktuell < 55:
            zulässige_busankunft_eine_schule.extend([
                busankunftszeiten_alle_schulen_aktuell[i] - 10,
                busankunftszeiten_alle_schulen_aktuell[i] - 5,
                busankunftszeiten_alle_schulen_aktuell[i],
                busankunftszeiten_alle_schulen_aktuell[i] + 5,
                busankunftszeiten_alle_schulen_aktuell[i] + 10,
                busankunftszeiten_alle_schulen_aktuell[i] + 15,
                busankunftszeiten_alle_schulen_aktuell[i] + 20
            ])
        # liegt der Unterrichtsbeginn an einer Schule aktuell nach 7:55 ist eine Verschiebung des Unterrichtsbeginns
        # (daraus resultierend auch der Busankunft) zwischen 10 Minuten nach vorne und 15 Minuten nach hinten zulässig
        else:
            zulässige_busankunft_eine_schule.extend([
                busankunftszeiten_alle_schulen_aktuell[i] - 10,
                busankunftszeiten_alle_schulen_aktuell[i] - 5,
                busankunftszeiten_alle_schulen_aktuell[i],
                busankunftszeiten_alle_schulen_aktuell[i] + 5,
                busankunftszeiten_alle_schulen_aktuell[i] + 10,
                busankunftszeiten_alle_schulen_aktuell[i] + 15
            ])

        # die Liste der zulässigen Busankünfte aller einzelnen Schulen werden zu einer Liste von Listen zusammengeführt
        zulässige_busankünfte_alle_schulen.append(zulässige_busankunft_eine_schule)

    # Um weiterzurechnen, benötigt man je Haltestelle die zulässige Busankunft und muss dabei berücksichtigen, dass eine
    # Haltestelle auch von mehreren Schulen genutzt wird
    zulässige_busankunft_alle_haltestellen = []

    for i in range(int(anzahl_schulen.get())):
        haltestellennummern_int = [int(entry.get()) for entry in haltestellennummern_alle_schulen]
        # wenn eine Haltestelle nur von einer Schule genutzt wird, werden die zulässigen Busankünfte dieser einen Schule
        # direkt in der Liste zulässige_busankunft_alle_haltestellen ergänzt, da diese Werte identisch sind
        if haltestellennummern_int.count(i + 1) == 1:
            index = haltestellennummern_int.index(i + 1)
            zulässige_busankunft_alle_haltestellen.append(zulässige_busankünfte_alle_schulen[index])
        # wenn eine Haltestelle von mehreren Schulen genutzt wird, werden nur jene Werte aus den inneren Listen aus
        # zulässige_busankünfte_alle_schulen genommen, die in allen Listen stehen, die zur gleichen Haltestellennummer
        # gehören
        else:
            zulässige_busankünfte_eine_haltestelle_mehrere_schulen = [
                busankunftszeit for j, busankunftszeit in enumerate(zulässige_busankünfte_alle_schulen)
                if haltestellennummern_int[j] == i + 1]

            if zulässige_busankünfte_eine_haltestelle_mehrere_schulen:
                intersection_result = set(zulässige_busankünfte_eine_haltestelle_mehrere_schulen[0]).intersection(
                    *zulässige_busankünfte_eine_haltestelle_mehrere_schulen[1:])
                zulässige_busankunft_alle_haltestellen.append(list(intersection_result))

    # Alle gültigen Kombinationen an Busankünften werden basierend auf zulässige_busankunft_alle_haltestellen bestimmt
    zulässige_kombinationen_busankünfte = list(itertools.product(*zulässige_busankunft_alle_haltestellen))

    return zulässige_kombinationen_busankünfte
