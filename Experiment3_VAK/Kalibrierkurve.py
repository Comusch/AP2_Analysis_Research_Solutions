import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#defining the functions for the fits
def exponential(x, a, b):
    return a * np.exp(b * x)

def exponential2(x, a, b, c):
    return a * np.exp(b * x**c)

def exponential3(x, a, b, c, d):
    return a * np.exp(b * x**c) +d



# Load the data
print("--------------VAK Experiment 3--------------")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("Pressure_Ampere_data.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

print("-----------Plot the data, Pressure vs. Amperage-----------")
data = []
for set in data_orignal:
    data.append((set[1], set[0]))
print(data)

#sort the data by pressure
data.sort(key=lambda x: x[1])
print(data)
#an.plot_data(data, plot_fit=False, scale_y="log" ,lable_y="Pressure [mbar]", lable_x="Amperage [A]", file_name="Pressure vs. Amperage.pdf")
plt.plot([x[0] for x in data], [x[1] for x in data], 'o')

print("-----------Calculate the fits of the graph-----------")
#divide the data in 3 parts
data1 = []
data2 = []
data3 = []
for set in data:
    if set[0] < 20:
        data1.append(set)
    elif set[0] < 50:
        data2.append(set)
    elif set[0] < 65:
        data3.append(set)

#fit the data

#lineare regression in the secound section
print("-----------Linear regression in the secound section-----------")

slope, intercept = np.polyfit([x[0] for x in data2], [np.log(x[1]) for x in data2], 1)
print(f"slope: {slope}, intercept: {intercept}")
print(f"y = exp({intercept}) * exp({slope} * x)")
x2 = np.linspace(20, 50, 100)
y2 = np.exp(intercept) * np.exp(slope * x2)
plt.plot(x2, y2, label="Fit for the secound section")

x1 = np.linspace(5, 20, 100)
y1 = np.exp(-0.65)*np.exp(-0.015*(x1-20)**2)
plt.plot(x1, y1, label="Fit for the first section")

'''x3 = np.linspace(50, 65, 100)
y3 = np.exp(-9)*np.exp(0.004*x3**2)
plt.plot(x3, y3, label="Fit for the third section")'''
plt.plot([x[0] for x in data3], [x[1] for x in data3], '-', label="fit Section 3")

plt.legend()
plt.grid()
plt.yscale("log")
plt.xlabel("Amperage [A]")
plt.ylabel("Pressure [mbar]")
plt.savefig("../Graphics/Pressure_vs_Amperage.pdf")
plt.show()

print("-----------Calculation of the Power of the resistance-----------")
# Calculate the power of the resistance
R = 6.4 # Resistance Ohm
u_R = 0.01 # Ohm

u_I = 0.1 # A

data_Power_pressure = []
error_bars_Power_pressure = []
for set in data:
    P = set[0]**2 * R
    u_P = np.sqrt((set[0]**2*u_R)**2+ (2*set[0]*R*u_I)**2)
    data_Power_pressure.append((set[1], P))
    error_bars_Power_pressure.append(u_P)
    print(f"P: {P} +- {u_P}, with I: {set[0]} and P: {set[1]}")
    print("---------------")

print(data_Power_pressure)
print(error_bars_Power_pressure)

print("------------Fit the data with the function log(y) = a log(x) + b------------")
data_part_4 = []
for i in range(len(data_Power_pressure)):
    if data_Power_pressure[i][0] < 4:
        data_part_4.append(data_Power_pressure[i])

slope4, intercept4 = np.polyfit([np.log(x[0]) for x in data_part_4], [np.log(x[1]) for x in data_part_4], 1)
print(f"slope: {slope4}, intercept: {intercept4}")
print(f"y = exp({intercept4}) * x^{slope4}")
x4 = np.linspace(0.005, 4, 100)
y4 = np.exp(intercept4) * x4**slope4

data_fit = []
for i in range(len(x4)):
    data_fit.append((x4[i], y4[i]))

print("-----------Plot the data, Power of the resistance vs. Pressure-----------")

an.plot_data(data_Power_pressure, data2=data_fit, file_name="Power_of_resistance_vs_Pressure", error_bars=True, error_bars_data=error_bars_Power_pressure, lable_x="Pressure [mBar]", lable_y="Power of the resistance [W]", lable_daten="Power of the resistance", get_pdf=True, plot_fit=False, scale_x="log", scale_y="log")




