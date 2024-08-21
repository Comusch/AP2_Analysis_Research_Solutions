import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

print("---------------Load Data---------------")
data = an.read_csv_file("Experiment5_Schwingkreis1.csv")
data = data[1:]
print(data)

#initial constants
L = 1.8*10**(-3) #H
u_L = 0.05*L #H
C = 6.8*10**(-9) #F
u_C = 0.1*C #F
R = 100 #Ohm
u_R = 0.01*R #Ohm

print("---------------prepare Data---------------")
data_phase = []
for set in data:
    data_phase.append((set[3]*10**3, set[2]))

data_amplitude = []
for set in data:
    data_amplitude.append((set[3]*10**3, set[1]/set[0]))

print("---------------Plot and fit Data---------------")
print("--------Fit Phase--------")
def fit_func_phase(f, f_0, delta):
    return -np.arctan((f**2-f_0**2)/(2*f*delta))*180/np.pi

popt_phase, pcov_phase = opt.curve_fit(fit_func_phase, (np.array(data_phase)[:, 0]), (np.array(data_phase)[:, 1]))
print(popt_phase)
print(f"f_0: {popt_phase[0]}")
f_0 = popt_phase[0]
print(f"u_f_0: {np.sqrt(pcov_phase[0][0])}")
print(f"delta: {popt_phase[1]}")
delta = popt_phase[1]
print(f"u_delta: {np.sqrt(pcov_phase[1][1])}")

f_fit_phase = np.linspace(0.1*10**3, 100*10**3, 1000)
phase_fit = fit_func_phase(f_fit_phase, f_0, delta)

theo_f_0 = 1/(2*np.pi*np.sqrt(L*C))
u_theo_f_0 = 1/(2*np.pi)*np.sqrt((-1/2*(C*L)**(-3/2)*C*u_L)**2 + (-1/2*(C*L)**(-3/2)*L*u_C)**2)
print(f"Theoretical f_0: {theo_f_0}+-{u_theo_f_0}")

theo_delta = R/(2*L)
u_theo_delta = np.sqrt((u_R/(2*L))**2 + (R*u_L/(2*L**2))**2)
print(f"Theoretical delta: {theo_delta}+-{u_theo_delta}")

theo_phase_fit = fit_func_phase(f_fit_phase, theo_f_0, theo_delta)
print("---------Plot Phase---------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(data_phase)[:, 0]), (np.array(data_phase)[:, 1]),"o", label="Phase")
plt.plot(f_fit_phase, theo_phase_fit, label="Theorie Line")
plt.plot(f_fit_phase, phase_fit, label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Phase (°)")
plt.xscale("log")
plt.savefig("../Graphics/Experiment5_Schwingkreis_phase.pdf")
plt.show()

print("--------Fit Amplitude--------")
def fit_func(f, f_0, delta):
    return 2*delta*f*2*np.pi/(np.sqrt(((f*2*np.pi)**2-(f_0*2*np.pi)**2)**2+ 4*delta**2*(f*2*np.pi)**2))

popt, pcov = opt.curve_fit(fit_func, (np.array(data_amplitude)[:, 0]), (np.array(data_amplitude)[:, 1]))
print(popt)
print(f"f_0: {popt[0]}")
f_0_2 = popt[0]
print(f"u_f_0: {np.sqrt(pcov[0][0])}")
print(f"delta: {popt[1]}")
delta_2 = popt[1]
print(f"u_delta: {np.sqrt(pcov[1][1])}")

f_fit = np.linspace(0.1*10**3, 100*10**3, 1000)
amplitude_fit = fit_func(f_fit, f_0_2, delta_2)

theo_f_0 = 1/(2*np.pi*np.sqrt(L*C))
u_theo_f_0 = 1/(2*np.pi)*np.sqrt((-1/2*(C*L)**(-3/2)*C*u_L)**2 + (-1/2*(C*L)**(-3/2)*L*u_C)**2)
print(f"Theoretical f_0: {theo_f_0}+-{u_theo_f_0}")

theo_delta = R/(2*L)
u_theo_delta = np.sqrt((u_R/(2*L))**2 + (R*u_L/(2*L**2))**2)
print(f"Theoretical delta: {theo_delta}+-{u_theo_delta}")

theo_amplitude_fit = fit_func(f_fit, theo_f_0, theo_delta)

print("---------Plot Amplitude---------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(data_amplitude)[:, 0]), (np.array(data_amplitude)[:, 1]),"o", label="Amplitude")
plt.plot(f_fit, theo_amplitude_fit, label="Theorie Line")
plt.plot(f_fit, amplitude_fit, label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Verhältnis Amplitude zwischen Eingang und Ausgang")
plt.xscale("log")
plt.savefig("../Graphics/Experiment5_Schwingkreis_amplitude.pdf")
plt.show()

print("--------Calculate B_f and Q_f--------")
B_f = delta/(np.pi)
print("B_f fit Phase: ", B_f)
Q_f = 1/(2*np.pi)*np.sqrt((f_0*2*np.pi)**2-4*delta**2)*1/B_f
print("Q_f fit Phase: ", Q_f)

B_f_2 = delta_2/(np.pi)
print("B_f fit Amplitude: ", B_f_2)
Q_f_2 = 1/(2*np.pi)*np.sqrt((f_0_2*2*np.pi)**2-4*delta_2**2)*1/B_f_2
print("Q_f fit Amplitude: ", Q_f_2)

print("--------Calculate B_f and Q_f Theoretical--------")
B_f_theo = theo_delta/(np.pi)
u_B_f_theo = u_theo_delta/(np.pi)
print(f"B_f Theoretical: {B_f_theo} +- {u_B_f_theo}")
f_res_theo = 1/(2*np.pi)*np.sqrt((theo_f_0*2*np.pi)**2-4*theo_delta**2)
Q_f_theo = f_res_theo/B_f_theo
u_f_res_theo = 1/(2*np.pi)*((theo_f_0*2*np.pi)**2-4*theo_delta**2)**(-1/2)*1/2*np.sqrt((2*theo_f_0*4*np.pi**2*u_theo_f_0)**2+ (-4*2*u_theo_delta)**2)
u_Q_f_theo = np.sqrt((u_theo_f_0/B_f_theo)**2 + (u_B_f_theo*f_res_theo/B_f_theo**2)**2)
print(f"Q_f Theoretical: {Q_f_theo} +- {u_Q_f_theo}")

