import numpy as np
import matplotlib . pyplot as plt

R = 1000 # Ohms
C = 10e-6 # Farads
V = 5 # Volts


t = np . linspace (0 , 0.05 , 1000) # Increased time range to better visualize discharge
Vc = V * np . exp ( - t / (R * C ) ) # Discharging capacitor formula

plt . plot (t , Vc )
plt . xlabel (" Time (s)")
plt . ylabel (" Voltage (V)")
plt . title ("RC Discharging Curve ")
plt . show ()
