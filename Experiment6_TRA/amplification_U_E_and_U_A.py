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
    r_ce =5160.58
    u_r_CE = 824.4
    R_L =  10*10**(3)
    return S*(1/(1/R_c + 1/R_L + 1/r_ce))

def fit_func_woC_woR(R_c, R_E):
    return R_c/R_E


print("Fit with C and without C:")
popt_1, pcov_1 = opt.curve_fit(fit_func_wC_woR, np.array(data_amplitude_1)[:,0], np.array(data_amplitude_1)[:, 1])
print(popt_1)
S1 = popt_1[0]
u_S1 = pcov_1[0]

fit_R_c_1 = np.linspace(0, 10, 1000)
fit_A_1 = fit_func_wC_woR(fit_R_c_1, S1)

print("-----")
print("Fit without C and R:")
popt_2, pcov_2 = opt.curve_fit(fit_func_woC_woR, np.array(data_amplitude_2)[:,0], np.array(data_amplitude_2)[:, 1])
print(popt_2)
R_E2 = popt_2[0]
u_R_E2 = pcov_2[0]

fit_R_c_2 = fit_R_c_1
fit_A_2 = fit_func_woC_woR(fit_R_c_2, R_E2)

print("------")
print("Fit with C and R:")
popt_3, pcov_3 = opt.curve_fit(fit_func_woC_woR, np.array(data_amplitude_3)[:,0], np.array(data_amplitude_3)[:, 1])
print(popt_3)
S2 = popt_3[0]
u_S2 = pcov_3[0]

fit_R_c_3 = fit_R_c_1
fit_A_3 = fit_func_woC_woR(fit_R_c_3, S2)

print("-------------Plot data------------")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot(np.array(data_amplitude_1)[:,0], np.array(data_amplitude_1)[:, 1], "o", label="Measurement with C_E, without R_L")
plt.plot(np.array(data_amplitude_2)[:,0], np.array(data_amplitude_2)[:, 1], "o", label="Measurement without C_E and R_L")
plt.plot(np.array(data_amplitude_3)[:, 0], np.array(data_amplitude_3)[:, 1], "o", label="Measurement with C_E and R_L")
plt.plot(fit_R_c_1, fit_A_1, "-", label="Fit with C_E, without R_L")
plt.plot(fit_R_c_2, fit_A_2, "-", label="Fit without C_E and R_L")
plt.plot(fit_R_c_3, fit_A_3, "-", label="Fit with C_E and R_L")
plt.xlabel("R_C in kOhm")
plt.ylabel("A = u_a/u_e")
plt.grid()
plt.legend()
plt.savefig("../Graphics/Experiment6_Amplification.pdf")
plt.show()