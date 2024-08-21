import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

print("---------------Load Data---------------")
data = an.read_csv_file("Experiment5_task_2.csv")
data = data[1:]
print(data)

print("---------------prepare Data---------------")
data_phase = []
for set in data:
    data_phase.append((set[3], set[2]))
print(data_phase)

data_amplitude = []
for set in data:
    data_amplitude.append((set[3], set[1]))

print("---------------Plot Data---------------")
fig, ax = plt.subplots(figsize=(8, 8))

plt.plot((np.array(data_phase)[:, 0]), (np.array(data_phase)[:, 1]), label="Phase")
plt.grid()
plt.legend()
plt.savefig("../Graphics/Experiment5_2_phase.pdf")
plt.show()

