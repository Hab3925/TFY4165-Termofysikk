from cProfile import label
import matplotlib.pyplot as plt 
import numpy as np

stefan_boltzmann = 5.67e-8

def stefanboltzmannslov(T):
    return stefan_boltzmann * T**4 * 10

x = np.linspace(1800, 2800, 100)

stefan_boltzmann_verdier = []

for i in x:
    stefan_boltzmann_verdier.append(stefanboltzmannslov(i))


målt_intensitet = np.array([0.5, 0.73, 0.96, 1.26, 1.60, 1.92]) * 1.5 * 10e6
målt_temp = [1910, 2090, 2250, 2340, 2500, 2620]

plt.figure(1)
plt.title("Målt intensitet plottet mot Stefan-Boltzmanns lov")
plt.xlabel("Temperatur Wolframtråd [$K$]")
plt.ylabel("Utsendt intensitet [$W / cm^2$]")
plt.plot(x, stefan_boltzmann_verdier, label="Stefan-boltzmanns lov")
plt.errorbar(målt_temp, målt_intensitet, yerr=0.05* 10e6, label="Målte verdier")
plt.legend()
plt.grid()
plt.show()