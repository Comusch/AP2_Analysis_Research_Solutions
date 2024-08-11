import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
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

data_orignal4 = an.read_csv_file("MilikanMesswerte_Messreihe4.csv")
data4 = data_orignal4[1:]
print(data4)

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
u_eta_air = 0.2 * 10**(-6) # Pa*s
d = 0.006 # m
u_d = 0.00005 # m

u_U = 0.5 # V

A = 1.257
lambda_r = 72*10**(-9) # m

#calculation of the velocity
distance = (7.55 - 2.65)/9*10**(-3)*0.5
u_distance = 0.00005
u_time =0.05
data_velocity = []
for set in data:
    velocity = set[3]*distance/(set[2])
    u_velocity = np.sqrt((u_distance/set[2])**2 + (distance*set[3]/set[2]**2*u_time)**2)
    data_velocity.append((set[0], set[1], velocity, u_velocity))
print(data_velocity)

print("-----------Calculate and Convert the velocity-----------")
#convert and calculate the velocity for the second data set and the third data set
distance2 = 3.2*10**(-3)*0.5
data_velocity2 = []
Nr = len(data_velocity)
for set in data2:
    velocity = distance2/set[1]
    u_velocity = np.sqrt((u_distance/set[1])**2 + (distance2/set[1]**2*u_time)**2)
    print("u_velocity: ", u_velocity)

    velocity2 = distance2/set[2]
    u_velocity2 = np.sqrt((u_distance/set[2])**2 + (distance2/set[2]**2*u_time)**2)
    print("u_velocity2: ", u_velocity2)
    print("-------")
    data_velocity2.append((Nr, set[3], velocity, u_velocity))
    data_velocity2.append((Nr, set[3], velocity2, u_velocity2))
    Nr += 1
print(data_velocity2)

data_velocity3 = []
Nr = len(data_velocity) + len(data_velocity2)
for set in data3:
    velocity = set[0]/set[3]
    u_velocity = np.sqrt((u_distance / set[3]) ** 2 + (set[0] / set[3] ** 2 * u_time) ** 2)
    data_velocity3.append((Nr, set[1], velocity, u_velocity))
    velocity2 = set[0]/set[2]
    u_velocity2 = np.sqrt((u_distance/set[2])**2 + (set[0]/set[2]**2*u_time)**2)
    data_velocity3.append((Nr, set[1], velocity2, u_velocity2))
    Nr += 1
print(data_velocity3)

data_velocity4 = []
Nr = len(data_velocity) + len(data_velocity2) + len(data_velocity3)
for set in data4:
    velocity = 3*distance/set[2]
    u_velocity = np.sqrt((u_distance / set[2]) ** 2 + (3*distance / set[2] ** 2 * u_time) ** 2)
    data_velocity4.append((Nr, set[1], velocity, u_velocity))
    velocity2 = 3*distance/set[3]
    u_velocity2 = np.sqrt((u_distance/set[3])**2 + (3*distance/set[3]**2*u_time)**2)
    data_velocity4.append((Nr, set[1], velocity2, u_velocity2))
    Nr += 1
print(data_velocity4)

print("-----------Calculation of the radius and the charge-----------")

for set in data_velocity2:
    data_velocity.append(set)
for set in data_velocity3:
    data_velocity.append(set)
for set in data_velocity4:
    data_velocity.append(set)

#calculation of the radius and the charge for each set
data_calculated = []
for i in range(len(data_velocity)):
    if i%2 == 1:
        continue
    set1 = data_velocity[i]
    set2 = data_velocity[i+1]

    print("------")
    radius = 3/2 * np.sqrt(eta_air*(set1[2]+set2[2])/(density_delta*g))
    u_radius = 3/2 * np.sqrt((1/np.sqrt(eta_air*(set1[2]+set2[2])/(density_delta*g)) * 1/2 * eta_air*set1[3])**2 + (1/2 *eta_air*set2[3]/np.sqrt(eta_air*(set1[2]+set2[2])/(density_delta*g)))**2 + (1/2 * u_eta_air*(set1[2]+ set2[2])/np.sqrt(eta_air*(set1[2]+ set2[2])/(density_delta*g)))**2)
    print("velocity: ", set1[2], set2[2])
    print("u_velocity: ", set1[3], set2[3])
    print("eta_air: ", eta_air)
    print("u_eta_air: ", u_eta_air)
    print("u_radius: ", u_radius/radius)
    u_radius = 0.05 * radius

    korr_radius = np.sqrt(radius**2 + A**2*lambda_r**2/4)-A*lambda_r/2
    u_korr_radius = (radius*u_radius/np.sqrt(radius**2 + A**2*lambda_r**2/4))
    print("u_korr_radius: ", u_korr_radius/korr_radius)

    eta_korr = eta_air*(1+A*lambda_r/radius)**(-1)
    u_eta_korr = np.sqrt((u_eta_air*(1+A*lambda_r/radius)**(-1))**2 + (eta_air*(1+A*lambda_r/radius)**(-2)*A*lambda_r/radius**2*u_radius)**2)
    print("u_eta_korr: ", u_eta_korr/eta_korr)

    charge = 3*np.pi *d/set1[1]*eta_korr*korr_radius*(set2[2]- set1[2])*2
    u_charge = 3*np.pi *np.sqrt((d/set1[1]*eta_korr*(set2[2]- set1[2])*u_korr_radius)**2 + (d/set1[1]*u_eta_korr*korr_radius*(set2[2]-set1[2]))**2 + (u_d/set1[1]*eta_korr*korr_radius*(set2[2]-set1[2]))**2 + (d/set1[1]**2 *u_U*eta_korr*korr_radius*(set2[2]-set1[2]))**2 + (d/set1[1]*eta_korr*korr_radius*set1[3])**2 + (d/set1[1]*eta_korr*korr_radius*set2[3])**2)

    print("u_charge: ", u_charge/(10**(-19)), "10^-19 C")
    data_calculated.append((set1[0], radius, charge, u_charge))
print(data_calculated)

print("-----------Plotting the charge graphs-----------")
#Plotting the data
data_charge_numbered = []
for set in data_calculated:
    data_charge_numbered.append((set[0], set[2]/(10**(-19)), set[3]/(10**(-19))))
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
error_bars_data = []
for i in range(len(data_charge_numbered_sort)):
    finish_data.append((i, data_charge_numbered_sort[i][1]))
    error_bars_data.append(data_charge_numbered_sort[i][2])

print("-------Cut values--------")

end = []
error_bars_data_end = []

end2 = []
error_bars_data_end2 = []
for i in finish_data:
    if i[1] > 10:
        end2.append(i)
        error_bars_data_end2.append(error_bars_data[i[0]])
    else:
        end.append(i)
        error_bars_data_end.append(error_bars_data[i[0]])

end = np.array(end)
print(end)
print("-------Error bars--------")
print(error_bars_data_end)

print("--------End2--------")
end2 = np.array(end2)
print(end2)
print("-------Error bars--------")
print(error_bars_data_end2)



an.plot_data(end, "Charges_numbered_lower_numbers", lable_x="Index of trops", lable_y="Charge in 10⁻19", plot_fit=False, skal=1.7, error_bars=True, error_bars_data=error_bars_data_end)
an.plot_data(end2, "Charges_numbered_greater_numbers", lable_x="Index of trops", lable_y="Charge in 10⁻19", plot_fit=False, error_bars=True, error_bars_data=error_bars_data_end2)


print("-----------Clustering the charges-----------")
column = 1
X = end[:, column].reshape(-1, 1)  # Verwende nur die ausgewählte Spalte für das Clustering

# Führe das Clustering durch
dbscan = DBSCAN(eps=0.3, min_samples=2)  # Beispielsweise eps verkleinern, um mehr Cluster zu erhalten
labels = dbscan.fit_predict(X)

# Cluster-Labels anzeigen
print("Cluster Labels für jedes Datenpunkt:", labels)

# Visualisierung der Cluster
plt.scatter(end[:, 0], end[:, 1], c=labels, cmap='rainbow')
plt.xlabel('Index')
plt.ylabel('Charge in 10⁻19')
plt.title('Cluster der geclusterten Daten')
plt.grid()
plt.savefig('../Graphics/Cluster.pdf')
plt.show()

data_clustered = []
for i in range(len(end)):
    data_clustered.append((end[i][0], end[i][1], labels[i]))
print(data_clustered)

print("-----------Calculate the average charge for each cluster-----------")
# Calculate the average charge for each cluster
clusters = np.unique(labels)
average_charges = []
standard_deviation = []
for cluster in clusters:
    print(f"------------Cluster {cluster}:")
    if cluster == -1:
        continue
    charges = []
    for data_point in data_clustered:
        if data_point[2] == cluster:
            charges.append(data_point[1])
    average_charge = np.mean(charges)
    average_charges.append((cluster, average_charge))
    print(f"Cluster {cluster}: Durchschnittliche Ladung: {average_charge} * 10⁻¹⁹ C")
    standard_deviation.append(np.std(charges))
    print(f"Cluster {cluster}: Standardabweichung: {np.std(charges)} * 10⁻¹⁹ C")
    e_charge = average_charges/(cluster +1)
    e_charge_uncertainty = standard_deviation/(cluster +1)
    print("e_charge: ", e_charge)
    print("e_charge_uncertainty: ", e_charge_uncertainty)


