import matplotlib.pyplot as plt
import math

def linreg(X, Y):
    assert len(X)==len(Y)
    n = len(X)
    EX = sum(X)
    EY = sum(Y)
    EX2 = sum([x * x for x in X])
    EXY = sum([ X[i] * Y[i] for i in range(n)])
    m = (n * EXY - EX * EY) / (n * EX2 - EX * EX)
    b = (EY - m * EX) / float(n)
    return (m, b)
                                    
def corr(X, Y):
    mux = sum(X)/float(len(X))
    muy = sum(Y)/float(len(Y))
    SUMXX = sum([(x - mux) * (x - mux) for x in X])
    SUMYY = sum([(y - muy) * (y - muy) for y in Y])
    SUMXY = sum([(X[i] - mux) * (Y[i] - muy) for i in range(len(X))])
    return SUMXY/(SUMXX * SUMYY)**0.5
    
def estimatedFit(X, m, b):
    return [x * m + b for x in X]

def bivariate(X, Y):
    print "Linear Regression: "
    print "Plot color: blue"
    (m, b) = linreg(X, Y)
    fit = estimatedFit(X, m, b)
    r = corr(fit, Y)
    print "M: %s" %(m)
    print "B: %s" %(b)
    print "R-squared: ", r*r
    plt.plot(X, fit, "b-")
    
    # y = (a/x)+b -> 1/X
    print "\nInverse Regression: "
    print "Plot color: red"
    Xp = [1.0/float(x) for x in X]
    (m,b) = linreg(Xp, Y)
    fit = estimatedFit(Xp, m, b)
    r = corr(fit, Y)
    print "M: %s" %(m)
    print "B: %s" %(b)
    print "R-squared: ", r*r
    plt.plot(X, fit, "r-")

    # y = x^m + b    
    print "\nPower Law: "
    print "Plot color: green"
    Xp = [math.log(x) for x in X]
    Yp = [math.log(y) for y in Y]
    (m,b) = linreg(Xp, Yp)
    fit = estimatedFit(Xp, m, b)
    r = corr(fit, Yp)
    print "M: %s" %(m)
    print "B: %s" %(b)
    print "R-squared: ", r*r
    plt.plot(X, [math.exp(y) for y in fit], "g-")
    
    # y = a*sqrt(x)+b -> X*X
    print "\nSquare root: "
    print "Plot color: magenta"
    Xp = [math.sqrt(x) for x in X]
    (m,b) = linreg(Xp, Y)
    fit = estimatedFit(Xp, m, b)
    r = corr(fit, Y)
    print "M: %s" %(m)
    print "B: %s" %(b)
    print "R-squared: ", r*r
    plt.plot(X, fit, 'm-')
    
    # y = a*log(x)+b -> e^X           
    print "\nLogarithm: "
    print "Plot color: cyan"
    Xp = [math.log(x) for x in X]
    (m,b) = linreg(Xp, Y)
    fit = estimatedFit(Xp, m, b)
    r = corr(fit, Y)
    print "M: %s" %(m)
    print "B: %s" %(b)
    print "R-squared: ", r*r
    plt.plot(X, fit, 'c-')
