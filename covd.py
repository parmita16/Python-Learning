#assignment 20 covariance and correlation 3rd pair
import numpy as np
import matplotlib.pyplot as plt
a = np.array([2, 4, 5, 6, 7, 8, 9, 10])
b = np.array([90, 85, 80, 75, 70, 65, 60, 55])
cov = np.cov(a, b)[0, 1]
corr = np.corrcoef(a, b)[0, 1]
print("Covariance =", cov)
print("Correlation =", corr)
plt.figure(figsize=(6,4))
plt.plot(a, b,color="green",linestyle=":",marker="^",markersize=5,linewidth=2,label="Dataset 3")
plt.xlabel("A")
plt.ylabel("B")
plt.title("Covariance and Correlation - Dataset 3")
plt.legend()
plt.grid(True)
plt.show()