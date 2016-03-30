#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     main.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 20:18:12
# MODIFIED: 2016-03-28 20:18:14

import os
import sys
import numpy as np
from tfidf import Tfidf
from w2v import W2v
from wordNet import WordNet
from classifier import Classifier

#write Precision-Recall-F1 result
def writeResult(writeFile, trainMatrix, trainLables, testMatrix, testLables):
    result = open(writeFile, "a+")
    result.write("-------Method\tPrecision-Recall-F1-------\n")
    classifierInstance = Classifier(trainMatrix, trainLables, testMatrix, testLables)
    
    methods = ["tree", "knn", "svm", "essemble", "nb", "gbdt"]
    for i in range(len(methods)):
        key = methods[i]
        classifierInstance.classification(key)
        print key + "classification() done!"
        dict = classifierInstance.evaluate()
        for metric in dict:
            result.write(key + "\t" + metric + "\t" + dict[metric] + "\n")
    result.close()


def combineFeature(tfidfMatrix, wnMatrix, w2vMatrix = None):
    allMatrix = np.concatenate((tfidfMatrix, wnMatrix), axis=1)
    if isinstance(w2vMatrix, np.ndarray):
        allMatrix = np.concatenate((allMatrix, w2vMatrix), axis=1)
    return allMatrix
    

def readData(inputFile):
    corpus = []
    targets = []
    categories = []
    polarities = []
    with open(inputFile, "r") as fin:
        for i, line in enumerate(fin):
            if i == 0:
                continue
            id, text, target, category, polarity = line.strip().split("\t")
            corpus.append(text)
            targets.append(target)
            categories.append(category)
            polarities.append(polarity)
                
    return corpus, targets, np.array(categories), polarities
            

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: predict train.txt!"
        print "sys.argv[2]: predict test.txt!"
        print "sys.argv[3]: categories p-recall-f1 outputFile!"
        print "sys.argv[4]: polarity p-recall-f1 outputFile!"
        exit()
    
    tfidfInstance = Tfidf()
    wordNetInstance = WordNet()
    w2vInstance = W2v()

    #train data set
    trCorpus, trTargets, trCategories, trPolarities = readData(sys.argv[1])  
    #test data set
    teCorpus, teTargets, teCategories, tePolarities = readData(sys.argv[2])    
    trainTfidf, testTfidf = tfidfInstance.tfidf(trCorpus, teCorpus)
    print trainTfidf.shape
    print testTfidf.shape
    
    trainWn = wordNetInstance.shortestPath(trTargets)
    testWn = wordNetInstance.shortestPath(teTargets)
    trainW2v = w2vInstance.semantic(trTargets)
    testW2v = w2vInstance.semantic(teTargets)
    trainMatrix = combineFeature(trainTfidf, trainWn, trainW2v)
    testMatrix = combineFeature(testTfidf, testWn, testW2v)
    # trainMatrix = combineFeature(trainTfidf, trainWn)
    # testMatrix = combineFeature(testTfidf, testWn)     
    
    writeResult(sys.argv[3], trainMatrix, trCategories, testMatrix, teCategories)
    writeResult(sys.argv[4], trainTfidf, trPolarities, testTfidf, tePolarities)
    

    
    
    
    
    
    

    
    
    
