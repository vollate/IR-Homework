import numpy as np
import matplotlib.pylab as plt


def log_inv_sensor_model(z, c):
    if c > z:
        return np.log(0.6 / 0.4)
    else:
        return np.log(0.3 / 0.7)


measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21)
m = 10 * np.arange(21)

for z in measurements:
    for i in range(len(m)):
        if m[i] > z + 20:
            continue
        l_m[i] += log_inv_sensor_model(z, m[i])


def odds_to_prob(l):
    return 1 - 1 / (1 + np.exp(l))


p_m = odds_to_prob(l_m)

plt.plot(m, p_m, marker='o')
plt.xlabel('Cell coordinate (cm)')
plt.ylabel('Belief')
plt.title('Task1')
plt.grid(True)
plt.show()
