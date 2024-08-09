import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
print("Millicanversuch")
print("-----------Data loading-----------")
data_orignal = an.read_csv_file("Millicanversuch.csv")
print(data_orignal)

data = data_orignal[1:]

print(data)

data_orignal2 = an.read_csv_file("ESE_Millican_2.csv")
data2 = data_orignal2[1:]
print(data2)

data_orignal3 = an.read_csv_file("Millikan_Versuch3.csv")
data3 = data_orignal3[1:]
print(data3)

print("-----------Initial the constants-----------")
#precalculation of the values
temperature = 24.5 # °C
pressure_orignal_air = 722 # mmHg
pressure_air = pressure_orignal_air * 133.322 # Pa
print("pressure_air: ", pressure_air)

density_air = 1.225 # kg/m^3
density_oel = 871 # kg/m^3
density_delta = density_oel - density_air # kg/m^3
g = 9.81 # m/s^2
eta_air = 17.2 * 10**(-6) # Pa*s
d = 0.006 # m
u_d = 0.00005 # m

A = 1.257
lambda_r = 72*10**(-9) # m

#calculation of the velocity
distance = (7.55 - 2.65)/9*10**(-3)*0.5
data_velocity = []
for set in data:
    velocity = set[3]*distance/(set[2])
    data_velocity.append((set[0], set[1], velocity))
print(data_velocity)

print("-----------Calculate and Convert the velocity-----------")
#convert and calculate the velocity for the second data set and the third data set
distance2 = 3.2*10**(-3)*0.5
data_velocity2 = []
Nr = len(data_velocity)
for set in data2:
    velocity = distance2/set[1]
    velocity2 = distance2/set[2]
    data_velocity2.append((Nr, set[3], velocity))
    data_velocity2.append((Nr, set[3], velocity2))
    Nr += 1
print(data_velocity2)

data_velocity3 = []
Nr = len(data_velocity) + len(data_velocity2)
for set in data3:
    velocity = set[0]/set[3]
    data_velocity3.append((Nr, set[1], velocity))
    velocity2 = set[0]/set[2]
    data_velocity3.append((Nr, set[1], velocity2))
    Nr += 1
print(data_velocity3)

print("-----------Calculation of the radius and the charge-----------")

for set in data_velocity2:
    data_velocity.append(set)
for set in data_velocity3:
    data_velocity.append(set)

#calculation of the radius and the charge for each set
data_calculated = []
for i in range(len(data_velocity)):
    if i%2 == 1:
        continue
    set1 = data_velocity[i]
    set2 = data_velocity[i+1]
    radius = 3/2 * np.sqrt(eta_air*(set1[2]+set2[2])/(density_delta*g))
    korr_radius = np.sqrt(radius**2 + A**2*lambda_r**2/4)-A*lambda_r/2
    eta_korr = eta_air*(1+A*lambda_r/radius)**(-1)
    charge = 3*np.pi *d/set1[1]*eta_korr*korr_radius*(set2[2]- set1[2])*2
    data_calculated.append((set1[0], radius, charge))
print(data_calculated)

print("-----------Plotting the charge graphs-----------")
#Plotting the data
data_charge_numbered = []
for set in data_calculated:
    data_charge_numbered.append((set[0], set[2]/(10**(-19))))
print(data_charge_numbered)

print("Cut messdate form the diagramm to see the different charges better")
# cut charge greater than 10e
for i in data_charge_numbered:
    if i[1] >= 10:
        data_charge_numbered.remove(i)
        print(i)
    if i[1] < 0.5:
        data_charge_numbered.remove(i)
        print(i)

data_charge_numbered = np.array(data_charge_numbered)
print(data_charge_numbered)

#sort data_charge_numbered by the second column
data_charge_numbered_sort = data_charge_numbered[data_charge_numbered[:, 1].argsort()]
print(data_charge_numbered_sort)

finish_data = []
for i in range(len(data_charge_numbered_sort)):
    finish_data.append((i, data_charge_numbered_sort[i][1]))

print("-------Cut values--------")

end = []
for i in finish_data:
    if i[1] > 0.5 and i[1] < 10:
        end.append(i)

end = np.array(end)
print(end)



an.plot_data(end, "Charges_numbered", lable_x="Index of trops", lable_y="Charge in 10⁻19", plot_fit=False, skal=1.7)
print("elementary charge: ", 1.7, "10^-19 C")




