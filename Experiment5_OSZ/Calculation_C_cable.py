import numpy as np

f_0 = 47.7*10**3 #Hz
u_f_0 = 0.05*10**3 #Hz

f_c = 44.44*10**3 #Hz
u_f_c = 0.05*10**3 #Hz

L = 1.8*10**(-3) #H
u_L = 0.05 * L

c_c = 1/((np.pi*2*f_c)**2*L) - 1/((np.pi*2*f_0)**2*L)
u_c = np.sqrt((1/((f_c*2*np.pi)**3*L)*(-2)*2*np.pi*u_f_c)**2 + (-1/((f_0*2*np.pi)**3*L)*(-2)*2*np.pi*u_f_0)**2 + (-1/((f_c*2*np.pi)**2*L**2) + 1/((f_c*2*np.pi)**2*L**2))**2*u_L**2)

print(f"C_c:{c_c}+- {u_c} F")

c_c_pro_meter = c_c/10
u_c_c_pro_meter = u_c/10
print(f"C_c pro Meter:{c_c_pro_meter} +- {u_c_c_pro_meter} F/m")
