import numpy as np


def getVocabList2():

    """reads the fixed vocabulary list in vocab.txt
    and returns a cell array of the words in vocabList.
    """

## Read the fixed vocabulary list
    vocab_list = []
    f = open('vocab2.txt','r')
    str = f.read()
    vocab_list = str.split(' ')
    f.close()
    return vocab_list
