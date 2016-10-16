import numpy as np
import os
os.chdir(r'C:\Users\SHIVAM MAHAJAN\Desktop\Coursera-Stanford-ML-Python-master\ex6')
def storeTxt(X,y,name):
    name = name + '.txt'
    
    file = open(name,'w')
    
    for i in range(len(y)):
        outstr = ''
        for j in range(len(X[1,:])):
            outstr += str(X[i,j]) + ','
        outstr += str(y[i,0]) + '\n'
        file.write(outstr)
     
    file.close()
    
    
