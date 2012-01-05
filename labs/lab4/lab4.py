#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#read the dataset
AAPL = np.loadtxt("aapl.csv", skiprows=1, delimiter=',', usecols=[6])
MSFT = np.loadtxt("msft.csv", skiprows=1, delimiter=',', usecols=[6])

#reverse the dataset
AAPL = AAPL[::-1] # same syntax for numpy and python
MSFT = MSFT[::-1]

#linear transformation
AAPL_linear = AAPL[-232:] #just look at the last year
MSFT_linear = MSFT[-232:]

AAPL_linear = (AAPL_linear - min(AAPL_linear))/(max(AAPL_linear) - min(AAPL_linear))
MSFT_linear = (MSFT_linear - min(MSFT_linear))/(max(MSFT_linear) - min(MSFT_linear))

AAPL_linear -= AAPL_linear[0]
MSFT_linear -= MSFT_linear[0]

plt.plot(AAPL_linear,'g-')
plt.plot(MSFT_linear,'r-')
plt.show()
