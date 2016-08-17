import os
os.chdir(r'C:\Users\SHIVAM MAHAJAN\Anaconda2\envs\dato-env\Lib\site-packages')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
os.chdir(r'C:\Users\SHIVAM MAHAJAN\Desktop\Coursera-Stanford-ML-Python-master\ex6')
from processEmail import processEmail
from getVocabList import getVocabList
from wordList import vocabularyDict
from getVocabList2 import getVocabList2
from Datacreation import Datacreation
vocab_list = getVocabList2()

X = []
X = np.array(X)
y = []
y = np.array(y)
path = "C:\Users\SHIVAM MAHAJAN\Desktop\Spam Classifier\data\spam"
X,y = Datacreation(X,path)
storeTxt(X,y,"spamData2")
