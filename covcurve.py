#assignment 20 covariance and correlation 2nd pair
import numpy as np
import matplotlib.pyplot as plt
a = np.array([0, 50, 100, 150, 200, 250, 300, 350])
b = np.array([60, 75, 88, 95, 92, 80, 65, 40])
cov = np.cov(a, b)[0, 1]
corr = np.corrcoef(a, b)[0, 1]
print("Covariance =", cov)
print("Correlation =", corr)
plt.figure(figsize=(6,4))
plt.plot(a, b,color="blue",linestyle="--",marker="s",markersize=5,linewidth=2,label="Dataset 2")
plt.xlabel("A")
plt.ylabel("B")
plt.title("Covariance and Correlation - Dataset 2")
plt.legend()
plt.grid(True)
plt.show()