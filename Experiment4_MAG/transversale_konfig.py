import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#uncertainties
u_l_g = 0.1 #cm
u_l_p = 0.0025

u_B = 0.01 #prozent

print("------------load data------------")
data = an.read_csv_file("Experiment4_1A_ohne_t.csv")
data = data[1:]
print(data)

print("------------prepare data------------")
data_Feld = []
error_y_1_Feld = []
error_x_1_Feld = []
for set in data:
    data_Feld.append((set[1], set[3]))
    error_y_1_Feld.append(abs(set[3])*u_B)
    error_x_1_Feld.append(u_l_p*abs(set[1])+ u_l_g)
    #mirror the data
    data_Feld.append((-set[1], set[3]))
    error_y_1_Feld.append(abs(set[3]) * u_B)
    error_x_1_Feld.append(u_l_p* abs(set[1]) + u_l_g)
print(data_Feld)

data_grund = []
error_y_1_grund = []
error_x_1_grund = []
for set in data:
    data_grund.append((set[1], set[2]))
    error_y_1_grund.append(abs(set[2])*u_B)
    error_x_1_grund.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_grund.append((-set[1], set[2]))
    error_y_1_grund.append(abs(set[2]) * u_B)
    error_x_1_grund.append(u_l_p * abs(set[1]) + u_l_g)

data_gesamt = []
error_y_1_gesamt = []
error_x_1_gesamt = []
for set in data:
    data_gesamt.append((set[1], set[3]-set[2]))
    error_y_1_gesamt.append(abs(set[3]-set[2])*u_B)
    error_x_1_gesamt.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_gesamt.append((-set[1], set[3]-set[2]))
    error_y_1_gesamt.append(abs(set[3]-set[2]) * u_B)
    error_x_1_gesamt.append(u_l_p * abs(set[1]) + u_l_g)


print("------------plot the data------------")
ax, fig = plt.subplots(figsize=(8, 8))
plt.errorbar([x[0] for x in data_Feld], [x[1] for x in data_Feld], yerr=error_y_1_Feld, xerr=error_x_1_Feld, fmt='o', label="Feldstärke")
plt.errorbar([x[0] for x in data_grund], [x[1] for x in data_grund], yerr=error_y_1_grund, xerr=error_x_1_grund, fmt='o', label="Untergrundmessung")
plt.errorbar([x[0] for x in data_gesamt], [x[1] for x in data_gesamt], yerr=error_y_1_gesamt, xerr=error_x_1_gesamt, fmt='o', label="Gesamtfeld")

plt.legend()
plt.grid()
plt.yscale("linear")
plt.xlabel("Abstand [cm]")
plt.ylabel("Magnetfeldstärke [mT]")
plt.savefig("../Graphics/Experiment4_1A_ohne_t.pdf")
plt.show()
