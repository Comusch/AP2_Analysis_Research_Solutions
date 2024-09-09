import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

print("-------------Load Data---------")
data_set1 = an.read_csv_file("TRA-Aufgabe2_Fall1.csv")
data_set1 = data_set1[1:]
print(data_set1)

data_set2 = an.read_csv_file("TRA-Aufgabe2_Fall2.csv")
data_set2 = data_set2[1:]
print(data_set2)

data_set3 = an.read_csv_file("TRA-Aufgabe2_Fall3.csv")
data_set3 = data_set3[1:]
print(data_set3)

print("------------Prepare data-----------")
data_amplitude_1 = []
for set in data_set1:
    if set[2]*10**(3)/set[1] > 300:
        continue
    data_amplitude_1.append((set[0], set[2]*10**(3)/set[1]))

data_amplitude_2 = []
for set in data_set2:
    data_amplitude_2.append((set[0], set[2]/set[1]))

data_amplitude_3 = []
for set in data_set3:
    data_amplitude_3.append((set[0], set[2]*10**(3)/set[1]))

print("-----------fitting to the three graphs------------")
def fit_func_wC_woR(R_c, S):
    return S*R_c

def fit_func_wC_wR(R_c, S):
    r_ce = 50.16058 # kOhm
    u_r_CE = 0.8244
    R_L = 10 # kOhm
    # Use np.where to handle cases where R_c is 0 in an array context
    return np.where(R_c == 0, 0, S * (1 / (1 / R_c + 1 / R_L + 1 / r_ce)))

def fit_func_woC_woR(R_c, R_E):
    return R_c/R_E


print("Compute with C and without C:")
#popt_1, pcov_1 = opt.curve_fit(fit_func_wC_woR, np.array(data_amplitude_1)[:,0], np.array(data_amplitude_1)[:, 1])
S = 19.6
print(S)
S1 = S
u_S1 = 0.2

fit_R_c_1 = np.linspace(0, 10, 1000)
fit_A_1 = fit_func_wC_woR(fit_R_c_1, S1)

print("-----")
print("Compute without C and R:")
#popt_2, pcov_2 = opt.curve_fit(fit_func_woC_woR, np.array(data_amplitude_2)[:,0], np.array(data_amplitude_2)[:, 1])
print(f"R_E: 1")
R_E2 = 1
u_R_E2 = 1

fit_R_c_2 = fit_R_c_1
fit_A_2 = fit_func_woC_woR(fit_R_c_2, R_E2)

print("------")
print("Compute with C and R:")
#popt_3, pcov_3 = opt.curve_fit(fit_func_woC_woR, np.array(data_amplitude_3)[:,0], np.array(data_amplitude_3)[:, 1])
print(S)
S2 = S
u_S2 = 0.2

fit_R_c_3 = fit_R_c_1
fit_A_3 = fit_func_wC_wR(fit_R_c_3, S2)

print("-------------Plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot(np.array(data_amplitude_1)[:,0], np.array(data_amplitude_1)[:, 1], "o", label="Measurement with C_E, without R_L")
plt.plot(np.array(data_amplitude_2)[:,0], np.array(data_amplitude_2)[:, 1], "o", label="Measurement without C_E and R_L")
plt.plot(np.array(data_amplitude_3)[:, 0], np.array(data_amplitude_3)[:, 1], "o", label="Measurement with C_E and R_L")
plt.plot(fit_R_c_1, fit_A_1, "-", label="Compute the expectation with C_E, without R_L")
plt.plot(fit_R_c_2, fit_A_2, "-", label="Compute the expectation without C_E and R_L")
plt.plot(fit_R_c_3, fit_A_3, "-", label="Compute the expectation with C_E and R_L")
plt.xlabel("R_C in kOhm")
plt.ylabel("A = u_a/u_e")
plt.grid()
plt.legend()
plt.savefig("../Graphics/Experiment6_Amplification.pdf")
plt.show()