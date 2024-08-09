import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math

# Load the data
print("Fadenstrahlrohr")
print("-----------Data loading-----------")
data_I_variations = an.read_csv_file("Fadenstrahlrohr-Stromstarke_Variation.csv")
print(data_I_variations)

data_I_variations = data_I_variations[1:]

data_U_variations = an.read_csv_file("Fadenstrahlrohr_Spannung_Variation.csv")
print(data_U_variations)

data_U_variations = data_U_variations[1:]

print("-----------Initial the constants-----------")
#precalculation of the values
N = 130 # Windungszahl
R = 150 * 10**(-3) # m
u_R = 0.0002 * 10**(-3) # m

r50 = (50*10**(-3)) # m
r40 = (40*10**(-3)) # m
r30 = (30*10**(-3)) # m

u_r = 0.1 * 10**(-3) # m uncertainty of the radius

mue_0 = 4 * math.pi * 10**(-7) # Vs/(Am)

print("-----------splite the arrays in all of the radius-----------")
data_r50_I = []
data_r40_I = []
data_r30_I = []
U_while_I = 187
unc_U_while_I = 0.5

data_r50_U = []
data_r40_U = []
data_r30_U = []
I_while_U = 1.35
unc_I_while_U = 0.005


for set in data_I_variations:
    if set[3] == 50:
        data_r50_I.append(set)
    elif set[3] == 40:
        data_r40_I.append(set)
    elif set[3] == 30:
        data_r30_I.append(set)
    else:
        print("Error in the radius")

for set in data_U_variations:
    if set[3] == 50:
        data_r50_U.append(set)
    elif set[3] == 40:
        data_r40_U.append(set)
    elif set[3] == 30:
        data_r30_U.append(set)
    else:
        print("Error in the radius")

print("-----------Calculate the average I and U-----------")
#calculate the average I and U
t = 1.06 # because the number of datasets are 10
print ("------r50 I------")
I_average_r50 = 0
for set in data_r50_I:
    I_average_r50 += set[2]
I_average_r50 = I_average_r50/len(data_r50_I)
print(f"len(data_r50_I): {len(data_r50_I)}")
print(f"Average I for r50: {I_average_r50}")
standard_deviation_I_r50 = math.sqrt(sum([(data_r50_I[i][2] - I_average_r50)**2 for i in range(len(data_r50_I))])/(len(data_r50_I)-1))
print(f"Standard deviation of I for r50: {standard_deviation_I_r50}")
standard_deviation_I_r50_of_average = standard_deviation_I_r50*t/math.sqrt(len(data_r50_I))
print(f"Standard deviation of average I for r50: {standard_deviation_I_r50_of_average}")

print ("------r40 I------")
I_average_r40 = 0
for set in data_r40_I:
    I_average_r40 += set[2]
I_average_r40 = I_average_r40/len(data_r40_I)
print(f"Average I for r40: {I_average_r40}")
standard_deviation_I_r40 = math.sqrt(sum([(data_r40_I[i][2] - I_average_r40)**2 for i in range(len(data_r40_I))])/(len(data_r40_I)-1))
print(f"Standard deviation of I for r40: {standard_deviation_I_r40}")
standard_deviation_I_r40_of_average = standard_deviation_I_r40*t/math.sqrt(len(data_r40_I))
print(f"Standard deviation of average I for r40: {standard_deviation_I_r40_of_average}")

print ("------r30 I------")
I_average_r30 = 0
for set in data_r30_I:
    I_average_r30 += set[2]
I_average_r30 = I_average_r30/len(data_r30_I)
print(f"Average I for r30: {I_average_r30}")
standard_deviation_I_r30 = math.sqrt(sum([(data_r30_I[i][2] - I_average_r30)**2 for i in range(len(data_r30_I))])/(len(data_r30_I)-1))
print(f"Standard deviation of I for r30: {standard_deviation_I_r30}")
standard_deviation_I_r30_of_average = standard_deviation_I_r30*t/math.sqrt(len(data_r30_I))
print(f"Standard deviation of average I for r30: {standard_deviation_I_r30_of_average}")

print ("------r50 U------")
U_average_r50 = 0
for set in data_r50_U:
    U_average_r50 += set[1]
U_average_r50 = U_average_r50/len(data_r50_U)
print(f"Average U for r50: {U_average_r50}")
standard_deviation_U_r50 = math.sqrt(sum([(data_r50_U[i][1] - U_average_r50)**2 for i in range(len(data_r50_U))])/(len(data_r50_U)-1))
print(f"Standard deviation of U for r50: {standard_deviation_U_r50}")
standard_deviation_U_r50_of_average = standard_deviation_U_r50*t/math.sqrt(len(data_r50_U))
print(f"Standard deviation of average U for r50: {standard_deviation_U_r50_of_average}")

print ("------r40 U------")
U_average_r40 = 0
for set in data_r40_U:
    U_average_r40 += set[1]
U_average_r40 = U_average_r40/len(data_r40_U)
print(f"Average U for r40: {U_average_r40}")
standard_deviation_U_r40 = math.sqrt(sum([(data_r40_U[i][1] - U_average_r40)**2 for i in range(len(data_r40_U))])/(len(data_r40_U)-1))
print(f"Standard deviation of U for r40: {standard_deviation_U_r40}")
standard_deviation_U_r40_of_average = standard_deviation_U_r40*t/math.sqrt(len(data_r40_U))
print(f"Standard deviation of average U for r40: {standard_deviation_U_r40_of_average}")

print ("------r30 U------")
U_average_r30 = 0
for set in data_r30_U:
    U_average_r30 += set[1]
U_average_r30 = U_average_r30/len(data_r30_U)
print(f"Average U for r30: {U_average_r30}")
standard_deviation_U_r30 = math.sqrt(sum([(data_r30_U[i][1] - U_average_r30)**2 for i in range(len(data_r30_U))])/(len(data_r30_U)-1))
print(f"Standard deviation of U for r30: {standard_deviation_U_r30}")
standard_deviation_U_r30_of_average = standard_deviation_U_r30*t/math.sqrt(len(data_r30_U))
print(f"Standard deviation of average U for r30: {standard_deviation_U_r30_of_average}")

print("-----------Calculate the B and the uncertainties-----------")
#calculate the B and the uncertainties
print("----")
B_r50_I = mue_0* (4/5)**(3/2) * N * I_average_r50 / R
print(f"B for r50: {B_r50_I}")
print(f"I_average_r50: {I_average_r50}")
print(f"standard_deviation_I_r50_of_average: {standard_deviation_I_r50_of_average}")
u_B_r50 = math.sqrt((mue_0* (4/5)**(3/2) * N / R * standard_deviation_I_r50_of_average)**2 + (mue_0* (4/5)**(3/2) * N * I_average_r50 / R**2 * u_R)**2)
print(f"Uncertainty of B for r50: {u_B_r50}")

print("----")
B_r40_I = mue_0* (4/5)**(3/2) * N * I_average_r40 / R
print(f"B for r40: {B_r40_I}")
print(f"I_average_r40: {I_average_r40}")
print(f"standard_deviation_I_r40_of_average: {standard_deviation_I_r40_of_average}")
u_B_r40 = math.sqrt((mue_0* (4/5)**(3/2) * N / R * standard_deviation_I_r40_of_average)**2 + (mue_0* (4/5)**(3/2) * N * I_average_r40 / R**2 * u_R)**2)
print(f"Uncertainty of B for r40: {u_B_r40}")

print("----")
B_r30_I = mue_0* (4/5)**(3/2) * N * I_average_r30 / R
print(f"B for r30: {B_r30_I}")
print(f"I_average_r30: {I_average_r30}")
print(f"standard_deviation_I_r30_of_average: {standard_deviation_I_r30_of_average}")
u_B_r30 = math.sqrt((mue_0* (4/5)**(3/2) * N / R * standard_deviation_I_r30_of_average)**2 + (mue_0* (4/5)**(3/2) * N * I_average_r30 / R**2 * u_R)**2)
print(f"Uncertainty of B for r30: {u_B_r30}")

print("----")
B_I_while_U = mue_0* (4/5)**(3/2) * N * I_while_U / R
u_B_I_while_U = math.sqrt((mue_0* (4/5)**(3/2) * N / R * unc_I_while_U)**2 + (mue_0* (4/5)**(3/2) * N * I_while_U / R**2 * u_R)**2)
print(f"Uncertainty of B by I while U variated: {u_B_I_while_U}")
print(f"I while U is variated: {I_while_U}")
print(f"B for I while U is variated: {B_I_while_U}")

print("-----------Calculate the specific charge and the uncertainties-----------")
#calculate the specific charge and the uncertainties
print("----")
q_r50 = 2 * U_while_I / (B_r50_I**2 * (50*10**(-3))**2)
print(f"Specific charge for r50: {q_r50}")
u_q_r50 = math.sqrt((4*U_while_I/(B_r50_I**2 * r50**3)*u_r)   +(4 * U_while_I / (B_r50_I**3 * r50**2) * u_B_r50)**2)
print(f"Uncertainty of the specific charge for r50: {u_q_r50}")

print("----")
q_r40 = 2 * U_while_I / (B_r40_I**2 * (40*10**(-3))**2)
print(f"Specific charge for r40: {q_r40}")
u_q_r40 = math.sqrt((4*U_while_I/(B_r40_I**2 * r40**3)*u_r)   +(4 * U_while_I / (B_r40_I**3 * r40**2) * u_B_r40)**2)
print(f"Uncertainty of the specific charge for r40: {u_q_r40}")

print("----")
q_r30 = 2 * U_while_I / (B_r30_I**2 * (30*10**(-3))**2)
print(f"Specific charge for r30: {q_r30}")
u_q_r30 = math.sqrt((4*U_while_I/(B_r30_I**2 * r30**3)*u_r)   +(4 * U_while_I / (B_r30_I**3 * r30**2) * u_B_r30)**2)
print(f"Uncertainty of the specific charge for r30: {u_q_r30}")

print("----")
q_u_r50 = 2 * U_average_r50 / (B_I_while_U**2 * r50**2)
print(f"Specific charge for r50 while U is variated: {q_u_r50}")
u_q_u_r50 = math.sqrt((4*U_average_r50/(B_I_while_U**2 * r50**3)*u_r)   +(2/ (B_I_while_U**2 * r50**2) * standard_deviation_U_r50_of_average)**2)
print(f"Uncertainty of the specific charge for r50 while U is variated: {u_q_u_r50}")

print("----")
q_u_r40 = 2 * U_average_r40 / (B_I_while_U**2 * r40**2)
print(f"Specific charge for r40 while U is variated: {q_u_r40}")
u_q_u_r40 = math.sqrt((4*U_average_r40/(B_I_while_U**2 * r40**3)*u_r)   +(2/ (B_I_while_U**2 * r40**2) * standard_deviation_U_r40_of_average)**2)
print(f"Uncertainty of the specific charge for r40 while U is variated: {u_q_u_r40}")

print("----")
q_u_r30 = 2 * U_average_r30 / (B_I_while_U**2 * r30**2)
print(f"Specific charge for r30 while U is variated: {q_u_r30}")
u_q_u_r30 = math.sqrt((4*U_average_r30/(B_I_while_U**2 * r30**3)*u_r)   +(2/ (B_I_while_U**2 * r30**2) * standard_deviation_U_r30_of_average)**2)
print(f"Uncertainty of the specific charge for r30 while U is variated: {u_q_u_r30}")

print("-----------Average the specific charge-----------")
#average the specific charge
q_m_average = (q_r50 + q_r40 + q_r30 + q_u_r50 + q_u_r40 + q_u_r30)/6
print(f"Average specific charge: {q_m_average}")
u_q_m_average = math.sqrt((u_q_r50**2 + u_q_r40**2 + u_q_r30**2 + u_q_u_r50**2 + u_q_u_r40**2 + u_q_u_r30**2)/6)
print(f"Uncertainty of the average specific charge: {u_q_m_average}")

replaceresult_q_m = (q_r50+ q_r40 +q_r30)/3
print(f"Replace result of q_m: {replaceresult_q_m}")
print("-----------Calculate the mass of the electron and the uncertainties-----------")
#calculate the mass of the electron and the uncertainties
charge = 1.7 * 10**(-19) # C
u_charge = 0.1 * 10**(-19) # C
m_e = charge/q_m_average
print(f"Mass of the electron: {m_e}")
u_m_e = math.sqrt((u_charge/q_m_average)**2 + (charge/q_m_average**2 * u_q_m_average)**2)
print(f"Uncertainty of the mass of the electron: {u_m_e}")

replace_result_m_e = replaceresult_q_m / charge
print(f"Replace result of m_e: {replace_result_m_e}")



