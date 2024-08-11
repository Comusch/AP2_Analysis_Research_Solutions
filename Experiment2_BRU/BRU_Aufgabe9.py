import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
def Aufgabe2_start():
    print("--------------BRU Experiment 3--------------")
    print("-----------Data loading-----------")
    data_orignal = an.read_csv_file("BRU-Experiment_lambe1.csv")
    data_orignal = data_orignal[1:]
    print(data_orignal)

    print("-----------Initial the constants-----------")
    u_R = 0.01  # Procentual uncertainty of the resistance
    u_A = 0.01  # absolute uncertainty of the relationship of the resistance

    U = 1  # Voltage
    u_U = 0.01  # absolute uncertainty of the voltage

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

    print("------------Calculate the amperage of the strom circuit------------")
    # Calculate the amperage of the strom circuit
    data_amperage = []
    data_power_of_resistance = []
    for set in data_resistance:
        R_ges = set[2] + set[0]
        u_R_ges = np.sqrt(set[3]**2 + (0.01*set[0])**2)
        amperage = U/R_ges
        u_amperage = np.sqrt((u_U/R_ges)**2 + (U*u_R_ges/R_ges**2)**2)
        data_amperage.append((set[0], set[1], R_ges, u_R_ges, amperage, u_amperage))
        print(f"I: {amperage} +- {u_amperage}, with R: {set[0]} and A: {set[1]}")
        print("-----")
        U2 = U/(set[0]/set[2] + 1)
        u_U2 = np.sqrt((u_U/(set[0]/set[2] + 1))**2 + (U*set[3]/set[2]**2)**2)
        P = U2*amperage
        u_P = np.sqrt((u_U2*amperage)**2 + (U2*u_amperage)**2)
        data_power_of_resistance.append((set[0], set[1], set[2], set[3], amperage, u_amperage, U2, u_U2, P, u_P))
        print(f"P: {P} +- {u_P}, with R: {set[0]} and A: {set[1]}")
        print("---------------")
    print(data_amperage)
    print(data_power_of_resistance)
    return data_power_of_resistance

data_power_of_resistance = Aufgabe2_start()


