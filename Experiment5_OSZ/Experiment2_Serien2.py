import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy import stats

print("---------------Load Data---------------")
data = an.read_csv_file("Experiment5_Schwingkreis2.csv")
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
time_amplitude = []
for set in data:
    time_amplitude.append((set[1]*10**(-6), set[0]))

print("---------------fit Data---------------")
def fit_func(t, a, b):
    return a*np.exp(b*t)

fit_data = []
for set in time_amplitude:
    fit_data.append((set[0], np.log(set[1])))
fit_data = np.array(fit_data)

slope, intercept, r_value, p_value, std_err = stats.linregress(fit_data[:, 0], fit_data[:, 1])
print(f"slope: {slope}")
print(f"intercept: {intercept}")
print(f"r_value: {r_value}")
print(f"p_value: {p_value}")
print(f"std_err: {std_err}")

print(f"slope = delta = {-slope} +- {std_err}")


time_fit = np.linspace(0, 112*10**(-6), 100)
amplitude_fit = fit_func(time_fit, np.exp(intercept), slope)

theo_delta = R/(2*L)
print(f"delta theoretic: {theo_delta}")
u_theo_delta = np.sqrt((u_R/(2*L))**2 + (R*u_L/(2*L**2))**2)
print(f"u_delta theoretic: {u_theo_delta}")

print("----------------Plot Data----------------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(time_amplitude)[:, 0]), (np.array(time_amplitude)[:, 1]), "o", label="Amplitude")
plt.plot(time_fit, amplitude_fit, label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude (V)")
plt.yscale("log")
plt.savefig("../Graphics/Experiment5_dampfung_2.pdf")
plt.show()
