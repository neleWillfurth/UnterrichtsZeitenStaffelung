#Maximale Änderung  hinten 10 Minuten (innerhalb Zeitkorridor 40 Minuten)
import itertools
from Modul_tt import *
from Matrizenbearbeitung3 import matrizenbearbeitung

n_ava = [17, 4, 15, 1, 4, 2, 3] # Anzahl an Bussen, die an einer Schule ankommen, also die maximal Anzahl, die weiterverwendet werden kann
n_reuse = 0
n_reuses = []
busses_needed_without = 46 # wenn man keine Staffelung hat
busses_needed_now = None # bezieht sich auf aktuelle Uhrzeitenkombination
busses_needed_with = None
# Busankuftszeit der Schulen festlegen in Minuten ab 7:00
s1_start = [20]
s2_start = [20,30]
s3_start = [15,20]
s4_start = [40,50]
s5_start = [20,30]
s6_start = [40,50]
s7_start = [20,30]
# Generate all possible combinations of values for the four variables

combinations = itertools.product(s1_start, s2_start, s3_start, s4_start, s5_start, s6_start, s7_start)
matrizen = []
schoolstart_combination = []

print(combinations)

for combination in combinations:

    s1_start, s2_start, s3_start, s4_start, s5_start, s6_start,s7_start = combination
    # Unpack the combination into the four variables
    # Erstelle eine leere Matrix mit 6 Spalten und 21 Zeilen
    matrix = [[0 for _ in range(7)] for _ in range(46)]
    min_val = min(combination)
    max_val = max(combination)
    if max_val - min_val <= 40:

        if s1_start + tts1h1_s2 < s2_start:
            matrix[17][0] = 1
        if s1_start + tts1h2_s2 < s2_start:
            matrix[18][0] = 1
        if s1_start + tts1h3_s2 < s2_start:
            matrix[19][0] = 1
        if s1_start + tts1h4_s2 < s2_start:
            matrix[20][0] = 1
        if s1_start + tts1h1_s3 < s3_start:
            matrix[21][0] = 1
        if s1_start + tts1h2_s3 < s3_start:
            matrix[22][0] = 1
        if s1_start + tts1h3_s3 < s3_start:
            matrix[23][0] = 1
        if s1_start + tts1h4_s3 < s3_start:
            matrix[24][0] = 1
        if s1_start + tts1h5_s3 < s3_start:
            matrix[25][0] = 1
        if s1_start + tts1h6_s3 < s3_start:
            matrix[26][0] = 1
        if s1_start + tts1h7_s3 < s3_start:
            matrix[27][0] = 1
        if s1_start + tts1h8_s3 < s3_start:
            matrix[28][0] = 1
        if s1_start + tts1h9_s3 < s3_start:
            matrix[29][0] = 1
        if s1_start + tts1h10_s3 < s3_start:
            matrix[30][0] = 1
        if s1_start + tts1h11_s3 < s3_start:
            matrix[31][0] = 1
        if s1_start + tts1h12_s3 < s3_start:
            matrix[32][0] = 1
        if s1_start + tts1h13_s3 < s3_start:
            matrix[33][0] = 1
        if s1_start + tts1h14_s3 < s3_start:
            matrix[34][0] = 1
        if s1_start + tts1h15_s3 < s3_start:
            matrix[35][0] = 1
        if s1_start + tts1h1_s4 < s4_start:
            matrix[36][0] = 1
        if s1_start + tts1h1_s5 < s5_start:
            matrix[37][0] = 1
        if s1_start + tts1h2_s5 < s5_start:
            matrix[38][0] = 1
        if s1_start + tts1h3_s5 < s5_start:
            matrix[39][0] = 1
        if s1_start + tts1h4_s5 < s5_start:
            matrix[40][0] = 1
        if s1_start + tts1h1_s6 < s6_start:
            matrix[41][0] = 1
        if s1_start + tts1h2_s6 < s6_start:
            matrix[42][0] = 1
        if s1_start + tts1h1_s7 < s7_start:
            matrix[43][0] = 1
        if s1_start + tts1h2_s7 < s7_start:
            matrix[44][0] = 1
        if s1_start + tts1h3_s7 < s7_start:
            matrix[45][0] = 1

        if s2_start + tts2h1_s1 < s1_start:
            matrix[0][1] = 1
        if s2_start + tts2h2_s1 < s1_start:
            matrix[1][1] = 1
        if s2_start + tts2h3_s1 < s1_start:
            matrix[2][1] = 1
        if s2_start + tts2h4_s1 < s1_start:
            matrix[3][1] = 1
        if s2_start + tts2h5_s1 < s1_start:
            matrix[4][1] = 1
        if s2_start + tts2h6_s1 < s1_start:
            matrix[5][1] = 1
        if s2_start + tts2h7_s1 < s1_start:
            matrix[6][1] = 1
        if s2_start + tts2h8_s1 < s1_start:
            matrix[7][1] = 1
        if s2_start + tts2h9_s1 < s1_start:
            matrix[8][1] = 1
        if s2_start + tts2h10_s1 < s1_start:
            matrix[9][1] = 1
        if s2_start + tts2h11_s1 < s1_start:
            matrix[10][1] = 1
        if s2_start + tts2h12_s1 < s1_start:
            matrix[11][1] = 1
        if s2_start + tts2h13_s1 < s1_start:
            matrix[12][1] = 1
        if s2_start + tts2h14_s1 < s1_start:
            matrix[13][1] = 1
        if s2_start + tts2h15_s1 < s1_start:
            matrix[14][1] = 1
        if s2_start + tts2h16_s1 < s1_start:
            matrix[15][1] = 1
        if s2_start + tts2h17_s1 < s1_start:
            matrix[16][1] = 1
        if s2_start + tts2h1_s3 < s3_start:
            matrix[21][1] = 1
        if s2_start + tts2h2_s3 < s3_start:
            matrix[22][1] = 1
        if s2_start + tts2h3_s3 < s3_start:
            matrix[23][1] = 1
        if s2_start + tts2h4_s3 < s3_start:
            matrix[24][1] = 1
        if s2_start + tts2h5_s3 < s3_start:
            matrix[25][1] = 1
        if s2_start + tts2h6_s3 < s3_start:
            matrix[26][1] = 1
        if s2_start + tts2h7_s3 < s3_start:
            matrix[27][1] = 1
        if s2_start + tts2h8_s3 < s3_start:
            matrix[28][1] = 1
        if s2_start + tts2h9_s3 < s3_start:
            matrix[29][1] = 1
        if s2_start + tts2h10_s3 < s3_start:
            matrix[30][1] = 1
        if s2_start + tts2h11_s3 < s3_start:
            matrix[31][1] = 1
        if s2_start + tts2h12_s3 < s3_start:
            matrix[32][1] = 1
        if s2_start + tts2h13_s3 < s3_start:
            matrix[33][1] = 1
        if s2_start + tts2h14_s3 < s3_start:
            matrix[34][1] = 1
        if s2_start + tts2h15_s3 < s3_start:
            matrix[35][1] = 1
        if s2_start + tts2h1_s4 < s4_start:
            matrix[36][1] = 1
        if s2_start + tts2h1_s5 < s5_start:
            matrix[37][1] = 1
        if s2_start + tts2h2_s5 < s5_start:
            matrix[38][1] = 1
        if s2_start + tts2h3_s5 < s5_start:
            matrix[39][1] = 1
        if s2_start + tts2h4_s5 < s5_start:
            matrix[40][1] = 1
        if s2_start + tts2h1_s6 < s6_start:
            matrix[41][1] = 1
        if s2_start + tts2h2_s6 < s6_start:
            matrix[42][1] = 1
        if s2_start + tts2h1_s7 < s7_start:
            matrix[43][1] = 1
        if s2_start + tts2h2_s7 < s7_start:
            matrix[44][1] = 1
        if s2_start + tts2h3_s7 < s7_start:
            matrix[45][1] = 1

        if s3_start + tts3h1_s1 < s1_start:
            matrix[0][2] = 1
        if s3_start + tts3h2_s1 < s1_start:
            matrix[1][2] = 1
        if s3_start + tts3h3_s1 < s1_start:
            matrix[2][2] = 1
        if s3_start + tts3h4_s1 < s1_start:
            matrix[3][2] = 1
        if s3_start + tts3h5_s1 < s1_start:
            matrix[4][2] = 1
        if s3_start + tts3h6_s1 < s1_start:
            matrix[5][2] = 1
        if s3_start + tts3h7_s1 < s1_start:
            matrix[6][2] = 1
        if s3_start + tts3h8_s1 < s1_start:
            matrix[7][2] = 1
        if s3_start + tts3h9_s1 < s1_start:
            matrix[8][2] = 1
        if s3_start + tts3h10_s1 < s1_start:
            matrix[9][2] = 1
        if s3_start + tts3h11_s1 < s1_start:
            matrix[10][2] = 1
        if s3_start + tts3h12_s1 < s1_start:
            matrix[11][2] = 1
        if s3_start + tts3h13_s1 < s1_start:
            matrix[12][2] = 1
        if s3_start + tts3h14_s1 < s1_start:
            matrix[13][2] = 1
        if s3_start + tts3h15_s1 < s1_start:
            matrix[14][2] = 1
        if s3_start + tts3h16_s1 < s1_start:
            matrix[15][2] = 1
        if s3_start + tts3h17_s1 < s1_start:
            matrix[16][2] = 1
        if s3_start + tts3h1_s2 < s2_start:
            matrix[17][2] = 1
        if s3_start + tts3h2_s2 < s2_start:
            matrix[18][2] = 1
        if s3_start + tts3h3_s2 < s2_start:
            matrix[19][2] = 1
        if s3_start + tts3h4_s2 < s2_start:
            matrix[20][2] = 1
        if s3_start + tts3h1_s4 < s4_start:
            matrix[36][2] = 1
        if s3_start + tts3h1_s5 < s5_start:
            matrix[37][2] = 1
        if s3_start + tts3h2_s5 < s5_start:
            matrix[38][2] = 1
        if s3_start + tts3h3_s5 < s5_start:
            matrix[39][2] = 1
        if s3_start + tts3h4_s5 < s5_start:
            matrix[40][2] = 1
        if s3_start + tts3h1_s6 < s6_start:
            matrix[41][2] = 1
        if s3_start + tts3h2_s6 < s6_start:
            matrix[42][2] = 1
        if s3_start + tts3h1_s7 < s7_start:
            matrix[43][2] = 1
        if s3_start + tts3h2_s7 < s7_start:
            matrix[44][2] = 1
        if s3_start + tts3h3_s7 < s7_start:
            matrix[45][2] = 1

        if s4_start + tts4h1_s1 < s1_start:
            matrix[0][3] = 1
        if s4_start + tts4h2_s1 < s1_start:
            matrix[1][3] = 1
        if s4_start + tts4h3_s1 < s1_start:
            matrix[2][3] = 1
        if s4_start + tts4h4_s1 < s1_start:
            matrix[3][3] = 1
        if s4_start + tts4h5_s1 < s1_start:
            matrix[4][3] = 1
        if s4_start + tts4h6_s1 < s1_start:
            matrix[5][3] = 1
        if s4_start + tts4h7_s1 < s1_start:
            matrix[6][3] = 1
        if s4_start + tts4h8_s1 < s1_start:
            matrix[7][3] = 1
        if s4_start + tts4h9_s1 < s1_start:
            matrix[8][3] = 1
        if s4_start + tts4h10_s1 < s1_start:
            matrix[9][3] = 1
        if s4_start + tts4h11_s1 < s1_start:
            matrix[10][3] = 1
        if s4_start + tts4h12_s1 < s1_start:
            matrix[11][3] = 1
        if s4_start + tts4h13_s1 < s1_start:
            matrix[12][3] = 1
        if s4_start + tts4h14_s1 < s1_start:
            matrix[13][3] = 1
        if s4_start + tts4h15_s1 < s1_start:
            matrix[14][3] = 1
        if s4_start + tts4h16_s1 < s1_start:
            matrix[15][3] = 1
        if s4_start + tts4h17_s1 < s1_start:
            matrix[16][3] = 1
        if s4_start + tts4h1_s2 < s2_start:
            matrix[17][3] = 1
        if s4_start + tts4h2_s2 < s2_start:
            matrix[18][3] = 1
        if s4_start + tts4h3_s2 < s2_start:
            matrix[19][3] = 1
        if s4_start + tts4h4_s2 < s2_start:
            matrix[20][3] = 1
        if s4_start + tts4h1_s3 < s3_start:
            matrix[21][3] = 1
        if s4_start + tts4h2_s3 < s3_start:
            matrix[22][3] = 1
        if s4_start + tts4h3_s3 < s3_start:
            matrix[23][3] = 1
        if s4_start + tts4h4_s3 < s3_start:
            matrix[24][3] = 1
        if s4_start + tts4h5_s3 < s3_start:
            matrix[25][3] = 1
        if s4_start + tts4h6_s3 < s3_start:
            matrix[26][3] = 1
        if s4_start + tts4h7_s3 < s3_start:
            matrix[27][3] = 1
        if s4_start + tts4h8_s3 < s3_start:
            matrix[28][3] = 1
        if s4_start + tts4h9_s3 < s3_start:
            matrix[29][3] = 1
        if s4_start + tts4h10_s3 < s3_start:
            matrix[30][3] = 1
        if s4_start + tts4h11_s3 < s3_start:
            matrix[31][3] = 1
        if s4_start + tts4h12_s3 < s3_start:
            matrix[32][3] = 1
        if s4_start + tts4h13_s3 < s3_start:
            matrix[33][3] = 1
        if s4_start + tts4h14_s3 < s3_start:
            matrix[34][3] = 1
        if s4_start + tts4h15_s3 < s3_start:
            matrix[35][3] = 1
        if s4_start + tts4h1_s5 < s5_start:
            matrix[37][3] = 1
        if s4_start + tts4h2_s5 < s5_start:
            matrix[38][3] = 1
        if s4_start + tts4h3_s5 < s5_start:
            matrix[39][3] = 1
        if s4_start + tts4h4_s5 < s5_start:
            matrix[40][3] = 1
        if s4_start + tts4h1_s6 < s6_start:
            matrix[41][3] = 1
        if s4_start + tts4h2_s6 < s6_start:
            matrix[42][3] = 1
        if s4_start + tts4h1_s7 < s7_start:
            matrix[43][3] = 1
        if s4_start + tts4h2_s7 < s7_start:
            matrix[44][3] = 1
        if s4_start + tts4h3_s7 < s7_start:
            matrix[45][3] = 1

        if s5_start + tts5h1_s1 < s1_start:
            matrix[0][4] = 1
        if s5_start + tts5h2_s1 < s1_start:
            matrix[1][4] = 1
        if s5_start + tts5h3_s1 < s1_start:
            matrix[2][4] = 1
        if s5_start + tts5h4_s1 < s1_start:
            matrix[3][4] = 1
        if s5_start + tts5h5_s1 < s1_start:
            matrix[4][4] = 1
        if s5_start + tts5h6_s1 < s1_start:
            matrix[5][4] = 1
        if s5_start + tts5h7_s1 < s1_start:
            matrix[6][4] = 1
        if s5_start + tts5h8_s1 < s1_start:
            matrix[7][4] = 1
        if s5_start + tts5h9_s1 < s1_start:
            matrix[8][4] = 1
        if s5_start + tts5h10_s1 < s1_start:
            matrix[9][4] = 1
        if s5_start + tts5h11_s1 < s1_start:
            matrix[10][4] = 1
        if s5_start + tts5h12_s1 < s1_start:
            matrix[11][4] = 1
        if s5_start + tts5h13_s1 < s1_start:
            matrix[12][4] = 1
        if s5_start + tts5h14_s1 < s1_start:
            matrix[13][4] = 1
        if s5_start + tts5h15_s1 < s1_start:
            matrix[14][4] = 1
        if s5_start + tts5h16_s1 < s1_start:
            matrix[15][4] = 1
        if s5_start + tts5h17_s1 < s1_start:
            matrix[16][4] = 1
        if s5_start + tts5h1_s2 < s2_start:
            matrix[17][4] = 1
        if s5_start + tts5h2_s2 < s2_start:
            matrix[18][4] = 1
        if s5_start + tts5h3_s2 < s2_start:
            matrix[19][4] = 1
        if s5_start + tts5h4_s2 < s2_start:
            matrix[20][4] = 1
        if s5_start + tts5h1_s3 < s3_start:
            matrix[21][4] = 1
        if s5_start + tts5h2_s3 < s3_start:
            matrix[22][4] = 1
        if s5_start + tts5h3_s3 < s3_start:
            matrix[23][4] = 1
        if s5_start + tts5h4_s3 < s3_start:
            matrix[24][4] = 1
        if s5_start + tts5h5_s3 < s3_start:
            matrix[25][4] = 1
        if s5_start + tts5h6_s3 < s3_start:
            matrix[26][4] = 1
        if s5_start + tts5h7_s3 < s3_start:
            matrix[27][4] = 1
        if s5_start + tts5h8_s3 < s3_start:
            matrix[28][4] = 1
        if s5_start + tts5h9_s3 < s3_start:
            matrix[29][4] = 1
        if s5_start + tts5h10_s3 < s3_start:
            matrix[30][4] = 1
        if s5_start + tts5h11_s3 < s3_start:
            matrix[31][4] = 1
        if s5_start + tts5h12_s3 < s3_start:
            matrix[32][4] = 1
        if s5_start + tts5h13_s3 < s3_start:
            matrix[33][4] = 1
        if s5_start + tts5h14_s3 < s3_start:
            matrix[34][4] = 1
        if s5_start + tts5h15_s3 < s3_start:
            matrix[35][4] = 1
        if s5_start + tts5h1_s4 < s4_start:
            matrix[36][4] = 1
        if s5_start + tts5h1_s6 < s6_start:
            matrix[41][4] = 1
        if s5_start + tts5h2_s6 < s6_start:
            matrix[42][4] = 1
        if s5_start + tts5h1_s7 < s7_start:
            matrix[43][4] = 1
        if s5_start + tts5h2_s7 < s7_start:
            matrix[44][4] = 1
        if s5_start + tts5h3_s7 < s7_start:
            matrix[45][4] = 1

        if s6_start + tts6h1_s1 < s1_start:
            matrix[0][5] = 1
        if s6_start + tts6h2_s1 < s1_start:
            matrix[1][5] = 1
        if s6_start + tts6h3_s1 < s1_start:
            matrix[2][5] = 1
        if s6_start + tts6h4_s1 < s1_start:
            matrix[3][5] = 1
        if s6_start + tts6h5_s1 < s1_start:
            matrix[4][5] = 1
        if s6_start + tts6h6_s1 < s1_start:
            matrix[5][5] = 1
        if s6_start + tts6h7_s1 < s1_start:
            matrix[6][5] = 1
        if s6_start + tts6h8_s1 < s1_start:
            matrix[7][5] = 1
        if s6_start + tts6h9_s1 < s1_start:
            matrix[8][5] = 1
        if s6_start + tts6h10_s1 < s1_start:
            matrix[9][5] = 1
        if s6_start + tts6h11_s1 < s1_start:
            matrix[10][5] = 1
        if s6_start + tts6h12_s1 < s1_start:
            matrix[11][5] = 1
        if s6_start + tts6h13_s1 < s1_start:
            matrix[12][5] = 1
        if s6_start + tts6h14_s1 < s1_start:
            matrix[13][5] = 1
        if s6_start + tts6h15_s1 < s1_start:
            matrix[14][5] = 1
        if s6_start + tts6h16_s1 < s1_start:
            matrix[15][5] = 1
        if s6_start + tts6h17_s1 < s1_start:
            matrix[16][5] = 1
        if s6_start + tts6h1_s2 < s2_start:
            matrix[17][5] = 1
        if s6_start + tts6h2_s2 < s2_start:
            matrix[18][5] = 1
        if s6_start + tts6h3_s2 < s2_start:
            matrix[19][5] = 1
        if s6_start + tts6h4_s2 < s2_start:
            matrix[20][5] = 1
        if s6_start + tts6h1_s3 < s3_start:
            matrix[21][5] = 1
        if s6_start + tts6h2_s3 < s3_start:
            matrix[22][5] = 1
        if s6_start + tts6h3_s3 < s3_start:
            matrix[23][5] = 1
        if s6_start + tts6h4_s3 < s3_start:
            matrix[24][5] = 1
        if s6_start + tts6h5_s3 < s3_start:
            matrix[25][5] = 1
        if s6_start + tts6h6_s3 < s3_start:
            matrix[26][5] = 1
        if s6_start + tts6h7_s3 < s3_start:
            matrix[27][5] = 1
        if s6_start + tts6h8_s3 < s3_start:
            matrix[28][5] = 1
        if s6_start + tts6h9_s3 < s3_start:
            matrix[29][5] = 1
        if s6_start + tts6h10_s3 < s3_start:
            matrix[30][5] = 1
        if s6_start + tts6h11_s3 < s3_start:
            matrix[31][5] = 1
        if s6_start + tts6h12_s3 < s3_start:
            matrix[32][5] = 1
        if s6_start + tts6h13_s3 < s3_start:
            matrix[33][5] = 1
        if s6_start + tts6h14_s3 < s3_start:
            matrix[34][5] = 1
        if s6_start + tts6h15_s3 < s3_start:
            matrix[35][5] = 1
        if s6_start + tts6h1_s4 < s4_start:
            matrix[36][5] = 1
        if s6_start + tts6h1_s5 < s5_start:
            matrix[37][5] = 1
        if s6_start + tts6h2_s5 < s5_start:
            matrix[38][5] = 1
        if s6_start + tts6h3_s5 < s5_start:
            matrix[39][5] = 1
        if s6_start + tts6h4_s5 < s5_start:
            matrix[40][5] = 1
        if s6_start + tts6h1_s7 < s7_start:
            matrix[43][5] = 1
        if s6_start + tts6h2_s7 < s7_start:
            matrix[44][5] = 1
        if s6_start + tts6h3_s7 < s7_start:
            matrix[45][5] = 1

        if s7_start + tts7h2_s1 < s1_start:
            matrix[0][6] = 1
        if s7_start + tts7h2_s1 < s1_start:
            matrix[1][6] = 1
        if s7_start + tts7h3_s1 < s1_start:
            matrix[2][6] = 1
        if s7_start + tts7h4_s1 < s1_start:
            matrix[3][6] = 1
        if s7_start + tts7h5_s1 < s1_start:
            matrix[4][6] = 1
        if s7_start + tts7h6_s1 < s1_start:
            matrix[5][6] = 1
        if s7_start + tts7h7_s1 < s1_start:
            matrix[6][6] = 1
        if s7_start + tts7h8_s1 < s1_start:
            matrix[7][6] = 1
        if s7_start + tts7h9_s1 < s1_start:
            matrix[8][6] = 1
        if s7_start + tts7h10_s1 < s1_start:
            matrix[9][6] = 1
        if s7_start + tts7h11_s1 < s1_start:
            matrix[10][6] = 1
        if s7_start + tts7h12_s1 < s1_start:
            matrix[11][6] = 1
        if s7_start + tts7h13_s1 < s1_start:
            matrix[12][6] = 1
        if s7_start + tts7h14_s1 < s1_start:
            matrix[13][6] = 1
        if s7_start + tts7h15_s1 < s1_start:
            matrix[14][6] = 1
        if s7_start + tts7h16_s1 < s1_start:
            matrix[15][6] = 1
        if s7_start + tts7h17_s1 < s1_start:
            matrix[16][6] = 1
        if s7_start + tts7h1_s2 < s2_start:
            matrix[17][6] = 1
        if s7_start + tts7h2_s2 < s2_start:
            matrix[18][6] = 1
        if s7_start + tts7h3_s2 < s2_start:
            matrix[19][6] = 1
        if s7_start + tts7h4_s2 < s2_start:
            matrix[20][6] = 1
        if s7_start + tts7h1_s3 < s3_start:
            matrix[21][6] = 1
        if s7_start + tts7h2_s3 < s3_start:
            matrix[22][6] = 1
        if s7_start + tts7h3_s3 < s3_start:
            matrix[23][6] = 1
        if s7_start + tts7h4_s3 < s3_start:
            matrix[24][6] = 1
        if s7_start + tts7h5_s3 < s3_start:
            matrix[25][6] = 1
        if s7_start + tts7h6_s3 < s3_start:
            matrix[26][6] = 1
        if s7_start + tts7h7_s3 < s3_start:
            matrix[27][6] = 1
        if s7_start + tts7h8_s3 < s3_start:
            matrix[28][6] = 1
        if s7_start + tts7h9_s3 < s3_start:
            matrix[29][6] = 1
        if s7_start + tts7h10_s3 < s3_start:
            matrix[30][6] = 1
        if s7_start + tts7h11_s3 < s3_start:
            matrix[31][6] = 1
        if s7_start + tts7h12_s3 < s3_start:
            matrix[32][6] = 1
        if s7_start + tts7h13_s3 < s3_start:
            matrix[33][6] = 1
        if s7_start + tts7h14_s3 < s3_start:
            matrix[34][6] = 1
        if s7_start + tts7h15_s3 < s3_start:
            matrix[35][6] = 1
        if s7_start + tts7h1_s4 < s4_start:
            matrix[36][6] = 1
        if s7_start + tts7h1_s5 < s5_start:
            matrix[37][6] = 1
        if s7_start + tts7h2_s5 < s5_start:
            matrix[38][6] = 1
        if s7_start + tts7h3_s5 < s5_start:
            matrix[39][6] = 1
        if s7_start + tts7h4_s5 < s5_start:
            matrix[40][6] = 1
        if s7_start + tts7h1_s6 < s6_start:
            matrix[41][6] = 1
        if s7_start + tts7h2_s6 < s6_start:
            matrix[42][6] = 1

    # Print the result for the current combination
    print(f"Combination: {combination}, Result: {matrix}")
    matrizen.append(matrix)
    schoolstart_combination.append(combination)
n_reuses=[]

for matrix in matrizen:
    max_anfahrten = [0, 0, 0, 0, 0, 0, 0]
    n_ava_unverbraucht = [17, 4, 15, 1, 4, 2, 3]
    n_ava = [17, 4, 15, 1, 4, 2, 3]
    n_anfahrten = [17, 4, 15, 1, 4, 2, 3]
    n_reuse = 0
    n_reuse_einzel = matrizenbearbeitung(matrix, n_ava, n_ava_unverbraucht, n_reuse,max_anfahrten, n_anfahrten)
    n_reuses.append(n_reuse_einzel)


print(n_reuses)



#print(n_reuses)
max_reuses = max(n_reuses)
indices_of_highest_value = [i for i, x in enumerate(n_reuses) if x == max_reuses]
print(indices_of_highest_value)
indices_of_second_highest_value = [i for i, x in enumerate(n_reuses) if x == max_reuses-1]
indices_of_third_highest_value = [i for i, x in enumerate(n_reuses) if x == max_reuses-2]
indices_of_fourth_highest_value = [i for i, x in enumerate(n_reuses) if x == max_reuses-3]
indices_of_fivest_highest_value = [i for i, x in enumerate(n_reuses) if x == max_reuses-4]





gesuchte_kombination = (10, 10, 0, 20, 10, 30,10) # hier wird die aktuelle Schulstartkombination eingegbenen 0=7:10 (Achtung WIsentalschule)
positionen = []
for i, kombination in enumerate(schoolstart_combination):
    if kombination == gesuchte_kombination:
        positionen.append(i)
print(positionen)
#busses_needed_now=busses_needed_without- n_reuses[positionen[0]]


# Ergbnistext
print ("-------------------------------------------------------------")
print ("Das sind die Ergbnisse")
print("Ohne Staffelung von Unterrichtszeiten werden " + str(busses_needed_without)+" Busse benötigt")
print("Mit der aktuellen Kombination an Schulzeiten werden "+str(busses_needed_now)+" Busse benötigt")
print(f"Die maximal einzusparende Busanzahl beträgt {max_reuses}")
print("Das wird bei folgenden Schulbeginnzeiten erreicht")

for q in indices_of_highest_value:
    print(schoolstart_combination[q])

busses_needed_with = busses_needed_without-max_reuses
print("Dann werden nur noch " + str (busses_needed_with)+" Busse benötigt")
print(len(indices_of_highest_value))









