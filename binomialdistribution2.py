import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
n = 5
k = np.arange(0,4)
p = 0.7
prob = binom.pmf(k,n,p)
print(prob)
plt.figure(figsize=(10,6))
plt.bar(k,prob)
plt.show()