#assignment 19 kurtosis
from scipy.stats import gaussian_kde, kurtosis
import matplotlib.pyplot as plt
import numpy as np
a = np.array([4.2, 5.1, 4.8, 5.5, 4.9, 5.0, 5.3, 4.7, 5.2,
              4.6, 5.4, 5.1, 4.9, 5.0, 5.2, 4.8, 5.3, 4.7, 5.1])
b = np.array([5.0, 5.1, 4.9, 5.0, 5.05, 4.95, 5.0, 5.02, 4.98,
              5.0, 5.01, 4.99, 5.0, 2.0, 8.0, 1.5, 8.5, 5.0, 5.0, 5.0])
c = np.array([3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0,
              3.2, 3.8, 4.2, 4.8, 5.2, 5.8, 6.2, 6.8, 7.2])
k_a = kurtosis(a)
k_b = kurtosis(b)
k_c = kurtosis(c)
print("Kurtosis of A:", k_a)
print("Kurtosis of B:", k_b)
print("Kurtosis of C:", k_c)
g_a = gaussian_kde(a)
g_b = gaussian_kde(b)
g_c = gaussian_kde(c)
plt.figure(figsize=(9,6))
xa = np.linspace(min(a)-2, max(a)+2, 500)
ya = g_a(xa)
xb = np.linspace(min(b)-2, max(b)+2, 500)
yb = g_b(xb)
xc = np.linspace(min(c)-2, max(c)+2, 500)
yc = g_c(xc)
plt.plot(xa, ya, color="magenta", label="A (Mesokurtic)")
plt.plot(xb, yb, color="darkgreen", label="B (Leptokurtic)")
plt.plot(xc, yc, color="orange", label="C (Platykurtic)")
plt.xlabel("X Value")
plt.ylabel("Density")
plt.title("Kurtosis")
plt.legend(loc="best")
plt.grid(True)
plt.show()