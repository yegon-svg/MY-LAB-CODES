import numpy as np
import matplotlib.pyplot as plt

R = 1000 # Ohms
C = 1e-6 # Farads
V = 5 # Volts

t = np.linspace(0, 0.01, 1000)
Vc = V * np . exp ( - t / (R * C ) ) 
        
plt.plot(t, Vc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC dis Charging Curve")
plt.show()
