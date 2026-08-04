import numpy as np
import matplotlib.pyplot as plt
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
p40_1 = np.percentile(mcq1, 40)
p60_1 = np.percentile(mcq1, 60)
p80_1 = np.percentile(mcq1, 80)
print("MCQ-1")
print("40th Percentile =", p40_1)
print("60th Percentile =", p60_1)
print("80th Percentile =", p80_1)
p40_2 = np.percentile(mcq2, 40)
p60_2 = np.percentile(mcq2, 60)
p80_2 = np.percentile(mcq2, 80)
print("\nMCQ-2")
print("40th Percentile =", p40_2)
print("60th Percentile =", p60_2)
print("80th Percentile =", p80_2)
p40_4 = np.percentile(mcq4, 40)
p60_4 = np.percentile(mcq4, 60)
p80_4 = np.percentile(mcq4, 80)
print("\nMCQ-4")
print("40th Percentile =", p40_4)
print("60th Percentile =", p60_4)
print("80th Percentile =", p80_4)
x = [1,2,3]
plt.figure(figsize=(6,4))
plt.plot(x, [p40_1,p60_1,p80_1],color="red",marker="o",linestyle="-",linewidth=2,label="MCQ-1")
plt.plot(x, [p40_2,p60_2,p80_2],color="blue",marker="s",linestyle="--",linewidth=2,label="MCQ-2")
plt.plot(x, [p40_4,p60_4,p80_4],color="green",marker="^",linestyle=":",linewidth=2,label="MCQ-4")
plt.xlabel("Percentiles (1 = 40%, 2 = 60%, 3 = 80%)")
plt.ylabel("Marks")
plt.title("Percentile Comparison")
plt.legend()
plt.grid(True)