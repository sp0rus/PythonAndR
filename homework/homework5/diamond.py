import numpy as np
import matplotlib.pyplot as plt
import bivariate
import math

carat = np.loadtxt('diamond.tab', delimiter='\t', skiprows=1,usecols=[0])
price = np.loadtxt('diamond.tab', delimiter='\t', skiprows=1,usecols=[1])

data = zip(carat, price) #sort
data.sort()
(carat, price) = zip(* data) # unzip
bivariate.bivariate(carat,price)

plt.plot(carat, price, 'k+')
plt.xlabel("Carats")
plt.ylabel("Price")
plt.title("Price of Diamonds by Carat")
plt.show()
