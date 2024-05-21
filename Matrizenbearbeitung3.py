import random
#import numpy as np

a=6 # Anzahl Schulen
b = 21 # Anzahl zu betrachtende Wege
 # Anzahl an Bussen, die an einer Schule ankommen, also die maximal Anzahl, die weiterverwendet werden kann
#n_reuse = 0

matrix = [[random.randint(0, 1) for _ in range(a)] for _ in range(b)]
matrix=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]
for row in matrix:
    print(row)

#If Sj ==1: there is a single cell aij with a value of 1. This means that there is only is one way to re-use a bus to cover the route j.
# We increase the number of times a bus is re-used in the alternative, n_reuse, by 1.
#for row in matrix:
 #   row_sum = sum(row)
  #  if row_sum == 1:
   #     n_reuse += 1
def matrizenbearbeitung (matrix, n_ava, n_ava_unverbraucht,n_reuse,max_anfahrten,n_anfahrten):
    print(matrix)
    print(n_ava)
    print(n_ava_unverbraucht)
    print(n_reuse)

    while any(value > 0 for value in n_ava):
        print("---------------------------------------")
        row_index = 0
        for row in matrix:
            row_sum = sum(row)

            #if row_sum == 1:
             #   index2=row.index(1)
              #  column_sums = [sum(matrix[i][index2] for i in range(row_index) if sum(matrix[i]) == 1)]
               # print(index2)
                #print("n_ava_index"+str(n_ava_unverbraucht[index2]))
                #print(column_sums[0])

                #if column_sums[0] <= n_ava_unverbraucht[index2] and n_ava_unverbraucht[index2]>0:
                 #   n_reuse += 1
                  #  n_ava_unverbraucht[index2] -=1
                #print ("n_ava_index_nach"+str(n_ava_unverbraucht[index2]))
                #print("Row_index"+ str(row_index))
                #print(n_reuse)
            #print(n_ava_index)
            #row_index += 1

            if row_sum == 1:
                index2=row.index(1)
                column_sums = [sum(matrix[i][index2] for i in range(row_index) if sum(matrix[i]) == 1)]
                print(index2)
                print("n_ava_index"+str(n_ava_unverbraucht[index2]))
                print(column_sums[0])

                if n_ava_unverbraucht[index2]>0 and max_anfahrten[index2]<n_anfahrten[index2]:
                    n_reuse += 1
                    n_ava_unverbraucht[index2] -=1
                    for i in range(len(row)):
                        row[i] = 0


                    print(index2)
                    print("max_Anfahrten")
                    print(max_anfahrten)
                    if row_index <= 15:
                        max_anfahrten[0]+=1
                    if row_index >= 16 and row_index <= 20 :
                        max_anfahrten[1]+=1
                    if row_index >= 21 and row_index <= 35:
                        max_anfahrten[2]+=1
                    if row_index == 36 :
                        max_anfahrten[3]+=1
                    if row_index >= 37 and row_index <= 40:
                        max_anfahrten[4]+=1
                    if row_index >= 41 and row_index <= 42:
                        max_anfahrten[5]+=1
                    if row_index >= 43:
                        max_anfahrten[6]+=1
                    print (max_anfahrten)

                print ("n_ava_index_nach"+str(n_ava_unverbraucht[index2]))
                print("Row_index"+ str(row_index))
                print (max_anfahrten)
                print(n_reuse)
            #print(n_ava_index)
            row_index += 1


        # All columns "in meinem Fall Zeilen" wo Sj < 2 werden gelöscht
        #matrix = [row for row in matrix if sum(row) >= 2]

        #We decrease the number of buses available for re-use at the school represented by row j, n_availablej, by 1.
        for a in range(len(n_ava)):
            n_ava[a] -= 1

        print(n_ava)
        print(n_ava_unverbraucht)
        #n_ava_unverbraucht = [x for x in n_ava_unverbraucht if x != 0]
        # bevor eine spalte gelöscht wird, wird nochmal überprüft, ob es dort eine Möglichkeit gibt etwas wiederzuwerdenden
        for i in range(len(n_ava)):
            row_index2=0
            if n_ava[i] is not None:
                if n_ava [i] ==0:
                    print("Hallo")
                    for zeile in matrix:
                        print("i"+str(i))
                        print(zeile[i])
                        index3=zeile[i]
                        print(n_ava[i])
                        print(n_ava_unverbraucht [i])
                        print(row_index2)

                        if zeile[i] == 1 and n_ava_unverbraucht[i] > 0 and max_anfahrten[index3]<n_anfahrten[index3]:
                            print("hier")
                            print(zeile)
                            for j in range(len(zeile)):
                                zeile[j] = 0
                            print(zeile)
                            n_ava_unverbraucht[i] -= 1
                            if n_ava_unverbraucht [i] ==0:
                                n_ava_unverbraucht [i] = -1
                            print(n_ava_unverbraucht)
                            print("Max anfahrten_unten")
                            print(max_anfahrten)
                            if row_index2 < 16:
                                max_anfahrten[0] += 1
                            if row_index2 >= 16 and row_index2 <= 20:
                                max_anfahrten[1] += 1
                            if row_index2 >= 21 and row_index2 <= 35:
                                max_anfahrten[2] += 1
                            if row_index2 == 36:
                                max_anfahrten[3] += 1
                            if row_index2 >= 37 and row_index2 <= 40:
                                max_anfahrten[4] += 1
                            if row_index2 >= 41 and row_index2 <= 42:
                                max_anfahrten[5] += 1
                            if row_index2 >= 43:
                                max_anfahrten[6] += 1
                            print(max_anfahrten)
                            n_reuse +=1

                        row_index2 +=1
                        print (row_index2)
        if n_ava [a] ==0:
            n_ava [a] = -1




        print(n_reuse)

         # Entfernen der Spalten aus der Matrix, wenn die Anzahl der verfügbaren Busse für eine Schule gleich 0 ist
        index = 0
        print(n_ava)
        #while index < len(n_ava):
         #   if n_ava[index] == 0:
          #      for row in matrix:
           #         del row
            #    del n_ava[index]
             #   index -= 1
            #index += 1
        while len(n_ava) > index:
            if n_ava[index] == 0:
                for row in matrix:
                    row[index] = 0
            index += 1
        print(matrix)
        print(n_reuse)
    # Ausgabe der gefilterten Daten

    return (n_reuse)


print(matrix)
n_reuses =[]
n_reuse = 0
n_ava_unverbraucht = [17, 4, 15, 1, 4, 2, 3]
n_ava = [17, 4, 15, 1, 4, 2, 3]
n_anfahrten = [17, 4, 15, 1, 4, 2, 3]
max_anfahrten =[0,0,0,0,0,0,0]
durchlauf=0

n_reuse_einzel= matrizenbearbeitung(matrix, n_ava, n_ava_unverbraucht,n_reuse,max_anfahrten,n_anfahrten)
n_reuses.append(n_reuse_einzel)


print (n_reuses)






