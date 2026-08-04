#assignment 20 covariance and correlation 1st pair
import numpy as np
import matplotlib.pyplot as plt
a = np.array([2, 4, 5, 6, 7, 8, 9, 10])
b = np.array([55, 60, 65, 70, 75, 80, 85, 90])
cov = np.cov(a, b)[0, 1]
corr = np.corrcoef(a, b)[0, 1]
print("Covariance =", cov)
print("Correlation =", corr)
plt.figure(figsize=(6,4))
plt.plot(a, b,color="red",linestyle="-",marker="o",markersize=5,linewidth=2,label="Dataset 1")
plt.xlabel("A")
plt.ylabel("B")
plt.title("Covariance and Correlation - Dataset 1")
plt.legend()
plt.grid(True)
plt.show()