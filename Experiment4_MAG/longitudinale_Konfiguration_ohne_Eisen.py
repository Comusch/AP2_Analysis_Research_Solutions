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

def x_from_Bx(I, R, B):
    R *= 10**(-2) #cm to m
    mu_0 = 4*np.pi*10**(-7) #N/A^2
    N = 1200
    print("B: ", B)
    print(f"R: {R}, I: {I}")
    print((N *mu_0*R**2 *2*np.pi/(4*np.pi*B*10**(-3)) * I)**(2/3) - R**2)
    return np.sqrt((N *mu_0*R**2 *2*np.pi/(4*np.pi*B*10**(-3)) * I)**(2/3) - R**2)*10**2

#uncertainties
u_l_g = 0.1 #cm
u_l_p = 0.0025

u_B = 0.01 #prozent


#load data
print("------------load data------------")
data = an.read_csv_file("Experiment4_1A_ohne_l.csv")
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
popt, pcov = curve_fit(Bx, [x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], p0=[0.8, 3.7])
print(popt)
I_eff = popt[0]
R_eff = popt[1]
I_eff = 0.85
R_eff = 3.75
print(f"I_eff: {I_eff}, R_eff: {R_eff}")

print(f"B_max: {Bx(I_eff, R_eff, 0)}")

x_max_negativ = -x_from_Bx(I_eff, R_eff, (15.47-0.0645))
x_max_positiv = x_from_Bx(I_eff, R_eff, (15.47-0.060))

#data_grenzen = [(x_max_negativ, 0), (x_max_positiv, 0)]

print(f"x_max_negativ: {x_max_negativ}")
print(f"x_max_positiv: {x_max_positiv}")

x_fit_data = []
for set in x_fit_data_r:
    if set < -3.7 or set > 3.7:
        x_fit_data.append(set)

y_fit_data = [Bx(I_eff, R_eff, x) for x in x_fit_data]

print("------------plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.axvline(-3.7, color="red")
plt.axvline(3.7, color="red")
#plt.plot([x[0] for x in data_grenzen], [x[1] for x in data_grenzen], 'o', color="red", label="Grenzen des konst. Maximums")
plt.errorbar([x[0] for x in data_1_Feld], [x[1] for x in data_1_Feld], yerr= error_y_1_Feld, xerr=error_x_1_Feld, fmt='o', label="Magnetfeld")
plt.errorbar([x[0] for x in data_1_grund], [x[1] for x in data_1_grund], yerr= error_y_1_grund, xerr=error_x_1_grund, fmt='o', label="Untergrundmessung")
plt.errorbar([x[0] for x in data_1_gesamt], [x[1] for x in data_1_gesamt], yerr=error_y_1_gesamt, xerr= error_x_1_gesamt,fmt='o', label="Gesamtfeld")


plt.plot(x_fit_data, y_fit_data, label="Fit")
ax.set_xlabel("Abstand in cm")
ax.set_ylabel("Magnetfeldstärke in mT")
ax.legend()
ax.grid('minor')
fig.savefig("../Graphics/Experiment4_1A_ohne_l_genze.pdf")
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
error_y_2_Feld = []
error_x_2_Feld = []
for set in data2:
    data_2_Feld.append((set[1], set[3]))
    error_y_2_Feld.append(abs(set[3])*u_B)
    error_x_2_Feld.append(u_l_p * abs(set[1]) + u_l_g)
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

grenze_spule = 4.35-0.5
print(f"Grenze Spule: {grenze_spule}")

print("-----------fit the data-----------")
#fit the data
x_fit_data2_r = np.linspace(-40, 40, 200)

#fit the data
popt, pcov = curve_fit(Bx, [x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], p0=[0.8, 3.7])
print(popt)
I_eff = popt[0]
R_eff = popt[1]
I_eff = 1.26
R_eff = 3.89
print(f"I_eff: {I_eff}, R_eff: {R_eff}")



print(f"B_max: {Bx(I_eff, R_eff, 0)}")

x_max_negativ2 = -x_from_Bx(I_eff, R_eff, (23.57))
x_max_positiv2 = x_from_Bx(I_eff, R_eff, (23.57))

#data_grenzen2 = [(x_max_negativ, 0), (x_max_positiv, 0)]

print(f"x_max_negativ: {x_max_negativ2}")
print(f"x_max_positiv: {x_max_positiv2}")

x_fit_data2 = []
for set in x_fit_data2_r:
    if set < -3.5 or set > 3.5:
        x_fit_data2.append(set)

y_fit_data2 = [Bx(I_eff, R_eff, x) for x in x_fit_data2]

print("------------plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))
plt.axvline(x=-3.5, color="red")
plt.axvline(x=3.5, color="red")
#plt.plot([x[0] for x in data_grenzen2], [x[1] for x in data_grenzen2], 'o', color="red", label="Grenzen des konst. Maximums")
plt.errorbar([x[0] for x in data_2_Feld], [x[1] for x in data_2_Feld],yerr=error_y_2_Feld, xerr=error_x_2_Feld, fmt='o', label="Magnetfeld")
plt.errorbar([x[0] for x in data_2_grund], [x[1] for x in data_2_grund], yerr= error_y_2_grund, xerr=error_x_2_grund, fmt='o', label="Untergrundmessung")
plt.errorbar([x[0] for x in data_2_gesamt], [x[1] for x in data_2_gesamt], yerr=error_y_2_gesamt, xerr=error_x_2_gesamt, fmt='o', label="Gesamtfeld")

plt.plot(x_fit_data2, y_fit_data2, label="Fit")
ax.set_xlabel("Abstand in cm")
ax.set_ylabel("Magnetfeldstärke in mT")
ax.legend()
ax.grid('minor')
fig.savefig("../Graphics/Experiment4_1.5A_ohne_l_grenze.pdf")
fig.show()



