import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,4,5,6,7,8,9,10])
y = np.array([55,60,65,70,75,80,85,90])
a = np.cov(x,y)
print(a)
b = np.corrcoef(x,y)
print(b)