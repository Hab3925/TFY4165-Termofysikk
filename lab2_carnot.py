import matplotlib.pyplot as plt
import numpy as np

Kelvin = 273.15
T_c = [12.0, 10.4, 9.1, 7.2, 6.0, 4.5, 3.6, 2.5, 1.4, 1.1, 1.2, 1.2]
T_h = [17.8, 19.7, 21.6, 24.0, 25.6, 27.4, 29.0, 30.5, 32.1, 33.3, 35.0, 36.2]

def carnot(T_h, T_c):
    return (T_h + Kelvin)/ ((T_h + Kelvin) - (T_c + Kelvin))

x = np.linspace(0, 26, 12)

carnotPlot = []

for i in range(len(x)):
    carnotPlot.append(carnot(T_h[i], T_c[i]))

plt.title("Utvikling av virkningsgrad carnot maskin")
plt.ylabel("Virkningsgrad")
plt.xlabel("Tid [m]")
line1 = plt.errorbar(x, carnotPlot, yerr=0.01)

plt.legend([line1], ["Virkningsgrad"], loc="upper left")
plt.show()