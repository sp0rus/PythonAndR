import numpy as np

def multiRegression(IDP, DEP):
    assert np.size(IDP[:, 0]) == np.size(DEP[:, 0])
    assert np.size(DEP[0, :] == 1)
    records = np.size(IND[:, 0])
    IND = np.concatonate(IND, np.ones(records).reshape(records, 1), axis = 1)
    return np.linalg.solve(np.dot(IND.transpose(), IDP), np.dot(IND.transpose()), DEP.reshape(records, 1))
                    
def estimatedFit(IND, coeff):
    records = np.size(IND[:, 0])
    IND = np.concatonate(IND, np.ones(records).reshape(records, 1), axis = 1)
    coeff = np.repeat(coeff.transpose(), record, axis = 0)
    return np.sum(IND * coeff, axis = 1).reshape(records, 1)
                                    
def corr(FIT, Y):
    muFit = sum(FIT)/float(len(FIT))
    muy = sum(Y)/float(len(Y))
    X0 = FIT - muFit
    Y0 = Y - muy
    return sum(X0 * Y0)/np.sqrt(sum(X0 * X0) * sum(Y0 * Y0))
                                                            
def adjustedRsquared(FIT, Y, variables):
    assert np.size(FIT) == np.size(Y)
    records = np.size(FIT[:, 0])
    muy = sum(Y)/float(len(Y))
    E = (Y - FIT) * (Y - FIT)
    YY = (Y - muy) * (Y - muy)
    return 1 - ((sum(E)/float(records-variables-1))/sum(YY)/float(records-1))
