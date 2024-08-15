import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


print("--------------VAK Experiment 3--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("Experiment3_Saugleistung.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

print("-----------Initial constants-----------")
p_0 = 957*10**2 #Pa
u_p_0 = 0.01*10**2 #Pa
u_p = 0.1*10**2 #Pa

V = 80 *10**-6 #m^3
u_V = 0.1*10**-6 #m^3


print("-----------Calculation of the Saugvermögen-----------")
for i in range(len(data_orignal)):
    if data_orignal[i][0] == 18.6:
        data_orignal[i][0] = 5.3*10**1 #Pa
    elif data_orignal[i][0] == 23.7:
        data_orignal[i][0] = 9*10**1 #Pa
    elif data_orignal[i][0] == 30.5:
        data_orignal[i][0] = 1.5*10**2 #Pa
    else:
        print("Error: The pressure is not in the list")
print(data_orignal)

average_t1 = 0
average_t2 = 0
average_t3 = 0

n1 = 0
n2 = 0
n3 = 0

for i in range(len(data_orignal)):
    if data_orignal[i][0] == 5.3*10**1:
        average_t1 += data_orignal[i][1]
        n1 += 1
    elif data_orignal[i][0] == 9*10**1:
        average_t2 += data_orignal[i][1]
        n2 += 1
    elif data_orignal[i][0] == 1.5*10**2:
        average_t3 += data_orignal[i][1]
        n3 += 1
    else:
        print("Error: The pressure is not in the list")
average_t1 = average_t1/n1
average_t2 = average_t2/n2
average_t3 = average_t3/n3
standard_deviation_t1 = 0
standard_deviation_t2 = 0
standard_deviation_t3 = 0
for i in range(len(data_orignal)):
    if data_orignal[i][0] == 5.3*10**1:
        standard_deviation_t1 += (data_orignal[i][1] - average_t1)**2
    elif data_orignal[i][0] == 9*10**1:
        standard_deviation_t2 += (data_orignal[i][1] - average_t2)**2
    elif data_orignal[i][0] == 1.5*10**2:
        standard_deviation_t3 += (data_orignal[i][1] - average_t3)**2
    else:
        print("Error: The pressure is not in the list")
standard_deviation_t1 = np.sqrt(standard_deviation_t1/(n1-1))
standard_deviation_t2 = np.sqrt(standard_deviation_t2/(n2-1))
standard_deviation_t3 = np.sqrt(standard_deviation_t3/(n3-1))
t_uncertainty = 1.32
u_t1 = standard_deviation_t1*t_uncertainty/np.sqrt(n1)
u_t2 = standard_deviation_t2*t_uncertainty/np.sqrt(n2)
u_t3 = standard_deviation_t3*t_uncertainty/np.sqrt(n3)

data_prepared = [(5.3*10**1, average_t1, u_t1), (9*10**1, average_t2, u_t2), (1.5*10**2, average_t3, u_t3)]

data_saugvermoegen = []
for set in data_prepared:
    saugvermoegen = p_0/set[0]* V/set[1] *(60*60)
    u_saugvermoegen = np.sqrt((u_p_0/set[0]*V/set[1])**2 + (p_0/set[0]**2 * u_p * V/set[1])**2 + (p_0/set[0] * u_V/set[1])**2 + (p_0/set[0] * V/set[1]**2 * set[2])**2)*(60*60)
    data_saugvermoegen.append((saugvermoegen, u_saugvermoegen))
    print(f"Saugvermögen: {saugvermoegen}+-{u_saugvermoegen}")
print(data_saugvermoegen)

