#import numpy as np
import os
#import sys
os.chdir('C:\Users\SHIVAM MAHAJAN\Desktop\Coursera-Stanford-ML-Python-master\ex6')
from processEmail import processEmail


def vocabularyDict(df,path): 
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            n=os.path.join(root, name)
            f = open(n,'r')
            content = f.read()
            words,li = processEmail(content)
            for name in li:
                if name in df:
                    df[name] = df[name] + 1
                else:
                    df[name] = 1
    
            f.close();
    return df


        
