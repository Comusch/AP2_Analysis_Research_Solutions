import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

print("--------------VAK Experiment 3--------------")
print("-----------Data loading-----------")

# CSV-Dateien einlesen
data_orignal = an.read_csv_file("Experiment2_Capillaren.csv")
data_orignal = data_orignal[1:]  # Überspringen der Kopfzeile
print(data_orignal)

data_kalibrierung = an.read_csv_file("Pressure_Ampere_data.csv")
data_kalibrierung = data_kalibrierung[1:]  # Überspringen der Kopfzeile
print(data_kalibrierung)

# Konvertiere die Daten in numerische Werte (float)
data_kalibrierung = np.array(data_kalibrierung, dtype=float)

#sort data_kalibrierung by pressure
data_kalibrierung = data_kalibrierung[data_kalibrierung[:, 0].argsort()]

# Stromstärke und Druck extrahieren
stromstaerke = data_kalibrierung[:, 1]  # Stromstärken
druck = data_kalibrierung[:, 0]  # Druckwerte

print(f"Stromstaerke: {stromstaerke}")
print(f"Druck: {druck}")

data1 = []
data2 = []
data3 = []

# Interpolation für jeden Satz in den Originaldaten
for set in data_orignal:
    set[1] = float(set[1])  # Stelle sicher, dass die Stromstärke ein float ist
    print(f"Originale Stromstärke: {set[1]}")
    set[1] = np.interp(set[1], stromstaerke, druck)
    print(f"Interpolierter Druck: {set[1]}")

    if set[2] == 2:  # Vergleiche mit String, falls die CSV-Daten als Strings eingelesen werden
        data1.append(set)
    elif set[2] == 3:
        data2.append(set)
    elif set[2] == 25:
        data3.append(set)
    else:
        print("Error: The pressure is not in the list")

print("Data1:", data1)
print("Data2:", data2)
print("Data3:", data3)

print("-----------Fit the data in two parts with linear regression-----------")
print("Divide the data in two parts")
data1_1 = []
data1_2 = []
data2_1 = []
data2_2 = []
data3_1 = []
data3_2 = []
for set in data1:
    if set[1] > 8:
        data1_1.append(set)
    elif set[1] < 2:
        data1_2.append(set)

for set in data2:
    if set[1] > 5:
        data2_1.append(set)
    elif set[1] < 1:
        data2_2.append(set)

for set in data3:
    if set[1] > 1:
        data3_1.append(set)
    elif set[1] < 0.5:
        data3_2.append(set)

print(f"Data1_1: {data1_1}")
print(f"Data1_2: {data1_2}")
print(f"Data2_1: {data2_1}")
print(f"Data2_2: {data2_2}")
print(f"Data3_1: {data3_1}")
print(f"Data3_2: {data3_2}")

print("-------Fit the data---------")
slope1, intercept1 = np.polyfit([x[0] for x in data1_1], [np.log(x[1]) for x in data1_1], 1)
slope1_2, intercept1_2 = np.polyfit([x[0] for x in data1_2], [np.log(x[1]) for x in data1_2], 1)
slope2, intercept2 = np.polyfit([x[0] for x in data2_1], [np.log(x[1]) for x in data2_1], 1)
slope2_2, intercept2_2 = np.polyfit([x[0] for x in data2_2], [np.log(x[1]) for x in data2_2], 1)
slope3, intercept3 = np.polyfit([x[0] for x in data3_1], [np.log(x[1]) for x in data3_1], 1)
slope3_2, intercept3_2 = np.polyfit([x[0] for x in data3_2], [np.log(x[1]) for x in data3_2], 1)

print(f"slope1: {slope1}, intercept1: {intercept1}")
print(f"slope1_2: {slope1_2}, intercept1_2: {intercept1_2}")
print("-------")
print(f"slope2: {slope2}, intercept2: {intercept2}")
print(f"slope2_2: {slope2_2}, intercept2_2: {intercept2_2}")
print("-------")
print(f"slope3: {slope3}, intercept3: {intercept3}")
print(f"slope3_2: {slope3_2}, intercept3_2: {intercept3_2}")

fig, ax = plt.subplots(figsize=(8, 8))

print("----------Create the fits and Plot the data----------")
x1 = np.linspace(data1_1[0][0], data1_1[len(data1_1)-1][0], 100)
y1 = np.exp(intercept1) * np.exp(slope1 * x1)
plt.plot(x1, y1, label="Fit for the first section 2mm")

x1_2 = np.linspace(data1_2[0][0], data1_2[len(data1_2)-1][0], 100)
y1_2 = np.exp(intercept1_2) * np.exp(slope1_2 * x1_2)
plt.plot(x1_2, y1_2, label="Fit for the secound section 2mm")

x2 = np.linspace(data2_1[0][0], data2_1[len(data2_1)-1][0], 100)
y2 = np.exp(intercept2) * np.exp(slope2 * x2)
plt.plot(x2, y2, label="Fit for the first section 3mm")

x2_2 = np.linspace(data2_2[0][0], data2_2[len(data2_2)-1][0], 100)
y2_2 = np.exp(intercept2_2) * np.exp(slope2_2 * x2_2)
plt.plot(x2_2, y2_2, label="Fit for the secound section 3mm")

x3 = np.linspace(data3_1[0][0], data3_1[len(data3_1)-1][0], 100)
y3 = np.exp(intercept3) * np.exp(slope3 * x3)
plt.plot(x3, y3, label="Fit for the first section 25mm")

x3_2 = np.linspace(data3_2[0][0], data3_2[len(data3_2)-1][0], 100)
y3_2 = np.exp(intercept3_2) * np.exp(slope3_2 * x3_2)
plt.plot(x3_2, y3_2, label="Fit for the secound section 25mm")

plt.plot([x[0] for x in data1], [x[1] for x in data1], 'o', label="2mm")
plt.plot([x[0] for x in data2], [x[1] for x in data2], 'x', label="3mm")
plt.plot([x[0] for x in data3], [x[1] for x in data3], 's', label="25mm")
plt.grid("minor")
ax.set_yscale("log")
ax.legend()
ax.set_xlabel("Zeit [s]")
ax.set_ylabel("Druck[hPa]")
fig.savefig("../Graphics/Pressure_time.pdf")
fig.show()

print("-----------Calculate the saugvermoegen-----------")
print ("------Schlauch------")
l_s = 0.558 #m
u_l_s = 0.001 #m

d_s = 0.025 #m
u_d_s = 0.001 #m

V_schlauch = (d_s/2)**2 * np.pi * l_s
u_V_schlauch = np.sqrt((d_s *np.pi * l_s * u_d_s)**2 + ((d_s/2)**2 * np.pi * u_l_s)**2)

s_eff_schlauch_1 = slope3 * V_schlauch *(-1) *60*60
s_eff_schlauch_2 = slope3_2 * V_schlauch *(-1) *60*60
print(f"S_eff Schlauch molekular (m³/h): {s_eff_schlauch_1}")
print(f"S_eff Schlauch viskoser (m³/h): {s_eff_schlauch_2}")

print("------Capillaren------")
l_k = 0.095 #m
u_l_k = 0.002 #m

d_k = 0.002 #m
u_d_k = 0.0001 #m

V_k = (d_k/2)**2 * np.pi * l_k
u_V_k = np.sqrt((d_k *np.pi * l_k * u_d_k)**2 + ((d_k/2)**2 * np.pi * u_l_k)**2)

s_eff_k_1 = slope1 * V_k *(-1) *60*60
s_eff_k_2 = slope1_2 * V_k *(-1) *60*60
print(f"S_eff Capillaren molekular (m³/h): {s_eff_k_1}")
print(f"S_eff Capillaren viskoser (m³/h): {s_eff_k_2}")

print("----------Calculate the conductance and the uncertainty----------")
eta_air = 1.82*10**-5 #Pa*s
p_desh = 5*10**2 #Pa
k_b = 1.38*10**-23 #J/K
T = 25+273.15 #K
m_mol = 0.028949 #kg/mol
m = 0.028949/6.022*10**23 #kg

conductance_schlauch_2 = np.pi * (d_s)**4 /(128*eta_air*l_s) * p_desh*60*60
u_conductance_schlauch_2 = np.sqrt((np.pi * (d_s)**4 /(128*eta_air*l_s**2) * p_desh*60*60 * u_l_s)**2 + (np.pi * (d_s)**3*4 /(128*eta_air*l_s) * p_desh*60*60 * u_d_s)**2)

conductance_schlauch_1 = 121*d_s**3/l_s *60*60
u_conductance_schlauch_1 = np.sqrt((121*d_s**3/l_s**2 *60*60 * u_l_s)**2 + (363*d_s**2/l_s *60*60 * u_d_s)**2)
print(f"Conductance Schlauch molekular (m³/h): {conductance_schlauch_1} +- {u_conductance_schlauch_1}")
print(f"Conductance Schlauch viskoser (m³/h): {conductance_schlauch_2} +- {u_conductance_schlauch_2}")
print("-------")

conductance_cabilaren_2 = np.pi * (d_k)**4 /(128*eta_air*l_k) * p_desh*60*60
u_conductance_cabilaren_2 = np.sqrt((np.pi * (d_k)**4 /(128*eta_air*l_k**2) * p_desh*60*60 * u_l_k)**2 + (np.pi * (d_k)**3*4 /(128*eta_air*l_k) * p_desh*60*60 * u_d_k)**2)

conductance_cabilaren_1 = 121*d_k**3/l_k *60*60
u_conductance_cabilaren_1 = np.sqrt((121*d_k**3/l_k**2 *60*60 * u_l_k)**2 + (363*d_k**2/l_k *60*60 * u_d_k)**2)
print(f"Conductance Capillaren molekular (m³/h): {conductance_cabilaren_1} +- {u_conductance_cabilaren_1}")
print(f"Conductance Capillaren viskoser (m³/h): {conductance_cabilaren_2} +- {u_conductance_cabilaren_2}")

print("-----------Conductance of the capillaren construction-----------")
s = 3.7 #m^3/h
u_s = 0.1 #m^3/h

s_eff_theo_schlauch1 = 1/(1/s +1/conductance_schlauch_1)
u_s_eff_theo_schlauch1 = np.sqrt((conductance_schlauch_1**2/(s+conductance_schlauch_1)**2 * u_s**2) + (s**2/(s+conductance_schlauch_1)**2 * u_conductance_schlauch_1**2))

s_eff_theo_schlauch2 = 1/(1/s +1/conductance_schlauch_2)
u_s_eff_theo_schlauch2 = np.sqrt((conductance_schlauch_2**2/(s+conductance_schlauch_2)**2 * u_s**2) + (s**2/(s+conductance_schlauch_2)**2 * u_conductance_schlauch_2**2))
print(f"S_eff theo Schlauch molekular (m³/h): {s_eff_theo_schlauch1} +- {u_s_eff_theo_schlauch1}")
print(f"S_eff theo Schlauch viskoser (m³/h): {s_eff_theo_schlauch2} +- {u_s_eff_theo_schlauch2}")

s_eff_theo_k1 = 1/(1/s +1/conductance_cabilaren_1 + 1/conductance_schlauch_1)
u_s_eff_theo_k1 = np.sqrt((conductance_schlauch_1**2*conductance_cabilaren_1**2/(s*conductance_cabilaren_1+conductance_cabilaren_1*conductance_schlauch_1+s*conductance_schlauch_1)*u_s)**2 + (s**2*conductance_schlauch_1**2/(s*conductance_cabilaren_1+conductance_cabilaren_1*conductance_schlauch_1+s*conductance_schlauch_1)*u_conductance_cabilaren_1)**2 + (s**2*conductance_cabilaren_1**2/(s*conductance_cabilaren_1+conductance_cabilaren_1*conductance_schlauch_1+s*conductance_schlauch_1)*u_conductance_schlauch_1)**2)
s_eff_theo_k2 = 1/(1/s +1/conductance_cabilaren_2 + 1/conductance_schlauch_2)
u_s_eff_theo_k2 = np.sqrt((conductance_schlauch_2**2*conductance_cabilaren_2**2/(s*conductance_cabilaren_2+conductance_cabilaren_2*conductance_schlauch_2+s*conductance_schlauch_2)*u_s)**2 + (s**2*conductance_schlauch_2**2/(s*conductance_cabilaren_2+conductance_cabilaren_2*conductance_schlauch_2+s*conductance_schlauch_2)*u_conductance_cabilaren_2)**2 + (s**2*conductance_cabilaren_2**2/(s*conductance_cabilaren_2+conductance_cabilaren_2*conductance_schlauch_2+s*conductance_schlauch_2)*u_conductance_schlauch_2)**2)
print(f"S_eff theo Capillaren molekular (m³/h): {s_eff_theo_k1} +- {u_s_eff_theo_k1}")
print(f"S_eff theo Capillaren viskoser (m³/h): {s_eff_theo_k2} +- {u_s_eff_theo_k2}")

