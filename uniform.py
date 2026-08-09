#Q. Uniform Distribution
import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 20

x = np.linspace(5, 25, 20)

y = np.zeros(len(x))

for i in range(len(x)):
    if x[i] >= a and x[i] <= b:
        y[i] = 1 / (b - a)

print("Uniform Distribution")
print("Minimum =", a)
print("Maximum =", b)
print("Probability Density =", 1 / (b - a))

plt.figure()

plt.bar(x, y)

plt.plot(x, y, marker='o')

plt.xlabel("X")
plt.ylabel("Probability Density")
plt.title("Uniform Distribution")

plt.show()