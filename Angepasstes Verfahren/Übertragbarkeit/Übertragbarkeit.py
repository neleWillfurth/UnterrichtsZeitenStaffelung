import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

# Definiere das Gebiet (xmin, xmax, ymin, ymax)
xmin, xmax = 0, 50
ymin, ymax = 0, 50

# Anzahl der Schulen und Startpunkte
Schulen = 10
Startpunkte = 54

# Generiere zufällige Punkte für Schulen und Startpunkte innerhalb des definierten Gebiets mit ganzzahligen Koordinaten
points_schulen = np.random.randint(low=[xmin, ymin], high=[xmax + 1, ymax + 1], size=(Schulen, 2))
points_startpunkte = np.random.randint(low=[xmin, ymin], high=[xmax + 1, ymax + 1], size=(Startpunkte, 2))

# Berechne die Abstände zwischen allen Punkten
distances = distance_matrix(points_schulen, points_startpunkte)

# Runde die Abstände auf ganze Zahlen
distances_rounded = np.round(distances)

# Ausgabe der Punkte und Distanzen
print("Zufällige Punkte der Schulen:\n", points_schulen)
print("Zufällige Punkte der Startpunkte:\n", points_startpunkte)
print("\nAbstände zwischen Schulen und Startpunkten (gerundet):\n")

# Ausgabe der Abstände nach Schule und Startpunkt sortiert
for i in range(Schulen):
    for j in range(Startpunkte):
        print(f"Abstand {distances_rounded[i, j]}: Schule {i+1} - Startpunkt {j+1}")

# Plotten der Punkte
plt.scatter(points_schulen[:, 0], points_schulen[:, 1], color='blue', label='Schulen')
plt.scatter(points_startpunkte[:, 0], points_startpunkte[:, 1], color='red', label='Startpunkte')

# Annotieren der Punkte
for i, point in enumerate(points_schulen):
    plt.text(point[0], point[1], f'S{i}')

for i, point in enumerate(points_startpunkte):
    plt.text(point[0], point[1], f'St{i}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Zufällige Punkte der Schulen und Startpunkte')
plt.legend()
plt.grid(True)
plt.show()
