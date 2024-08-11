import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
print("--------------BRU Experiment 2--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("BRU_Experiment_Aufgabe2.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

print("-----------Initial the constants-----------")
u_R = 0.01  # Procentual uncertainty of the resistance
u_A = 0.01  # absolute uncertainty of the relationship of the resistance

# Calculate the resistance
print("-----------Calculate the resistance-----------")
data_resistance = []
for set in data_orignal:
    resistance = set[1]/(10-set[1])*set[0]
    u_resistance = np.sqrt((u_R*set[0]*set[1]/(10-set[1]))**2 + (set[0]*10/(10-set[1])**2*u_A)**2)
    data_resistance.append((set[0], set[1], resistance, u_resistance))
    print(f"R: {resistance} +- {u_resistance}, with R: {set[0]} and A: {set[1]}")
    print("---------------")
print(data_resistance)

print("------------Compare the resistance of the diffrent sink---------------")
# Compare the resistance of the diffrent sink
print(f"Resistance of the first sink: {data_resistance[0][2]} +- {data_resistance[0][3]}")
print(f"Resistance of the second sink: {data_resistance[1][2]} +- {data_resistance[1][3]}")
print(f"Resistance of the third sink: {data_resistance[2][2]} +- {data_resistance[2][3]}")
print(f"Resistance of the fourth sink: {data_resistance[3][2]} +- {data_resistance[3][3]}")

print("---------")

print(f"Relationship between the second and the third sink: {data_resistance[1][2]/data_resistance[2][2]} +- {np.sqrt((data_resistance[1][3]/data_resistance[1][2])**2 + (data_resistance[2][3]/data_resistance[2][2])**2)}")
print(f"Relationship between the second and the fourth sink: {data_resistance[1][2]/data_resistance[3][2]} +- {np.sqrt((data_resistance[1][3]/data_resistance[1][2])**2 + (data_resistance[3][3]/data_resistance[3][2])**2)}")

