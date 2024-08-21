import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


mu_0 = 4*np.pi*10**(-7) #N/A^2

#fit function
def Bx(I, R, mu_r, x):
    x *= 10**(-2) #cm to m
    R *= 10**(-2) #cm to m
    mu_0 = 4*np.pi*10**(-7) #N/A^2
    N = 1200
    return mu_r*N *mu_0/(4*np.pi) * I * R**2 *2*np.pi/ (R**2 + x**2)**(3/2) * 10**3 #mT

#uncertainties
u_l_g = 0.1 #cm
u_l_p = 0.0025

u_B = 0.01 #prozent

#load data
print("------------load data------------")
data = an.read_csv_file("Experiment4_1A_mit_l.csv")
data = data[1:]
print(data)

print("------------prepare data------------")
for i in range(len(data)):
    data[i][1] -= 0.5

data_1_Feld = []
error_y_1_Feld = []
error_x_1_Feld = []
for set in data:
    data_1_Feld.append((set[1], set[3]))
    error_y_1_Feld.append(abs(set[3])*u_B)
    error_x_1_Feld.append(u_l_p*abs(set[1])+ u_l_g)
    #mirror the data
    data_1_Feld.append((-set[1], set[3]))
    error_y_1_Feld.append(abs(set[3]) * u_B)
    error_x_1_Feld.append(u_l_p * abs(set[1]) + u_l_g)
print(data_1_Feld)

data_1_grund = []
error_y_1_grund = []
error_x_1_grund = []
for set in data:
    data_1_grund.append((set[1], set[2]))
    error_y_1_grund.append(abs(set[2])*u_B)
    error_x_1_grund.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_1_grund.append((-set[1], set[2]))
    error_y_1_grund.append(abs(set[2]) * u_B)
    error_x_1_grund.append(u_l_p * abs(set[1]) + u_l_g)
print(data_1_grund)

data_1_gesamt = []
error_y_1_gesamt = []
error_x_1_gesamt = []
for set in data:
    data_1_gesamt.append((set[1], set[3]-set[2]))
    error_y_1_gesamt.append(abs(set[3]-set[2])*u_B)
    error_x_1_gesamt.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_1_gesamt.append((-set[1], set[3]-set[2]))
    error_y_1_gesamt.append(abs(set[3]-set[2]) * u_B)
    error_x_1_gesamt.append(u_l_p * abs(set[1]) + u_l_g)
print(data_1_gesamt)

grenze_spule = 4.35-0.5
print(f"Grenze Spule: {grenze_spule}")

print("-----------fit the data-----------")
#fit the data
x_fit_data_r = np.linspace(-40, 40, 200)

#fit the data
popt, pcov = curve_fit(Bx, [x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], p0=[0.8, 3.7, 2.5])
print(popt)
I_eff = popt[0]
R_eff = popt[1]
mu_r = popt[2]
print(f"I_eff: {I_eff}, R_eff: {R_eff}, mu_r: {mu_r}")
I_eff = 0.85
R_eff = 3.75
mu_r = 3.4
print(f"I_eff: {I_eff}, R_eff: {R_eff}, mu_r: {mu_r}")

B1_max = Bx(I_eff, R_eff, mu_r, 1.0037)

x_fit_data = []
for set in x_fit_data_r:
    if set < -3.7 or set > 3.7:
        x_fit_data.append(set)

y_fit_data = [Bx(I_eff, R_eff, mu_r, x) for x in x_fit_data]

#data_grenzen1 = [(-1.0037, B1_max), (1.0037, B1_max)]

print("-----------Calculation of B1_max and M-----------")

print(f"B1_max: {B1_max} mT")
x_m = mu_r - 1
M = B1_max *10**(-3)/ (mu_0 * mu_r) * x_m
print(f"M_max: {M} A/m")

print("------------plot data------------")

fig, ax = plt.subplots(figsize=(8, 8))
plt.axvline(x=-3.7, color="red")
plt.axvline(x=3.7, color="red")
#plt.plot([x[0] for x in data_grenzen1], [x[1] for x in data_grenzen1],"-", color="red", label="Maximumsplatto")
plt.errorbar([x[0] for x in data_1_Feld], [x[1] for x in data_1_Feld], yerr=error_y_1_Feld, xerr=error_x_1_Feld, fmt='o', label="Magnetfeld")
plt.errorbar([x[0] for x in data_1_grund], [x[1] for x in data_1_grund],yerr=error_y_1_grund, xerr=error_x_1_grund, fmt= 'o', label="Untergrundmessung")
plt.errorbar([x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], yerr=error_y_1_gesamt, xerr=error_x_1_grund, fmt='o', label="Gesamtfeld")
plt.plot(x_fit_data, y_fit_data, label="Fit")

plt.legend()
plt.grid()
plt.yscale("linear")
plt.xlabel("Abstand [cm]")
plt.ylabel("Magnetfeldstärke [mT]")
plt.savefig("../Graphics/Experiment4_1A_mit_l.pdf")
plt.show()

print("------------done------------")

print("---------------same with the second data set---------------")
data2 = an.read_csv_file("Experiment4_1.5_mit_l.csv")
data2 = data2[1:]
print(data2)

print("------------prepare data------------")
for i in range(len(data2)):
    data2[i][1] -= 0.5

data_2_Feld = []
error_y_2_Feld = []
error_x_2_Feld = []
for set in data2:
    data_2_Feld.append((set[1], set[3]))
    error_y_2_Feld.append(abs(set[3])*u_B)
    error_x_2_Feld.append(u_l_p*abs(set[1])+ u_l_g)
    #mirror the data
    data_2_Feld.append((-set[1], set[3]))
    error_y_2_Feld.append(abs(set[3]) * u_B)
    error_x_2_Feld.append(u_l_p * abs(set[1]) + u_l_g)
print(data_2_Feld)

data_2_grund = []
error_y_2_grund = []
error_x_2_grund = []
for set in data2:
    data_2_grund.append((set[1], set[2]))
    error_y_2_grund.append(abs(set[2])*u_B)
    error_x_2_grund.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_2_grund.append((-set[1], set[2]))
    error_y_2_grund.append(abs(set[2]) * u_B)
    error_x_2_grund.append(u_l_p * abs(set[1]) + u_l_g)
print(data_2_grund)

data_2_gesamt = []
error_y_2_gesamt = []
error_x_2_gesamt = []
for set in data2:
    data_2_gesamt.append((set[1], set[3]-set[2]))
    error_y_2_gesamt.append(abs(set[3]-set[2])*u_B)
    error_x_2_gesamt.append(u_l_p * abs(set[1]) + u_l_g)
    #mirror the data
    data_2_gesamt.append((-set[1], set[3]-set[2]))
    error_y_2_gesamt.append(abs(set[3]-set[2]) * u_B)
    error_x_2_gesamt.append(u_l_p * abs(set[1]) + u_l_g)
print(data_2_gesamt)

print("-----------fit the data-----------")
#fit the data
x_fit_data2_r = np.linspace(-40, 40, 400)

#fit the data
fit = curve_fit(Bx, [x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], p0=[0.8, 3.7, 2.5])
popt = fit[0]
print(popt)
I_eff2 = popt[0]
R_eff2 = popt[1]
mu_r2 = popt[2]
print(f"I_eff: {I_eff2}, R_eff: {R_eff2}, mu_r: {mu_r2}")
I_eff2 = 1.26
R_eff2 = 3.89
mu_r2 = 3.05
print(f"I_eff: {I_eff2}, R_eff: {R_eff2}, mu_r: {mu_r2}")

x_fit_data2 = []
for set in x_fit_data2_r:
    if set < -3.5 or set > 3.5:
        x_fit_data2.append(set)
    else:
        print(set)

y_fit_data2 = [Bx(I_eff2, R_eff2, mu_r2, x) for x in x_fit_data2]

B2_max = Bx(I_eff2, R_eff2, mu_r2, 0.9)

#data_grenzen2 = [(-4.35, B2_max), (4.35, B2_max)]

print("-----------Calculation of B2_max and M-----------")

print(f"B2_max: {B2_max} mT")

x_m2 = mu_r2 - 1
M2 = B2_max *10**(-3)/ (mu_0 * mu_r2) * x_m2
print(f"M_max: {M2} A/m")

print("------------plot data------------")

fig, ax = plt.subplots(figsize=(8, 8))

plt.axvline(x=-3.5, color="red")
plt.axvline(x=3.5, color="red")
#plt.plot([x[0] for x in data_grenzen2], [x[1] for x in data_grenzen2], color="red", label="Maximumsplatto")
plt.errorbar([x[0] for x in data_2_Feld], [x[1] for x in data_2_Feld], yerr=error_y_2_Feld, xerr=error_x_2_Feld, fmt='o', label="Magnetfeld")
plt.errorbar([x[0] for x in data_2_grund], [x[1] for x in data_2_grund], yerr=error_y_2_grund, xerr=error_x_2_Feld, fmt='o', label="Untergrundmessung")
plt.errorbar([x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], yerr=error_y_2_gesamt, xerr=error_x_2_gesamt, fmt='o', label="Gesamtfeld")
plt.plot(x_fit_data2, y_fit_data2, label="Fit")

plt.legend()
plt.grid()
plt.yscale("linear")
plt.xlabel("Abstand [cm]")
plt.ylabel("Magnetfeldstärke [mT]")
plt.savefig("../Graphics/Experiment4_1.5A_mit_l.pdf")
plt.show()

print("------------done------------")



