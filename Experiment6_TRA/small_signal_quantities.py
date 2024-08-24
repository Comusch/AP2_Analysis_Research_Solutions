import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.stats import linregress

#initial constants
k_b = 1.380649 * 10**(-23) #J/k
q = 1.6*10**(-19) #C


print("------------load Data-----------")
data_UEB_IB = an.read_csv_file("TRA-Aufgabe4_Teil1.csv")
data_UEB_IB = data_UEB_IB[1:]
print(data_UEB_IB)

data_UCE_IC = an.read_csv_file("TRA-Aufgabe4_Teil2.csv")
data_UCE_IC = data_UCE_IC[1:]
print(data_UCE_IC)

print("---------------plot data----------")
print("---------fit the function IB(UBE)------")

# Logarithmic transformation of the y-values to linearize the data
log_y = np.log(np.array(data_UEB_IB)[:, 1])
x = np.array(data_UEB_IB)[:, 0]

# Perform linear regression on the transformed data
slope, intercept, r_value, p_value, std_err = linregress(x, log_y)

# Convert back to exponential parameters
a = np.exp(intercept)  # a is the exponential of the intercept
b = slope  # b remains the slope

print(f"a = {a}")
print(f"b = {b}")

# Generate fitted values using the linear regression parameters
fit_U_BE = np.linspace(450, 680, 1000)
fit_log_I_B = intercept + slope * fit_U_BE  # linear regression equation

# Convert the linear fit back to exponential
fit_I_B = np.exp(fit_log_I_B)

print("Calculation of the temperature at the working point:")
T = b*10**8*k_b/q
u_T = std_err*10**8*k_b/q
print(f"T: {T} +- {u_T}")

print("----------Calculate Tangent at the working point")
U_BE_work = 562 #mV

data_tangent_calc = []
for i in range(len(fit_U_BE)):
    if fit_U_BE[i] > 562 - 10 and fit_U_BE[i] < 562 + 10:
        data_tangent_calc.append((fit_U_BE[i], fit_I_B[i]))

x_2 = np.array(data_tangent_calc)[:,0]
y_2 = np.array(data_tangent_calc)[:, 1]

slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_2, y_2)
print(f"slope2: {slope2}")
print(f"u_slope2: {std_err2}")

print("Calculation of r_BE:")
r_BE = 1/slope2 *10**(3)
u_r_BE = 1/slope2**2 * std_err2 *10**(3)
print(f"r_BE: {r_BE} +- {u_r_BE}")

x_tangent_1 = np.linspace(500, 650, 1000)
y_tangent_1 = slope2*x_tangent_1 + intercept2


print("-----------plot U_EB against IB----------")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot((np.array(data_UEB_IB)[:, 0]), (np.array(data_UEB_IB)[:, 1]), "o", label="Measurement points")
plt.plot(fit_U_BE, fit_I_B, "-", label=f"Fit with a = {a} and b = {b}")
plt.plot(x_tangent_1, y_tangent_1, "-", label="Tangent at the operation point")
plt.xlabel("U_BE in mV")
plt.ylabel("I_B in \mu A")
plt.grid()
plt.legend()
plt.savefig("../Graphics/Experiment6_IB_UEB.pdf")
plt.show()

print("-------Calculation of the steepness in all three operation points-------")
I_C = 561*10**(-6) #A
u_I_C = 1*10**(-6) #A

S = q*I_C/(k_b*T)
u_S = np.sqrt((q*u_I_C/(k_b*T))**2 + (q*I_C/(k_b*T**2)*u_T)**2)
print(f"Steepness: {S} +- {u_S} 1/Omega")

print("------fit tangent at the operation point in the function U_CE against IC-------")
U_CE_op = 5.71

data_tangent_calc2 = []
for set in data_UCE_IC:
    if set[0] > U_CE_op-2 and set[0] < U_CE_op+2:
        data_tangent_calc2.append(set)
print(data_tangent_calc2)

x_3 = np.array(data_tangent_calc2)[:,0]
y_3 = np.array(data_tangent_calc2)[:,1]

slope3, intercept3, r_value3, p_value3, std_err3 = linregress(x_3, y_3)

print(f"slope: {slope3}")
print(f"intercept: {intercept3}")

fit_U_CE = np.linspace(4, 8, 100)
fit_I_C = slope3*fit_U_CE + intercept3

print("Calculate r_CE:")
slope3 = 1*10**(-10)
r_CE = 1/(slope3-S*(0.562/5.71))*10**1
u_r_CE = 1/(slope3-S)*np.sqrt((std_err3)**2 + (u_S)**2)
print(f"r_CE: {r_CE} +- {u_r_CE}")

print("----------plot U_CE against IC-----------")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot((np.array(data_UCE_IC)[:, 0]), (np.array(data_UCE_IC)[:, 1]), "o", label="Measurement points")
plt.plot(fit_U_CE, fit_I_C, "-", label="Tangent at operation point")
plt.xlabel("U_CE in V")
plt.ylabel("I_C in \mu A")
plt.grid()
plt.legend()
plt.savefig("../Graphics/Experiment6_IC_UCE.pdf")
plt.show()