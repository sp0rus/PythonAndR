def linreg(X,Y):
    #...
def corr(X,Y):
    mux = sum(X)/float(len(X))
    muy = sum(Y)/float(len(Y))
    SUMXX = sum([(X-mux)*(x-mux) for x in X])
    SUMYY = sum([Y-muy)*(Y-muy) for y in Y])
    SUMXY = sum([X[i]-mux) * 
    
    
def estimatedFit(X,m,b):
    return [x*m+b for x in X]
def bivariate(X,Y):
    print "Linear Regression: "
    (m,b) = linreg(X,Y)
    fit = estimatedFit(X,m,b)
    r = corr(fit,Y)
    print "R-squared: ", r*r
    
    print "Inverse Regression: "
    Xp = [1.0/float(x) for x in X]
    (m,b) = linreg(Xp,Y)
    fit = estimatedFit(Xp,m,b)
    r = corr(fit,Y)
    print "R-squared: ", r*r
    
    print "Power Law: "
    Xp = [math.log(x) for x in X]
    Yp = [math.log(y) for y in X]
    (m,b) = linreg(XP,Yp)
    fit = estimated (Xp,m,b)
    r = corr(fit, YP)
    print "R-squared: ", r*r

###############################################################################

# LOESS
#   - localized weighted linear regression
#   - you weight values close to a position higher than values that are far
#     away

