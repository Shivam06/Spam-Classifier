# Spam-Classifier

Trained ML model to predict whether a mail is Spam or Ham as an extension over ML class, Coursera homework.

<ul>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/processEmail.py">processEmail.py</a></b> - Module containing function to process the individual mail and convert them into feature vectors after removing redundant stuff.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/wordList.py">wordList.py</a></b> - Module containing function to create a dictionary of all the words occuring in all mails</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/getVocabList2.py">getVocabList2.py</a></b> - Module containing function to return the vocabulary list.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/DataCreation.py">DataCreation.py</a></b> - Module containing function to form feature matrix and output vector.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/storeTxt.py">storeTxt.py</a></b> - Module containing function to store feature matrix and output vector in a text file - <b>vocab2.txt</b>.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/dataset3Params.py">dataset3Params.py</a></b> - Module containing function to find the best regularization hyperparameter for SVM model.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/main">main.py</a></b> - Script to create feature matrix and output vector and storing it in spamData2.txt file.</li>
<li><b><a href="https://github.com/Shivam06/Spam-Classifier/blob/master/Scripts/dataset3Params.py">main2.py</a></b> - Script to load data from spamData2.txt and split it into training, test and cross validation set and subsequently finding the best value of regularization hyperparameter.</li>
</ul>
