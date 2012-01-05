#!/usr/bin/env/python

import matplotlib.pyplot as plt
import numpy as np

def linreg(X,Y):
    assert len(X) == len(Y)
    n = len(X)
    EX = sum(X)
    EY = sum(Y)
    EX2 = sum(X*X)
    EXY = sum(X*Y)
    m = (n * EXY - EX * EY)/(n * EX2 - EX * EX)
    b = (EY - m * EX)/float(n)
    return(m,b)
    
#read the dataset
AAPL = np.loadtxt("aapl.csv", skiprows=1, delimiter=',', usecols=[6])
MSFT = np.loadtxt("msft.csv", skiprows=1, delimiter=',', usecols=[6])

#reverse the dataset
AAPL = AAPL[::-1] # same syntax for numpy and python
MSFT = MSFT[::-1]

#linear transformation
AAPL_linear = AAPL[-232:] #just look at the last year
MSFT_linear = MSFT[-232:]

(m,b) = linreg(AAPL_linear, MSFT_linear)

x = np.linspace(min(AAPL_linear),max(AAPL_linear),232)
y = m * x + b

yhat = m * AAPL_linear + b

R = sum(AAPL_linear * MSFT_linear)/np.sqrt(sum(MSFT_linear**2)*sum(yhat**2))
print "R: ", R

Rsqrd = R*R
print "R squared: ", Rsqrd

plt.plot(AAPL_linear, MSFT_linear, 'r+')
plt.plot(x,y,'b-')
plt.show()
