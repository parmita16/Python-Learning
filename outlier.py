import matplotlib.pyplot as plt
import numpy as np
b= np.array([1,2,3,4,5,6,7])
a = np.array([1,12,13,14,15,17,25])
q1 = np.percentile(a,25)
median = np.percentile(a,50)
q3 = np.percentile(a,75)
iqr = q3 - q1
print(q1)
print(median)
print(q3)
print(iqr)
lowerfence =q1 - 1.5 * iqr
upperfence =q3 + 1.5 * iqr
print(lowerfence)
print(upperfence)
outlier_mask = (a<lowerfence)|(a>upperfence)
print(outlier_mask)
outlier_data = a[outlier_mask]
print(f"outlier data are = {outlier_data}")
clean_data = a[~outlier_mask]
print(f"Clean data is {clean_data}")
plt.scatter(b[outlier_mask],outlier_data,color="red",label = "outlier")
plt.scatter(b[~outlier_mask],clean_data,color="purple",label = "Cleandata")
plt.axhline(q1,color="yellow",label="1st Quartile")
plt.axhline(q3,color="blue",label="3rd Quartile")
plt.axhline(lowerfence,color="blue",linestyle=":",label="lowerfence")
plt.axhline(upperfence,color="yellow",linestyle=":",label="upperfence")
plt.legend()
plt.show()
