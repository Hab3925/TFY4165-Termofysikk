import matplotlib.pyplot as plt 
import numpy as np

stefan_boltzmann = 5.67e-8

svart = [2.66, 3.98, 5.78, 7.92]
hvit = [2.06, 4.01, 5.36, 7.58]
blank = [0.50, 0.35, 0.38, 0.43]
grå = [1.05, 1.64, 1.94, 2.60]

x = [42.3, 47.5, 58.5, 68.5]

line1 = plt.errorbar(x, svart, yerr=0.05, color="black")
line2 = plt.errorbar(x, hvit, yerr=0.05, color="red")
line3 = plt.errorbar(x, blank, yerr=0.05, color="green")
line4 = plt.errorbar(x, grå, yerr=0.05, color="grey")

plt.title("Utsendt stråling fra ulike overflater på leslies kuben")
plt.xlabel("Temperatur Leslies Kube [˚C]")
plt.ylabel("Spenning strålingssensor [mV]")

plt.legend([line1,line2,line3,line4], ["Svart", "Hvit", "Blank", "grå"])
plt.grid()
plt.show()