
import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

print("--------------Load Data-----------")
data_orignal = an.read_csv_file("TRA-Aufgabe_3.csv")
data_orignal = data_orignal[1:]
print(data_orignal)

print("---------preparing the data---------")
data_amplitude = []
data_phase = []
for set in data_orignal:
    if set[2]*10**3/set[1] > 600:
       continue
    data_amplitude.append((set[0]*10**3, set[2]*10**3/set[1]))

    data_phase.append((set[0]*10**3, 2*np.pi-2*np.pi*set[0]*10**3*set[3]))

print("---------plot the data------------")
print("Plot amplitude:")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot(np.array(data_amplitude)[:, 0], np.array(data_amplitude)[:, 1], "o", label="Measurements values")
plt.legend()
plt.grid()
plt.xlabel("frequence in Hz")
plt.ylabel("A = u_a/u_e")
plt.xscale("log")
plt.savefig("../Graphics/Experiment6_amplitude_task_6.pdf")
plt.show()

print("Plot phase:")
fig, ax = plt.subplots(figsize=(8, 8))
plt.plot(np.array(data_phase)[:, 0], np.array(data_phase)[:, 1], "o", label="Measurements values")
plt.legend()
plt.grid()
plt.xlabel("frequence in Hz")
plt.ylabel("phase shift")
plt.xscale("log")
plt.savefig("../Graphics/Experiment6_phase_task_6.pdf")
plt.show()
