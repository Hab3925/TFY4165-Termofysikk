import matplotlib.pyplot as plt
import numpy as np

c = 4.2e3
m_h = 4
P = 94
dt = 150

T_h = [17.8, 19.7, 21.6, 24.0, 25.6, 27.4, 29.0, 30.5, 32.1, 33.3, 35.0, 36.2]

def virkningsgrad(dT_h):
    return c * m_h * dT_h / (P * dt)

virkningsgrader = []
forrigeT = 16
for T in T_h:
    virkningsgrader.append(virkningsgrad(T - forrigeT))
    forrigeT = T

x = np.linspace(0, 26, 12)

plt.title("Utvikling av virkningsgrad")
plt.ylabel("Virkningsgrad ")
plt.xlabel("Tid [m]")
line1 = plt.errorbar(x, virkningsgrader, yerr=0.05)

plt.legend([line1], ["Virkningsgrad"])
plt.show()