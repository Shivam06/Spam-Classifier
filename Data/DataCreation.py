from processEmail import processEmail
from getVocabList2 import getVocabList2

def Datacreation(X,y,path):
    vli = getVocabList2()
    count = 0
    for root, dirs, files in os.walk(path):
            for name in files:
                n = os.path.join(root,name)
                f = open(n,'r')
                content = f.read()
                word_index,wlist = processEmail(content)
                n = len(vli)
                
                if len(X) == 0:
                    X = np.zeros((1,n))
                    X[0,word_index] = 1
                    if root.find('spam')>=0:
                        y = np.ones((1,1))
                    else:
                        y = np.zeros((1,1))
                    
                else:
                    a = np.zeros((1,n))
                    a[0,word_index] = 1
                    X = np.vstack((X,a))
                    if root.find('spam')>=0:
                        b = np.ones((1,1))
                    else:
                        b = np.zeros((1,1))
                    y = np.vstack((y,b))
                    count = count + 1
                print count
                f.close()
        
    return X,y
