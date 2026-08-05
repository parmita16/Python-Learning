import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
n = 10
k = np.arange(0,n+1)
p = 0.5
prob = binom.pmf(k,n,p)
print(prob)
plt.figure(figsize=(10,6))
plt.bar(k,prob)
plt.show()