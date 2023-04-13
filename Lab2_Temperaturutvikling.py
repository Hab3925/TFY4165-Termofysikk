import matplotlib.pyplot as plt
import numpy as np

T_c = [12.0, 10.4, 9.1, 7.2, 6.0, 4.5, 3.6, 2.5, 1.4, 1.1, 1.2, 1.2]
T_h = [17.8, 19.7, 21.6, 24.0, 25.6, 27.4, 29.0, 30.5, 32.1, 33.3, 35.0, 36.2]

x = np.linspace(0, 26, 12)

plt.title("Temperaturutvikling")
plt.ylabel("Temperatur [°C]")
plt.xlabel("Tid [m]")
line1 = plt.errorbar(x, T_c, yerr=0.5, xerr=0.1)
line2 = plt.errorbar(x, T_h, yerr=0.5, xerr=0.1)

plt.legend([line1, line2], ["T_c", "T_h"])
plt.show()