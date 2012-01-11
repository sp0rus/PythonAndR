#Notes
#January 10, 2012

###############################################################################

# Numpy functions we will be using in multiple regression analysis

np.array() # converts a python list to numpy array
np.reshape() # reshapes an array from one dimension set to another
    # by default: (1, n) -> (rows, columns), n is the number of elements
    #EXAMPLE: 
    a = np.array([1, 2, 3, 4])
    a.size(1,4)
    a.reshape(2,2)
    #[[1, 2],
    # [3, 4]]
    #//end example
np.zeros(r,c) # creates array of shape (r, c) filled with zeroes
np.ones(r,c) # creates array of shape (r, c) filled with ones
np.size() # returns the numbers of elements ( r by c )
np.dot(a, b) # a and b are matrices, multiply them together
np.sqrt() #
np.transpose() # converts an r, c matrix to a c, r matrix, flips along a diagonal
np.linalg.solve(a, b) # linear equation solver, solves ax = b, where a is a
                      # matrix and both b and x are vectors. solves for x
np.concatonate() # takes two matrices and combines them together

###############################################################################

# y = ax + b -> linear regression equation, y is dependent variable, x is
#   independent variable

# In multiple regression, there exists multiple independent variables and one
#   dependent variable

# y = a1x1 + a2x2 + a3x3 + ... + b

# At Ak = At b

# A -> independent variables with an additional column of ones
# At -> is transpose of A
# AtA -> is At times A
# b -> is our dependent variables
# Atb -> is At times b
# k -> is our unknown coefficient

###############################################################################

# multivariate.py

import numpy as np

def multiRegression(IDP, DEP):
    assert npssize(IDP[:, 0]) == np.size(DEP[:, 0])
    assert np.size(DEP[0, :] == 1
    records = np.size(IND[:, 0])
    IND = np.concatonate((IND, np.ones(records).reshape(records, 1), axis = 1)
    return np.linalg.solve(np.dot(IND.transpose(), IDP), np.dot(IND.transpose(), DEP.reshape(records, 1))

def estimatedFit(IND, coeff):
    records = np.size(IND[:, 0])
    IND = np.concatonate(IND, np.ones(records).reshape(records, 1), axis = 1)
    coeff = np.repeat(coeff.transpose(), record, axis = 0
    return np.sum(IND * coeff, axis = 1).reshape(records, 1)

def corr(FIT, Y):
    muFit = sum(FIT)/float(len(FIT))
    muy = sum(Y)/float(len(Y))
    X0 = FIT - muFit
    Y0 = Y - muy
    return sum(X0 * Y0)/np.sqrt(sum(X0 * X0) * sum(Y0 * Y0)
    
def adjustedRsquared(FIT, Y, variables):
    assert np.size(FIT) == np.size(Y)
    records = np.size(FIT[:, 0])
    muy = sum(Y)/float(len(Y))
    E = (Y - FIT) * (Y - FIT)
    YY = (Y - muy) * (Y - muy)
    return 1 - ((sum(E)/float(records-variables-1))/sum(YY)/float(records-1))
  
###############################################################################

# Round Robin

# Comparison of all subsets of variables, looking for the best adjusted R^2 values
