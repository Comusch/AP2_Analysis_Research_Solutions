import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
print("--------------BRU Experiment 4--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("BRU-Experiment_Induktivitaet.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

data_orignal2 = an.read_csv_file("BRU-Experiment_Induktivitaet2.csv")
data_orignal2 = data_orignal2[1:]
print(data_orignal2)

print("-----------Initial the constants-----------")
u_L = 0.1 #mH
u_A = 0.01  # absolute uncertainty of the relationship of the resistance

print("-----------Calculate the inductance of the first coil-----------")
data_inductance = []
for set in data_orignal:
    inductance = set[1]/(10-set[1])*set[0]
    u_inductance = np.sqrt((u_L*set[1]/(10-set[1]))**2 + (set[0]*10/(10-set[1])**2*u_A)**2)
    data_inductance.append((set[0], set[1], inductance, u_inductance))
    print(f"L: {inductance} +- {u_inductance}, with R: {set[0]} and A: {set[1]}")
    print("---------------")

l1 = data_inductance[0][2]
u_l1 = data_inductance[0][3]

print("-----------Calculate the inductance of the half coil-----------")
data_inductance2 = []
for set in data_orignal2:
    inductance = set[1]/(10-set[1])*l1
    u_inductance = np.sqrt((u_l1*set[1]/(10-set[1]))**2 + (set[0]*10/(10-set[1])**2*u_A)**2)
    data_inductance2.append((set[0], set[1], inductance, u_inductance))
    print(f"L: {inductance} +- {u_inductance}, with R: {set[0]} and A: {set[1]}")
    print(f"Relation of the inductance: {inductance/data_orignal[0][0]}")
    print("---------------")
