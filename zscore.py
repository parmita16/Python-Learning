#assignment 20 z score
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
mcq1 = np.array([
9,6,10,11,12,9,10,9,7,7,10,13,
12,9,10,6,8,11,8,12,9,11,15,9,9,9
])
mcq2 = np.array([
15.5,14.5,11,12.5,9.5,11.5,14.5,8,
13.5,10,6.5,11,13.5,14.5,9,12.5,
15.5,13.5,14.5,8,15,9.5,16.5,14.5,14
])
mcq4 = np.array([
7,5,3,12,6,8,11,6,5,7,8,9,
10,5,10,9,15,7,10,10,12,14,7,10,7,13
])
parmita_marks = [12, 13.5, 9]
z1 = (12 - np.mean(mcq1)) / np.std(mcq1)
z2 = (13.5 - np.mean(mcq2)) / np.std(mcq2)
z3 = (9 - np.mean(mcq4)) / np.std(mcq4)
print("Parmita's Z-Scores")
print("MCQ-1:", z1)
print("MCQ-2:", z2)
print("MCQ-4:", z3)
x = [1, 2, 3]
y = [z1, z2, z3]
plt.figure(figsize=(6,4))
plt.plot(x, y,color="blue",linestyle=":",marker="s",markersize=5,linewidth=2,label="Z-Score")
plt.xticks([1,2,3], ["MCQ-1", "MCQ-2", "MCQ-4"])
plt.xlabel("MCQ")
plt.ylabel("Z-Score")
plt.title("Parmita Rajthala's Z-Scores")
plt.legend()
plt.grid(True)
plt.show()