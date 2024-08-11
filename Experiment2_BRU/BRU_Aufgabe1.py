import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
print("--------------BRU Experiment 1--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("BRU-Experiment1.csv")
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

print("------------Calculate the weighted mean------------")
# Calculate the weighted mean
sum_resistance = 0
sum_weight = 0
for set in data_resistance:
    sum_resistance += set[2]/set[3]**2
    sum_weight += 1/set[3]**2
mean_resistance = sum_resistance/sum_weight
u_mean_resistance = 1/np.sqrt(sum_weight)
print(f"Mean resistance: {mean_resistance} +- {u_mean_resistance}")