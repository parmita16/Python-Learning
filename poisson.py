#Q1. Poisson Distribution
import numpy as np
import matplotlib.pyplot as plt

lam = 5

x = np.arange(0, 16)

factorial = []

for i in x:
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    factorial.append(fact)

factorial = np.array(factorial)

p = (np.exp(-lam) * (lam ** x)) / factorial

print("Poisson Distribution")
print("Lambda =", lam)

for i in range(len(x)):
    print("X =", x[i], "P(X) =", p[i])

plt.figure()

plt.bar(x, p)

plt.plot(x, p, marker='o')

plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.title("Poisson Distribution")

plt.show()