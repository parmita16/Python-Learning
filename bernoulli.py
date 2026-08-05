from scipy.stats import bernoulli
p=0.7
p1=bernoulli.cdf(k=1,p=0.7)
p2=bernoulli.cdf(k=0,p=0.7)
p3=bernoulli.cdf(k=2,p=0.7)
print(p1,p2,p3)