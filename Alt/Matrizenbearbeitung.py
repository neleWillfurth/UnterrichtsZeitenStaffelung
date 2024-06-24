import random
#import numpy as np

a=6 # Anzahl Schulen
b = 21 # Anzahl zu betrachtende Wege
 # Anzahl an Bussen, die an einer Schule ankommen, also die maximal Anzahl, die weiterverwendet werden kann
#n_reuse = 0

matrix = [[random.randint(0, 1) for _ in range(a)] for _ in range(b)]
matrix =[[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0]]

# Ausgabe der Matrix
for row in matrix:
    print(row)

#If Sj ==1: there is a single cell aij with a value of 1. This means that there is only is one way to re-use a bus to cover the route j.
# We increase the number of times a bus is re-used in the alternative, n_reuse, by 1.
#for row in matrix:
 #   row_sum = sum(row)
  #  if row_sum == 1:
   #     n_reuse += 1
def matrizenbearbeitung (matrix, n_ava, n_ava_index,n_reuse):

    while len(n_ava) >1:
        print("---------------------------------------")
        row_index = 0
        for row in matrix:
            row_sum = sum(row)

            if row_sum == 1:
                index2=row.index(1)
                column_sums = [sum(matrix[i][index2] for i in range(row_index) if sum(matrix[i]) == 1)]
                print(index2)
                print("n_ava_index"+str(n_ava_index[index2]))
                print(column_sums[0])

                if column_sums[0] <= n_ava_index[index2] and n_ava_index[index2]>0:
                    n_reuse += 1
                    n_ava_index[index2] -=1
                print ("n_ava_index_nach"+str(n_ava_index[index2]))
                print("Row_index"+ str(row_index))
                print(n_reuse)
            #print(n_ava_index)
            row_index += 1


        # All columns "in meinem Fall Zeilen" wo Sj < 2 werden gelöscht
        matrix = [row for row in matrix if sum(row) >= 2]

        #We decrease the number of buses available for re-use at the school represented by row j, n_availablej, by 1.
        for i in range(len(n_ava)):
            n_ava[i] -= 1

         # Entfernen der Spalten aus der Matrix, wenn die Anzahl der verfügbaren Busse für eine Schule gleich 0 ist
        index = 0
        #while len(n_ava) > index:
           # if n_ava[index] == 0:
            #    for col in matrix:
             #       for zeile in matrix:
                        zeile[index] = 0
              #  del n_ava[index]
               # index-=1
            #index += 1
        while len(n_ava) > index:
            if n_ava[index] == 0:
                for col in matrix:
                    del col[index]
                del n_ava[index]
                index-=1
            index += 1

        print(matrix)
    # Ausgabe der gefilterten Daten

    return (n_reuse)

n_reuses =[]
n_reuse = 0
n_ava_index = [3, 5, 8, 2, 1, 2]
n_ava = [3, 5, 8, 2, 1, 2]
n_reuse_einzel= matrizenbearbeitung(matrix, n_ava, n_ava_index,n_reuse)
n_reuses.append(n_reuse_einzel)
#matrix =[[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
#n_reuse = 0
#n_ava_index = [3, 5, 8, 2, 1, 2]
#n_ava = [3, 5, 8, 2, 1, 2]
#n_reuse_einzel= matrizenbearbeitung(matrix, n_ava, n_ava_index,n_reuse)
#n_reuses.append(n_reuse_einzel)
#matrix =[[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
#n_reuse = 0
#n_ava_index = [3, 5, 8, 2, 1, 2]
#n_ava = [3, 5, 8, 2, 1, 2]
#n_reuse_einzel= matrizenbearbeitung(matrix, n_ava, n_ava_index,n_reuse)
#n_reuses.append(n_reuse_einzel)

print (n_reuses)






