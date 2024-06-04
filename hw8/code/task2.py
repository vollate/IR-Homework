import numpy as np
import matplotlib.pylab as plt


def log_odds(p):
    return np.log(p / (1 - p))


log_free = log_odds(0.3)
log_occ = log_odds(0.6)
log_prior = log_odds(0.5)

measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21) + log_prior
m = 10 * np.arange(21)

for z in measurements:
    i = z // 10
    if i + 3 <= len(l_m):
        l_m[0:i + 1] += log_free
        l_m[i + 1:i + 3] += log_occ
    elif i + 1 <= len(l_m):
        l_m[0:i + 1] += log_free
        l_m[i + 1:] += log_occ
    else:
        l_m += log_free


def odds_to_prob(l):
    return 1 - 1 / (1 + np.exp(l))


p_m = odds_to_prob(l_m)

plt.plot(m, p_m, marker='o')
plt.xlabel('Cell coordinate (cm)')
plt.ylabel('Belief')
plt.title('Task2')
plt.grid(True)
plt.show()
