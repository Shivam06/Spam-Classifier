import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def ParametersLinsvm(Xtrain,ytrain,Xval,yval):
    
    cvalue = [0.01,0.03,0.1,0.3,1,3,10]
    max = 0    
    scores = []
    for c in cvalue:
        svm = SVC(kernel = 'linear', random_state = 0, C=c)
        svm.fit(Xtrain,ytrain)
        ypred = svm.predict(Xval)
        a = accuracy_score(ypred,yval)
        scores.append(a)
        if a > max:
            max = a
            C=c
            
            
    return C,max,scores
