import itertools
from Modul_tt import *
from Matrizenbearbeitung_felxibel import matrizenbearbeitung
import numpy as np
import pandas as pd

n_ava = [7,7,7,7,7,7,7] # Anzahl an Bussen, die an einer Schule ankommen, also die maximal Anzahl, die weiterverwendet werden kann
n_reuse = 0
n_reuses = []
busses_needed_without = 49 # wenn man keine Staffelung hat
busses_needed_now = None # bezieht sich auf aktuelle Uhrzeitenkombination
busses_needed_with = None
matrizen = []
schoolstart_combination = []
s1_start = [60]
s2_start = [60]
s3_start = [60]
s4_start = [60]
s5_start = [60]
s6_start = [60]
s7_start = [60]
Fahrzeit =10

starts=[s1_start,s2_start,s3_start,s4_start,s5_start,s6_start,s7_start]
total_minutes = 140
num_elements = 7

combinations_durchlauf=[]
def generate_partitions(total_minutes, num_elements):
    all_partitions = []

    for r in range(1, num_elements + 1):
        for comb in itertools.combinations(range(num_elements), r):

            value = total_minutes // r
            partition = [0] * num_elements
            for index in comb:
                partition[index] = value
            all_partitions.append(partition)

    return all_partitions

partitions = generate_partitions(total_minutes, num_elements)

combinations=[]

combinations_list=[]

for combination in partitions:

    # Reset start values for each combination
    s1_start = [60]
    s2_start = [60]
    s3_start = [60]
    s4_start = [60]
    s5_start = [60]
    s6_start = [60]
    s7_start = [60]
    all_starts = []

    # Extend start values based on combination
    if combination[0] == 140:
        s1_start.extend(
            [-10, 130])
    if combination[1] == 140:
        s2_start.extend(
            [-10, 130])
    if combination[2] == 140:
        s3_start.extend(
            [-10, 130])
    if combination[3] == 140:
        s4_start.extend([-10, 130])
    if combination[4] == 140:
        s5_start.extend([-10, 130])
    if combination[5] == 140:
        s6_start.extend([-10, 130])
    if combination[6] == 140:
        s7_start.extend([-10, 130])

    if combination[0] == 70:
        s1_start.extend([25,95])
    if combination[1] == 70:
        s2_start.extend([25,95])
    if combination[2] == 70:
        s3_start.extend([25,95])
    if combination[3] == 70:
        s4_start.extend([25,95])
    if combination[4] == 70:
        s5_start.extend([25,95])
    if combination[5] == 70:
        s6_start.extend([25,95])
    if combination[6] == 70:
        s7_start.extend([25,95])

    if combination[0] == 46:
        s1_start.extend([37,83])
    if combination[1] == 46:
        s2_start.extend([37,83])
    if combination[2] == 46:
        s3_start.extend([37,83])
    if combination[3] == 46:
        s4_start.extend([37,83])
    if combination[4] == 46:
        s5_start.extend([37,83])
    if combination[5] == 46:
        s6_start.extend([37,83])
    if combination[6] == 46:
        s7_start.extend([37,83])

    if combination[0] == 35:
        s1_start.extend([43, 78])
    if combination[1] == 35:
        s2_start.extend([43, 78])
    if combination[2] == 35:
        s3_start.extend([43, 78])
    if combination[3] == 35:
        s4_start.extend([43, 78])
    if combination[4] == 35:
        s5_start.extend([43, 78])
    if combination[5] == 35:
        s6_start.extend([43, 78])
    if combination[6] == 35:
        s7_start.extend([43, 78])

    if combination[0] == 28:
        s1_start.extend([46,74])
    if combination[1] == 28:
        s2_start.extend([46,74])
    if combination[2] == 28:
        s3_start.extend([46,74])
    if combination[3] == 28:
        s4_start.extend([46,74])
    if combination[4] == 28:
        s5_start.extend([46,74])
    if combination[5] == 28:
        s6_start.extend([46,74])
    if combination[6] == 28:
        s7_start.extend([46,74])

    if combination[0] == 23:
        s1_start.extend([48,72])
    if combination[1] == 23:
        s2_start.extend([48,72])
    if combination[2] == 23:
        s3_start.extend([48,72])
    if combination[3] == 23:
        s4_start.extend([48,72])
    if combination[4] == 23:
        s5_start.extend([48,72])
    if combination[5] == 23:
        s6_start.extend([48,72])
    if combination[6] == 23:
        s7_start.extend([48,72])

    if combination[0] == 20:
        s1_start.extend([50,70])

    if combination[1] == 20:
        s2_start.extend([50,70])

    if combination[2] == 20:
        s3_start.extend([50,70])

    if combination[3] == 20:
        s4_start.extend([50,70])

    if combination[4] == 20:
        s5_start.extend([50,70])

    if combination[5] == 20:
        s6_start.extend([50,70])

    if combination[6] == 20:
        s7_start.extend([50,70])

    starts = {
        "s1_start": s1_start,
        "s2_start": s2_start,
        "s3_start": s3_start,
        "s4_start": s4_start,
        "s5_start": s5_start,
        "s6_start": s6_start,
        "s7_start": s7_start
    }

    all_starts.append(starts)

    print(all_starts)
    combinations = itertools.product(s1_start, s2_start, s3_start, s4_start, s5_start, s6_start, s7_start)

    for combination_unten in combinations:

        print(combination_unten)
        s1_start, s2_start, s3_start, s4_start, s5_start, s6_start, s7_start = combination_unten

        # Unpack the combination into the four variables
        # Erstelle eine leere Matrix mit 6 Spalten und 21 Zeilen
        matrix = [[0 for _ in range(7)] for _ in range(49)]

        if s1_start + Fahrzeit < s2_start:
            matrix[7][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][0] = 1
        if s1_start + (2 * Fahrzeit) < s2_start:
            matrix[9][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][0] = 1
        if s1_start + (3 * Fahrzeit) < s2_start:
            matrix[11][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][0] = 1
        if s1_start + (4 * Fahrzeit) < s2_start:
            matrix[13][0] = 1

        if s1_start + Fahrzeit < s3_start:
            matrix[14][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][0] = 1
        if s1_start + (2 * Fahrzeit) < s3_start:
            matrix[16][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][0] = 1
        if s1_start + (3 * Fahrzeit) < s3_start:
            matrix[18][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][0] = 1
        if s1_start + (4 * Fahrzeit) < s3_start:
            matrix[20][0] = 1

        if s1_start + Fahrzeit < s4_start:
            matrix[21][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][0] = 1
        if s1_start + (2 * Fahrzeit) < s4_start:
            matrix[23][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][0] = 1
        if s1_start + (3 * Fahrzeit) < s4_start:
            matrix[25][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][0] = 1
        if s1_start + (4 * Fahrzeit) < s4_start:
            matrix[27][0] = 1

        if s1_start + Fahrzeit < s5_start:
            matrix[28][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][0] = 1
        if s1_start + (2 * Fahrzeit) < s5_start:
            matrix[30][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][0] = 1
        if s1_start + (3 * Fahrzeit) < s5_start:
            matrix[32][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][0] = 1
        if s1_start + (4 * Fahrzeit) < s5_start:
            matrix[34][0] = 1

        if s1_start + Fahrzeit < s6_start:
            matrix[35][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][0] = 1
        if s1_start + (2 * Fahrzeit) < s6_start:
            matrix[37][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][0] = 1
        if s1_start + (3 * Fahrzeit) < s6_start:
            matrix[39][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][0] = 1
        if s1_start + (4 * Fahrzeit) < s6_start:
            matrix[41][0] = 1

        if s1_start + Fahrzeit < s7_start:
            matrix[42][0] = 1
        if s1_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][0] = 1
        if s1_start + (2 * Fahrzeit) < s7_start:
            matrix[44][0] = 1
        if s1_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][0] = 1
        if s1_start + (3 * Fahrzeit) < s7_start:
            matrix[46][0] = 1
        if s1_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][0] = 1
        if s1_start + (4 * Fahrzeit) < s7_start:
            matrix[48][0] = 1

        if s2_start + Fahrzeit < s1_start:
            matrix[0][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][1] = 1
        if s2_start + (2 * Fahrzeit) < s1_start:
            matrix[2][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][1] = 1
        if s2_start + (3 * Fahrzeit) < s1_start:
            matrix[4][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][1] = 1
        if s2_start + (4 * Fahrzeit) < s1_start:
            matrix[6][1] = 1

        if s2_start + Fahrzeit < s3_start:
            matrix[14][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][1] = 1
        if s2_start + (2 * Fahrzeit) < s3_start:
            matrix[16][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][1] = 1
        if s2_start + (3 * Fahrzeit) < s3_start:
            matrix[18][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][1] = 1
        if s2_start + (4 * Fahrzeit) < s3_start:
            matrix[20][1] = 1

        if s2_start + Fahrzeit < s4_start:
            matrix[21][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][1] = 1
        if s2_start + (2 * Fahrzeit) < s4_start:
            matrix[23][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][1] = 1
        if s2_start + (3 * Fahrzeit) < s4_start:
            matrix[25][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][1] = 1
        if s2_start + (4 * Fahrzeit) < s4_start:
            matrix[27][1] = 1

        if s2_start + Fahrzeit < s5_start:
            matrix[28][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][1] = 1
        if s2_start + (2 * Fahrzeit) < s5_start:
            matrix[30][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][1] = 1
        if s2_start + (3 * Fahrzeit) < s5_start:
            matrix[32][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][1] = 1
        if s2_start + (4 * Fahrzeit) < s5_start:
            matrix[34][1] = 1

        if s2_start + Fahrzeit < s6_start:
            matrix[35][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][1] = 1
        if s2_start + (2 * Fahrzeit) < s6_start:
            matrix[37][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][1] = 1
        if s2_start + (3 * Fahrzeit) < s6_start:
            matrix[39][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][1] = 1
        if s2_start + (4 * Fahrzeit) < s6_start:
            matrix[41][1] = 1

        if s2_start + Fahrzeit < s7_start:
            matrix[42][1] = 1
        if s2_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][1] = 1
        if s2_start + (2 * Fahrzeit) < s7_start:
            matrix[44][1] = 1
        if s2_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][1] = 1
        if s2_start + (3 * Fahrzeit) < s7_start:
            matrix[46][1] = 1
        if s2_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][1] = 1
        if s2_start + (4 * Fahrzeit) < s7_start:
            matrix[48][1] = 1

        if s3_start + Fahrzeit < s1_start:
            matrix[0][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][2] = 1
        if s3_start + (2 * Fahrzeit) < s1_start:
            matrix[2][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][2] = 1
        if s3_start + (3 * Fahrzeit) < s1_start:
            matrix[4][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][2] = 1
        if s3_start + (4 * Fahrzeit) < s1_start:
            matrix[6][2] = 1

        if s3_start + Fahrzeit < s2_start:
            matrix[7][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][2] = 1
        if s3_start + (2 * Fahrzeit) < s2_start:
            matrix[9][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][2] = 1
        if s3_start + (3 * Fahrzeit) < s2_start:
            matrix[11][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][2] = 1
        if s3_start + (4 * Fahrzeit) < s2_start:
            matrix[13][2] = 1

        if s3_start + Fahrzeit < s4_start:
            matrix[21][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][2] = 1
        if s3_start + (2 * Fahrzeit) < s4_start:
            matrix[23][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][2] = 1
        if s3_start + (3 * Fahrzeit) < s4_start:
            matrix[25][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][2] = 1
        if s3_start + (4 * Fahrzeit) < s4_start:
            matrix[27][2] = 1

        if s3_start + Fahrzeit < s5_start:
            matrix[28][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][2] = 1
        if s3_start + (2 * Fahrzeit) < s5_start:
            matrix[30][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][2] = 1
        if s3_start + (3 * Fahrzeit) < s5_start:
            matrix[32][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][2] = 1
        if s3_start + (4 * Fahrzeit) < s5_start:
            matrix[34][2] = 1

        if s3_start + Fahrzeit < s6_start:
            matrix[35][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][2] = 1
        if s3_start + (2 * Fahrzeit) < s6_start:
            matrix[37][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][2] = 1
        if s3_start + (3 * Fahrzeit) < s6_start:
            matrix[39][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][2] = 1
        if s3_start + (4 * Fahrzeit) < s6_start:
            matrix[41][2] = 1

        if s3_start + Fahrzeit < s7_start:
            matrix[42][2] = 1
        if s3_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][2] = 1
        if s3_start + (2 * Fahrzeit) < s7_start:
            matrix[44][2] = 1
        if s3_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][2] = 1
        if s3_start + (3 * Fahrzeit) < s7_start:
            matrix[46][2] = 1
        if s3_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][2] = 1
        if s3_start + (4 * Fahrzeit) < s7_start:
            matrix[48][2] = 1

        if s4_start + Fahrzeit < s1_start:
            matrix[0][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][3] = 1
        if s4_start + (2 * Fahrzeit) < s1_start:
            matrix[2][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][3] = 1
        if s4_start + (3 * Fahrzeit) < s1_start:
            matrix[4][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][3] = 1
        if s4_start + (4 * Fahrzeit) < s1_start:
            matrix[6][3] = 1

        if s4_start + Fahrzeit < s2_start:
            matrix[7][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][3] = 1
        if s4_start + (2 * Fahrzeit) < s2_start:
            matrix[9][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][3] = 1
        if s4_start + (3 * Fahrzeit) < s2_start:
            matrix[11][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][3] = 1
        if s4_start + (4 * Fahrzeit) < s2_start:
            matrix[13][3] = 1

        if s4_start + Fahrzeit < s3_start:
            matrix[14][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][3] = 1
        if s4_start + (2 * Fahrzeit) < s3_start:
            matrix[16][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][3] = 1
        if s4_start + (3 * Fahrzeit) < s3_start:
            matrix[18][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][3] = 1
        if s4_start + (4 * Fahrzeit) < s3_start:
            matrix[20][3] = 1

        if s4_start + Fahrzeit < s5_start:
            matrix[28][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][3] = 1
        if s4_start + (2 * Fahrzeit) < s5_start:
            matrix[30][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][3] = 1
        if s4_start + (3 * Fahrzeit) < s5_start:
            matrix[32][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][3] = 1
        if s4_start + (4 * Fahrzeit) < s5_start:
            matrix[34][3] = 1

        if s4_start + Fahrzeit < s6_start:
            matrix[35][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][3] = 1
        if s4_start + (2 * Fahrzeit) < s6_start:
            matrix[37][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][3] = 1
        if s4_start + (3 * Fahrzeit) < s6_start:
            matrix[39][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][3] = 1
        if s4_start + (4 * Fahrzeit) < s6_start:
            matrix[41][3] = 1

        if s4_start + Fahrzeit < s7_start:
            matrix[42][3] = 1
        if s4_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][3] = 1
        if s4_start + (2 * Fahrzeit) < s7_start:
            matrix[44][3] = 1
        if s4_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][3] = 1
        if s4_start + (3 * Fahrzeit) < s7_start:
            matrix[46][3] = 1
        if s4_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][3] = 1
        if s4_start + (4 * Fahrzeit) < s7_start:
            matrix[48][3] = 1

        if s5_start + Fahrzeit < s1_start:
            matrix[0][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][4] = 1
        if s5_start + (2 * Fahrzeit) < s1_start:
            matrix[2][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][4] = 1
        if s5_start + (3 * Fahrzeit) < s1_start:
            matrix[4][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][4] = 1
        if s5_start + (4 * Fahrzeit) < s1_start:
            matrix[6][4] = 1

        if s5_start + Fahrzeit < s2_start:
            matrix[7][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][4] = 1
        if s5_start + (2 * Fahrzeit) < s2_start:
            matrix[9][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][4] = 1
        if s5_start + (3 * Fahrzeit) < s2_start:
            matrix[11][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][4] = 1
        if s5_start + (4 * Fahrzeit) < s2_start:
            matrix[13][4] = 1

        if s5_start + Fahrzeit < s3_start:
            matrix[14][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][4] = 1
        if s5_start + (2 * Fahrzeit) < s3_start:
            matrix[16][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][4] = 1
        if s5_start + (3 * Fahrzeit) < s3_start:
            matrix[18][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][4] = 1
        if s5_start + (4 * Fahrzeit) < s3_start:
            matrix[20][4] = 1

        if s5_start + Fahrzeit < s4_start:
            matrix[21][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][4] = 1
        if s5_start + (2 * Fahrzeit) < s4_start:
            matrix[23][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][4] = 1
        if s5_start + (3 * Fahrzeit) < s4_start:
            matrix[25][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][4] = 1
        if s5_start + (4 * Fahrzeit) < s4_start:
            matrix[27][4] = 1

        if s5_start + Fahrzeit < s6_start:
            matrix[35][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][4] = 1
        if s5_start + (2 * Fahrzeit) < s6_start:
            matrix[37][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][4] = 1
        if s5_start + (3 * Fahrzeit) < s6_start:
            matrix[39][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][4] = 1
        if s5_start + (4 * Fahrzeit) < s6_start:
            matrix[41][4] = 1

        if s5_start + Fahrzeit < s7_start:
            matrix[42][4] = 1
        if s5_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][4] = 1
        if s5_start + (2 * Fahrzeit) < s7_start:
            matrix[44][4] = 1
        if s5_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][4] = 1
        if s5_start + (3 * Fahrzeit) < s7_start:
            matrix[46][4] = 1
        if s5_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][4] = 1
        if s5_start + (4 * Fahrzeit) < s7_start:
            matrix[48][4] = 1

        if s6_start + Fahrzeit < s1_start:
            matrix[0][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][5] = 1
        if s6_start + (2 * Fahrzeit) < s1_start:
            matrix[2][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][5] = 1
        if s6_start + (3 * Fahrzeit) < s1_start:
            matrix[4][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][5] = 1
        if s6_start + (4 * Fahrzeit) < s1_start:
            matrix[6][5] = 1

        if s6_start + Fahrzeit < s2_start:
            matrix[7][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][5] = 1
        if s6_start + (2 * Fahrzeit) < s2_start:
            matrix[9][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][5] = 1
        if s6_start + (3 * Fahrzeit) < s2_start:
            matrix[11][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][5] = 1
        if s6_start + (4 * Fahrzeit) < s2_start:
            matrix[13][5] = 1

        if s6_start + Fahrzeit < s3_start:
            matrix[14][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][5] = 1
        if s6_start + (2 * Fahrzeit) < s3_start:
            matrix[16][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][5] = 1
        if s6_start + (3 * Fahrzeit) < s3_start:
            matrix[18][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][5] = 1
        if s6_start + (4 * Fahrzeit) < s3_start:
            matrix[20][5] = 1

        if s6_start + Fahrzeit < s4_start:
            matrix[21][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][5] = 1
        if s6_start + (2 * Fahrzeit) < s4_start:
            matrix[23][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][5] = 1
        if s6_start + (3 * Fahrzeit) < s4_start:
            matrix[25][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][5] = 1
        if s6_start + (4 * Fahrzeit) < s4_start:
            matrix[27][5] = 1

        if s6_start + Fahrzeit < s5_start:
            matrix[28][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][5] = 1
        if s6_start + (2 * Fahrzeit) < s5_start:
            matrix[30][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][5] = 1
        if s6_start + (3 * Fahrzeit) < s5_start:
            matrix[32][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][5] = 1
        if s6_start + (4 * Fahrzeit) < s5_start:
            matrix[34][5] = 1

        if s6_start + Fahrzeit < s7_start:
            matrix[42][5] = 1
        if s6_start + (1.5 * Fahrzeit) < s7_start:
            matrix[43][5] = 1
        if s6_start + (2 * Fahrzeit) < s7_start:
            matrix[44][5] = 1
        if s6_start + (2.5 * Fahrzeit) < s7_start:
            matrix[45][5] = 1
        if s6_start + (3 * Fahrzeit) < s7_start:
            matrix[46][5] = 1
        if s6_start + (3.5 * Fahrzeit) < s7_start:
            matrix[47][5] = 1
        if s6_start + (4 * Fahrzeit) < s7_start:
            matrix[48][5] = 1

        if s7_start + Fahrzeit < s1_start:
            matrix[0][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s1_start:
            matrix[1][6] = 1
        if s7_start + (2 * Fahrzeit) < s1_start:
            matrix[2][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s1_start:
            matrix[3][6] = 1
        if s7_start + (3 * Fahrzeit) < s1_start:
            matrix[4][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s1_start:
            matrix[5][6] = 1
        if s7_start + (4 * Fahrzeit) < s1_start:
            matrix[6][6] = 1

        if s7_start + Fahrzeit < s2_start:
            matrix[7][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s2_start:
            matrix[8][6] = 1
        if s7_start + (2 * Fahrzeit) < s2_start:
            matrix[9][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s2_start:
            matrix[10][6] = 1
        if s7_start + (3 * Fahrzeit) < s2_start:
            matrix[11][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s2_start:
            matrix[12][6] = 1
        if s7_start + (4 * Fahrzeit) < s2_start:
            matrix[13][6] = 1

        if s7_start + Fahrzeit < s3_start:
            matrix[14][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s3_start:
            matrix[15][6] = 1
        if s7_start + (2 * Fahrzeit) < s3_start:
            matrix[16][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s3_start:
            matrix[17][6] = 1
        if s7_start + (3 * Fahrzeit) < s3_start:
            matrix[18][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s3_start:
            matrix[19][6] = 1
        if s7_start + (4 * Fahrzeit) < s3_start:
            matrix[20][6] = 1

        if s7_start + Fahrzeit < s4_start:
            matrix[21][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s4_start:
            matrix[22][6] = 1
        if s7_start + (2 * Fahrzeit) < s4_start:
            matrix[23][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s4_start:
            matrix[24][6] = 1
        if s7_start + (3 * Fahrzeit) < s4_start:
            matrix[25][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s4_start:
            matrix[26][6] = 1
        if s7_start + (4 * Fahrzeit) < s4_start:
            matrix[27][6] = 1

        if s7_start + Fahrzeit < s5_start:
            matrix[28][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s5_start:
            matrix[29][6] = 1
        if s7_start + (2 * Fahrzeit) < s5_start:
            matrix[30][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s5_start:
            matrix[31][6] = 1
        if s7_start + (3 * Fahrzeit) < s5_start:
            matrix[32][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s5_start:
            matrix[33][6] = 1
        if s7_start + (4 * Fahrzeit) < s5_start:
            matrix[34][6] = 1

        if s7_start + Fahrzeit < s6_start:
            matrix[35][6] = 1
        if s7_start + (1.5 * Fahrzeit) < s6_start:
            matrix[36][6] = 1
        if s7_start + (2 * Fahrzeit) < s6_start:
            matrix[37][6] = 1
        if s7_start + (2.5 * Fahrzeit) < s6_start:
            matrix[38][6] = 1
        if s7_start + (3 * Fahrzeit) < s6_start:
            matrix[39][6] = 1
        if s7_start + (3.5 * Fahrzeit) < s6_start:
            matrix[40][6] = 1
        if s7_start + (4 * Fahrzeit) < s6_start:
            matrix[41][6] = 1

        # Print the result for the current combination
        # print(f"Combination: {combination}, Result: {matrix}")
        matrizen.append(matrix)
        schoolstart_combination.append(combination)
n_reuses = []

for matrix in matrizen:
    max_anfahrten = [0, 0, 0, 0, 0, 0, 0]
    n_ava_unverbraucht = [7,7,7,7,7,7,7]
    n_ava = [7,7,7,7,7,7,7]
    n_anfahrten = [7,7,7,7,7,7,7]
    n_reuse = 0
    n_reuse_einzel = matrizenbearbeitung(matrix, n_ava, n_ava_unverbraucht, n_reuse, max_anfahrten, n_anfahrten)
    n_reuses.append(n_reuse_einzel)

print(n_reuses)

for i in combinations:
    print(n_reuses[i])

data = []


for i in range(len(schoolstart_combination)):
    data.append((schoolstart_combination[i], n_reuses[i]))

# Erstellen eines DataFrames aus den Daten
df = pd.DataFrame(data, columns=['Combination', 'ReuseValue'])

print(df)

with open('datei', 'w') as file:
    file.write(df.to_string())

# Gruppieren nach Kombinationen und Finden des maximalen Wiederverwendungswerts für jede Gruppe
max_reuse_per_combination = df.groupby('Combination')['ReuseValue'].max()

# Ausgabe des Ergebnisses
print(max_reuse_per_combination)
max_reuse_per_combination_dataframe=pd.DataFrame(max_reuse_per_combination)