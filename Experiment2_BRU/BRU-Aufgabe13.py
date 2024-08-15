import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt

# Load the data
print("--------------BRU Experiment 5--------------")
print("-----------Data loading-----------")
A = 3.16
u_A = 0.01
c2 = 1*(10**-6) # F
u_c2 = 0.05 *c2
w = 1000 *2*np.pi# Hz
u_w = 0.1 *np.pi

print("Calculate the capacity of the second condensator")

c1 = (10-A)/A * c2/(w**2*c2**2+1)
u_c1 = np.sqrt((10/A**2*u_A*c2/(w**2*c2**2+1))**2 + (2*w*c2**2*u_c2/(w**2*c2**2+1))**2)
print(f"C1: {c1} +- {u_c1}, with A: {A} and C2: {c2}")