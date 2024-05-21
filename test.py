import itertools
s1_start = [0,10,20]
s2_start = [0,10,20]
s3_start = [-10,0,10]
s4_start = [10,20,30]
s5_start = [0,10,20]
s6_start = [20,30,40]
s7_start = [0,10,20]
# Generate all possible combinations of values for the four variables

combinations = itertools.product(s1_start, s2_start, s3_start, s4_start, s5_start, s6_start, s7_start)
matrizen = []
schoolstart_combination = []

for combination in combinations:
    min_val = min(combination)
    max_val = max(combination)
    if max_val - min_val <= 40:
        print(combination)