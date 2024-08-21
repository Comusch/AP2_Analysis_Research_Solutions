import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

print("---------------Load Data---------------")
data = an.read_csv_file("Experiment5_task_2.csv")
data = data[1:]
print(data)

#initial constants
C = 5.6*10**(-9) #F
u_C = 0.1*C #F
R = 2.2*10**3 #Ohm
u_R = 0.01*R #Ohm

print("---------------prepare Data---------------")
data_phase = []
for set in data:
    data_phase.append((set[3], set[2]))
print(data_phase)

data_amplitude = []
for set in data:
    data_amplitude.append((set[3], set[1]/set[0]))

print("---------------Plot and fit Data---------------")
print("--------Fit Phase--------")
def fit_func_phase(f, R_C):
    return np.arctan(-f*2*np.pi*R_C)*180/np.pi

popt_phase, pcov_phase = opt.curve_fit(fit_func_phase, (np.array(data_phase)[:, 0]), (np.array(data_phase)[:, 1]))
print(popt_phase)
print(f"R_C um 10^3 größer: {popt_phase[0]}")
print(f"u_R_C um 10^3 größer: {np.sqrt(pcov_phase[0][0])}")

f_fit_phase = np.linspace(0.1, 100, 1000)
phase_fit = fit_func_phase(f_fit_phase, popt_phase[0])

theo_R_C = 2.2*10**3*5.6*10**(-9)*10**3 #2.2kOhm * 5.6nF *10^3
u_theo_R_C = np.sqrt((u_C*R*10**3)**2 + (u_R*C*10**3)**2)
print(f"Theoretical R_C um 10^3 größer: {theo_R_C} +- {u_theo_R_C}")
phase_fit_theo = fit_func_phase(f_fit_phase, theo_R_C)

w_g_p = 1/popt_phase[0] *1/(2*np.pi)
u_w_g_p = np.sqrt(pcov_phase[0][0])/popt_phase[0]**2 *1/(2*np.pi)
print(f"w_g_p: {w_g_p}")
theo_w_g_p = 1/theo_R_C *1/(2*np.pi)
u_theo_w_g_p = np.sqrt((u_theo_R_C/theo_R_C**2)**2) *1/(2*np.pi)
print(f"Theoretical w_g_p: {theo_w_g_p} +- {u_theo_w_g_p}")

print("-----Plot phase-----")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(data_phase)[:, 0]), (np.array(data_phase)[:, 1]),"o", label="Phase")
plt.plot(f_fit_phase, phase_fit_theo, label="Theorie Line")
plt.plot(f_fit_phase, phase_fit, label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Frequenz (kHz)")
plt.ylabel("Phase (°)")
plt.xscale("log")
plt.savefig("../Graphics/Experiment5_2_phase.pdf")
plt.show()

print("--------Fit Amplitude--------")
def fit_func(f, R_C):
    return 1/(np.sqrt(1+(f*2*np.pi*R_C)**2))

popt, pcov = opt.curve_fit(fit_func, (np.array(data_amplitude)[:, 0]), (np.array(data_amplitude)[:, 1]))
print(popt)
print(f"R_C: {popt[0]}")
print(f"u_R_C: {np.sqrt(pcov[0][0])}")
R_C = popt[0]
u_R_C = np.sqrt(pcov[0][0])

f_fit = np.linspace(0.1, 100, 1000)
amplitude_fit = fit_func(f_fit, R_C)

theo_R_C = 2.2*10**3*5.6*10**(-9)*10**3 #2.2kOhm * 5.6nF *10^3
print(f"Theoretical R_C: {theo_R_C} +- {u_theo_R_C}")
amplitude_fit_theo = fit_func(f_fit, theo_R_C)

w_g_a = 1/popt[0] *1/(2*np.pi)
u_w_g_a = np.sqrt(pcov[0][0])/popt[0]**2
print(f"w_g_a: {w_g_a}")
theo_w_g_a = 1/theo_R_C *1/(2*np.pi)
u_theo_w_g_a = np.sqrt((u_theo_R_C/theo_R_C**2)**2) *1/(2*np.pi)
print(f"Theoretical w_g_a: {theo_w_g_a} +- {u_theo_w_g_a}")

print("-----Plot amplitude-----")

fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(data_amplitude)[:, 0]), (np.array(data_amplitude)[:, 1]),"o", label="Amplitude")
plt.plot(f_fit, amplitude_fit_theo, label="Theorie Line")
plt.plot(f_fit, amplitude_fit, label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Frequenz (kHz)")
plt.ylabel("Verhältnis der Amplituden von Eingangs- und Ausgangsspannung")
plt.xscale("log")
plt.savefig("../Graphics/Experiment5_2_amplitude.pdf")
plt.show()
print("---------------done---------------")

