import numpy as np

f_0 = 47.7*10**3 #Hz
u_f_0 = 0.1*10**3 #Hz

f_c = 44.44*10**3 #Hz
u_f_c = 0.1*10**3 #Hz

L = 1.8*10**(-3) #H

c_c = 1/((np.pi*2*f_c)**2*L) - 1/((np.pi*2*f_0)**2*L)
print(f"C_c:{c_c} F")

c_c_pro_meter = c_c/10
print(f"C_c pro Meter:{c_c_pro_meter} F/m")
