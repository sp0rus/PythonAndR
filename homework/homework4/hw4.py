#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def linreg(X, Y):
    assert len(X)==len(Y)
    n = len(X)
    EX = sum(X)
    EY = sum(Y)
    EX2 = sum([x*x for x in X])
    EXY = sum([ X[i] * Y[i] for i in range(n)])
    m = int((n*EXY - EX*EY) / (n*EX2 - EX*EX))
    b = int((EY - m*EX) / n)
    return (m, b)

#assign the file to a variable
filename = "Tax_Year_2007_County_Income_Data.csv"

returns = []
exemptions = []

#assign some variables for use later
i = 0 #counter to skip the first line

#loop through the file
for line in file(filename):
    #skip the first line
    if i != 0:
        #clean the data and make each line into a list to parse
        curline = line.strip()
        curline = curline.replace("$","")
        curlinelist = curline.split(",")
        
        #append the county's average gross income to the list
        if curlinelist[1] != 0:
            pop = int(curlinelist[4])
            returns.append(pop)
            exemptions.append(int(curlinelist[5]))
    i = i + 1

print "(Slope, Y-Intercept): %s \n" %(linreg(returns, exemptions),)

(m, b) = linreg(returns, exemptions)
X = np.linspace(min(returns), max(returns))
Y = X * m + b

#figuring out the LA County/Cook County question
lacr = 8405456 #LA County returns
lace = 4005895 #LA County Exemptions
ccr = 4754875 #Cook County returns
cce = 2350974 #Cook county exemptions

laccr = [lacr,ccr] #list with returns from both counties
lacce = [lace,cce] #list with exemptions from both counties

(m2, b2) = linreg(laccr,lacce) # compute linear regression for the counties, to get the slope and y-intercept
lay = m2 * (lacr - 1000000) + b2 #compute the expected exemption number for LA County
ccy = m2 * (ccr + 1000000) + b2 #compute the expected exemption number for Cook County

print "Expected number of exemptions filed if 1,000,000 people move from Los Angeles County to Cook County:"
print "Los Angeles County: %s" %(lay)
print "Cook County: %s" %(ccy)

# plot the number of returns filed and number of exemptions
plt.plot(returns, exemptions, "r+")
plt.plot(X, Y, "b-")

plt.show()
