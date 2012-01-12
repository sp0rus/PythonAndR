#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import multivariate
import math

#read all the data in from the file
IND = np.loadtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
#sepallength = np.loadtxt('iris.data', delimiter=',', skiprows=0,usecols=[0])
#sepalwidth = np.loadtxt('iris.data', delimiter=',', skiprows=0,usecols=[1])
#petallength = np.loadtxt('iris.data', delimiter=',', skiprows=0,usecols=[2])
#petalwidth = np.loadtxt('iris.data', delimiter=',', skiprows=0,usecols=[3])
irisclass = []
for line in file('iris.data'):
    line = line.strip()
    curline = line.split(",")
    iristype = 0
    if curline[4] == 'Iris-setosa':
        iristype = 0
    elif curline[4] == 'Iris-versicolor':
        iristype = 1
    elif curline[4] == 'Iris-virginica':
        iristype = 2
    irisclass.append(iristype)
irisclass = np.array(irisclass)

DEP = np.array(irisclass).reshape(len(irisclass),1)
# sepal length and petal length
slpl = IND[0,2]
coeff = multivariate.multiRegression(IND, DEP)
fit = multivariate.estimatedFit(slpl, coeff)
slplrsquare = multivariate.adjustedRsquared(fit, DEP, slpl )
print "Regression coefficient: %s" %(coeff)
print "Adjusted R-square Value: %s" %(slplrsquare)

# sepal length and sepal width
#slpw = IND[]
#coeff = multivariate.multiRegression(sepallength, DEP)
#fit = multivariate.estimatedFit(slpw, coeff)
#slpwrsquare = multivariate.adjustedRsquared(fit, , )
#print "Regression coefficient: %s" %(coeff)
#print "Adjusted R-square Value: %s" %(slpwrsquare)

# sepal length, petal length, petal width
#slplpw = IND[]
#coeff = multivariate.multiRegression(, DEP)
#fit = multivariate.estimatedFit(slplpw, coeff)
#slplpwrsquare = multivariate.adjustedRsquared(fit, , )
#print "Regression coefficient: %s" %(coeff)
#print "Adjusted R-square Value: %s" %(slplpwrsquare)

# sepal length, sepal width, petal length, petal width
#slswplpw = IND[]
#coeff = multivariate.multiRegression(, DEP)
#fit = multivariate.estimatedFit(slswplpw, coeff)
#slswplpwrsquare = multivariate.adjustedRsquared(fit, , )
#print "Regression coefficient: %s" %(coeff)
#print "Adjusted R-square Value: %s" %(slswplpwrsquare)

#determine which r-square value was the best
#rsquares = [slpl, slpw, slplpw, slswplpw]
#combo = ['sepal length and petal length', 'sepal length and sepal width', 
#             'sepal length, petal length, petal width', 'sepal length, sepal width, petal length, petal width']

#best = 0
#best2 = ''

#i = 0
#while i < len(rsquares):
#    current = 1 - best
#    test = 1 - rsquares[i]
#    if test < current:
#	     best = rsquares[i]
#  	     best2 = iristypes[i]
#    i += 1

#print "The combination with the best adjusted R-squared value was %s with a %s value." %(best2, best)
