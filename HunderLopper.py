import numpy as np
import matplotlib.pyplot as plt

N = 2000
max_T = 30000

t = np.linspace(1, max_T, max_T)
N_A = np.empty(max_T )
N_B = np.empty(max_T )
N_A[0] = N

N_A_an = []
N_B_an = []

N_A_an.append(N)
N_B_an.append(0)

hopper = np.random.randint(0, high=N, size=max_T +1)
loppested = np.full(N, True)                                    # True = hund A, False = hund B

def N_A_analytisk(t):
    return N / 2 * (1 + np.exp(-2 * 1 / N * t))

for tid in range(1, max_T, 1):
    N_A_an.append(N_A_analytisk(tid))
    N_B_an.append(N - N_A_analytisk(tid))

    if loppested[hopper[tid]]:
        loppested[hopper[tid]] = False
        N_A[tid] = N_A[tid - 1] - 1
        N_B[tid] = N_B[tid - 1] + 1
    else:
        loppested[hopper[tid]] = True
        N_A[tid] = N_A[tid - 1] + 1
        N_B[tid] = N_B[tid - 1] - 1

fig, axarr = plt.subplots(1, 2)

axarr[0].set_title("Antall lopper numerisk")
axarr[0].set_ylabel("Antall lopper")
axarr[0].set_xlabel("Tid $[s]$")
axarr[0].plot(t, N_A, label="Antall lopper hund A")
axarr[0].plot(t, N_B, label="Antall lopper hund B")
axarr[0].legend()

axarr[1].set_title("Antall lopper analytisk")
axarr[1].set_ylabel("Antall lopper")
axarr[1].set_xlabel("Tid $[s]$")
axarr[1].plot(t, N_A_an, label="Antall lopper hund A")
axarr[1].plot(t, N_B_an, label="Antall lopper hund B")
axarr[1].legend()

plt.show()