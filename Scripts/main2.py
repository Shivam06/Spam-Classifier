import os
os.chdir(r'C:\Users\SHIVAM MAHAJAN\Anaconda2\envs\dato-env\Lib\site-packages')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import scipy.io
from sklearn.svm import SVC

import scipy.misc
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
os.chdir(r'C:\Users\SHIVAM MAHAJAN\Desktop\Coursera-Stanford-ML-Python-master\ex6')
from processEmail import processEmail
from getVocabList import getVocabList
from wordList import vocabularyDict
from getVocabList import getVocabList
from Datacreation import Datacreation
from gaussianKernel import gaussianKernel
from visualizeBoundary import visualizeBoundary
from dataset3Params import dataset3Params

 
df = pd.read_csv('spamData2.txt')
X = np.array(df.iloc[:,0:17323].values)
y = np.array(df.iloc[:,[17323]].values)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size = 0.2,random_state = 0)
Xtrain,Xval,ytrain,yval = train_test_split(Xtrain,ytrain,test_size=0.25,random_state=0)

C,sigma,accuracy = dataset3Params(Xtrain_std,ytrain,Xval_std,yval)
