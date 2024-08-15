import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import BRU_Aufgabe9 as a9
from scipy.stats import linregress

# Load the data
print("--------------BRU Experiment 4--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("BRU-Experiment_lambe2.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

print("-----------Initial the constants-----------")
u_R = 0.01  # Procentual uncertainty of the resistance
u_A = 0.01  # absolute uncertainty of the relationship of the resistance

u_U = 0.01  # absolute uncertainty of the voltage

# Sort the data by the resistance
print("-----------Sort the data by the resistance-----------")
#R = 200 instead of 50, but the name is still r50
data_r10 = []
data_r30 = []
data_r50 = []

for set in data_orignal:
    if set[1] == 10:
        data_r10.append(set)
    elif set[1] == 30:
        data_r30.append(set)
    elif set[1] == 200:
        data_r50.append(set)
    else:
        print("Error")
print(data_r10)
print(data_r30)
print(data_r50)

# Calculate the resistance
print("-----------Calculate the resistance-----------")
data_r10_resistance = []
data_r30_resistance = []
data_r50_resistance = []
data_resistance_power_r10 = []
data_resistance_power_r30 = []
data_resistance_power_r50 = []

for set in data_r10:
    print(f"R:{set[1]}, U: {set[0]}, A: {set[2]}")
    resistance = set[2]/(10-set[2])*set[1]
    u_resistance = np.sqrt((u_R*set[1]*set[2]/(10-set[2]))**2 + (set[1]*10/(10-set[2])**2*u_A)**2)
    data_r10_resistance.append((set[0], set[1], resistance, u_resistance))
    print(f"R: {resistance} +- {u_resistance}, with R: {set[0]} and A: {set[1]}")
    print("----")
    R_ges = resistance + set[1]
    u_R_ges = np.sqrt(u_resistance**2 + (0.01*set[1])**2)
    amperage = set[0]/R_ges
    u_amperage = np.sqrt((u_U/R_ges)**2 + (set[0]*u_R_ges/R_ges**2)**2)
    print(f"I: {amperage} +- {u_amperage}, with R: {set[1]} and A: {set[2]}")
    power = set[0]*amperage
    u_power = np.sqrt((u_U*amperage)**2 + (set[0]*u_amperage)**2)
    print(f"P: {power} +- {u_power}")
    data_resistance_power_r10.append((resistance, u_resistance, amperage, u_amperage, power, u_power))
    print("---------------")

for set in data_r30:
    print(f"R:{set[1]}, U: {set[0]}, A: {set[2]}")
    resistance = set[2]/(10-set[2])*set[1]
    u_resistance = np.sqrt((u_R*set[1]*set[2]/(10-set[2]))**2 + (set[1]*10/(10-set[2])**2*u_A)**2)
    data_r30_resistance.append((set[0], set[1], resistance, u_resistance))
    print(f"R: {resistance} +- {u_resistance}, with R: {set[0]} and A: {set[1]}")
    print("----")
    R_ges = resistance + set[1]
    u_R_ges = np.sqrt(u_resistance**2 + (0.01*set[1])**2)
    amperage = set[0]/R_ges
    u_amperage = np.sqrt((u_U/R_ges)**2 + (set[0]*u_R_ges/R_ges**2)**2)
    print(f"I: {amperage} +- {u_amperage}, with R: {set[1]} and A: {set[2]}")
    power = set[0]*amperage
    u_power = np.sqrt((u_U*amperage)**2 + (set[0]*u_amperage)**2)
    print(f"P: {power} +- {u_power}")
    data_resistance_power_r30.append((resistance, u_resistance, amperage, u_amperage, power, u_power))
    print("---------------")

for set in data_r50:
    print(f"R:{set[1]}, U: {set[0]}, A: {set[2]}")
    resistance = set[2]/(10-set[2])*set[1]
    u_resistance = np.sqrt((u_R*set[1]*set[2]/(10-set[2]))**2 + (set[1]*10/(10-set[2])**2*u_A)**2)
    data_r50_resistance.append((set[0], set[1], resistance, u_resistance))
    print(f"R: {resistance} +- {u_resistance}, with R: {set[0]} and A: {set[1]}")
    print("----")
    R_ges = resistance + set[1]
    u_R_ges = np.sqrt(u_resistance**2 + (0.01*set[1])**2)
    amperage = set[0]/R_ges
    u_amperage = np.sqrt((u_U/R_ges)**2 + (set[0]*u_R_ges/R_ges**2)**2)
    print(f"I: {amperage} +- {u_amperage}, with R: {set[1]} and A: {set[2]}")
    power = set[0]*amperage
    u_power = np.sqrt((u_U*amperage)**2 + (set[0]*u_amperage)**2)
    print(f"P: {power} +- {u_power}")
    data_resistance_power_r50.append((resistance, u_resistance, amperage, u_amperage, power, u_power))
    print("---------------")

print(data_r10_resistance)
print(data_r30_resistance)
print(data_r50_resistance)
print(data_resistance_power_r10)
print(data_resistance_power_r30)
print(data_resistance_power_r50)

print("-----------Plott the I-R diagram-----------")
# Plott the I-R diagram
I_R = []
P_R = []
for set in data_resistance_power_r10:
    I_R.append((set[0], set[2]))
    P_R.append((set[0], set[4]))

for set in data_resistance_power_r30:
    I_R.append((set[0], set[2]))
    P_R.append((set[0], set[4]))

for set in data_resistance_power_r50:
    I_R.append((set[0], set[2]))
    P_R.append((set[0], set[4]))

data_resistance_power_aufgabe2 = a9.Aufgabe2_start()
for set in data_resistance_power_aufgabe2:
    I_R.append((set[2], set[4]))
    P_R.append((set[2], set[8]))

x = np.array(I_R)[:,0]
y = np.array(I_R)[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"R: {slope} +- {std_err}")
R_plot = np.linspace(0, 18, 100)
data_fit_I_R = []
for r in R_plot:
    data_fit_I_R.append((r, slope*r+intercept))

x2 = np.array(P_R)[:,0]
y2 = np.array(P_R)[:, 1]

slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)
print(f"P: {slope2} +- {std_err2}")
P_plot = np.linspace(0, 18, 100)
data_fit_P_R = []
for r in P_plot:
    data_fit_P_R.append((r, slope2*r+intercept2))

an.plot_data(I_R, data2= data_fit_I_R,file_name="I-R diagram", lable_x="R [Ohm]", lable_y="I [A]", plot_fit=False)
an.plot_data(P_R, data2=data_fit_P_R, file_name="P-R diagram", lable_x="R [Ohm]", lable_y="P [W]", plot_fit=False, scale_y="log", scale_x="log")



