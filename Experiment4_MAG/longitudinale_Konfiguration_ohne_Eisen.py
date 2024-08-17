import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#fit function
def Bx(I, R, x):
    x *= 10**(-2) #cm to m
    R *= 10**(-2) #cm to m
    mu_0 = 4*np.pi*10**(-7) #N/A^2
    N = 1200
    return N *mu_0/(4*np.pi) * I * R**2 *2*np.pi/ (R**2 + x**2)**(3/2) * 10**3 #mT

#load data
print("------------load data------------")
data = an.read_csv_file("Experiment4_1A_ohne_l.csv")
data = data[1:]
print(data)

print("------------prepare data------------")
for i in range(len(data)):
    data[i][1] -= 0.5

data_1_Feld = []
for set in data:
    data_1_Feld.append((set[1], set[3]))
    #mirror the data
    data_1_Feld.append((-set[1], set[3]))
print(data_1_Feld)

data_1_grund = []
for set in data:
    data_1_grund.append((set[1], set[2]))
    #mirror the data
    data_1_grund.append((-set[1], set[2]))
print(data_1_grund)

data_1_gesamt = []
for set in data:
    data_1_gesamt.append((set[1], set[3]-set[2]))
    #mirror the data
    data_1_gesamt.append((-set[1], set[3]-set[2]))
print(data_1_gesamt)

grenze_spule = 4.35-0.5
print(f"Grenze Spule: {grenze_spule}")

print("-----------fit the data-----------")
#fit the data
x_fit_data = np.linspace(-40, 40, 200)

#fit the data
popt, pcov = curve_fit(Bx, [x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], p0=[0.8, 3.7])
print(popt)
I_eff = popt[0]
R_eff = popt[1]
I_eff = 0.78
R_eff = 3.74
print(f"I_eff: {I_eff}, R_eff: {R_eff}")

y_fit_data = [Bx(I_eff, R_eff, x) for x in x_fit_data]

print("------------plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot([x[0] for x in data_1_Feld], [x[1] for x in data_1_Feld], 'o', label="Magnetfeld")
plt.plot([x[0] for x in data_1_grund], [x[1] for x in data_1_grund], 'o', label="Untergrundmessung")
plt.plot([x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], 'o', label="Gesamtfeld")
plt.plot(x_fit_data, y_fit_data, label="Fit")
ax.set_xlabel("Abstand in cm")
ax.set_ylabel("Magnetfeldstärke in mT")
ax.legend()
ax.grid('minor')
fig.savefig("../Graphics/Experiment4_1A_ohne_l.pdf")
fig.show()
print("------------done------------")

print("--------------Same for 1.5A--------------")
#load data
print("------------load data------------")
data2 = an.read_csv_file("Experiment4_1.5A_ohne_l.csv")
data2 = data2[1:]
print(data2)

print("------------prepare data------------")
for i in range(len(data2)):
    data2[i][1] -= 0.5

data_2_Feld = []
for set in data2:
    data_2_Feld.append((set[1], set[3]))
    #mirror the data
    data_2_Feld.append((-set[1], set[3]))
print(data_2_Feld)

data_2_grund = []
for set in data2:
    data_2_grund.append((set[1], set[2]))
    #mirror the data
    data_2_grund.append((-set[1], set[2]))
print(data_2_grund)

data_2_gesamt = []
for set in data2:
    data_2_gesamt.append((set[1], set[3]-set[2]))
    #mirror the data
    data_2_gesamt.append((-set[1], set[3]-set[2]))
print(data_2_gesamt)

grenze_spule = 4.35-0.5
print(f"Grenze Spule: {grenze_spule}")

print("-----------fit the data-----------")
#fit the data
x_fit_data2 = np.linspace(-40, 40, 200)

#fit the data
popt, pcov = curve_fit(Bx, [x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], p0=[0.8, 3.7])
print(popt)
I_eff = popt[0]
R_eff = popt[1]
I_eff = 1.26
R_eff = 3.89
print(f"I_eff: {I_eff}, R_eff: {R_eff}")

y_fit_data2 = [Bx(I_eff, R_eff, x) for x in x_fit_data2]

print("------------plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot([x[0] for x in data_2_Feld], [x[1] for x in data_2_Feld], 'o', label="Magnetfeld")
plt.plot([x[0] for x in data_2_grund], [x[1] for x in data_2_grund], 'o', label="Untergrundmessung")
plt.plot([x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], 'o', label="Gesamtfeld")
plt.plot(x_fit_data2, y_fit_data2, label="Fit")
ax.set_xlabel("Abstand in cm")
ax.set_ylabel("Magnetfeldstärke in mT")
ax.legend()
ax.grid('minor')
fig.savefig("../Graphics/Experiment4_1.5A_ohne_l.pdf")
fig.show()



