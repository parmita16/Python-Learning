#Q2. Normal Distribution
import numpy as np
import matplotlib.pyplot as plt

mean = 50
std = 10

x = np.linspace(10, 90, 20)

y = (1 / (std * np.sqrt(2 * np.pi))) * \
    np.exp(-0.5 * ((x - mean) / std) ** 2)

print("Normal Distribution")
print("Mean =", mean)
print("Standard Deviation =", std)

plt.figure(figsize=(10, 5))

plt.bar(x, y, width=3,label="Bar Graph")

plt.plot(x, y, marker='o', label="Line Graph")

plt.xlabel("X")
plt.ylabel("Probability Density")
plt.title("Normal Distribution")
plt.legend()

plt.show()

plt.plot(x, y, marker='o')

plt.xlabel("X")
plt.ylabel("Probability Density")
plt.title("Uniform Distribution")

plt.show()