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

def combineFeature(tfidfMatrix, wnMatrix, w2vMatrix = None):
    allMatrix = np.concatenate((tfidfMatrix, wnMatrix), axis=1)
    if w2vMatrix:
        allMatrix = np.concatenate((allMatrix, w2vMatrix), axis=1)
    return allMatrix
    

def readData(inputFile):
    #test usage!
    ids = []
    
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
            #test usage!
            ids.append(id)
            if i > 20:
                print ids
                print corpus
                print targets
                return corpus, targets, categories, polarities
                
    return corpus, targets, np.array(categories), polarities
            

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: predict train.txt!"
        print "sys.argv[2]: predict test.txt!"
        print "sys.argv[3]: p-recall-f1 outputFile!"
        exit()
    
    tfidfInstance = Tfidf()
    wordNetInstance = WordNet()
    w2vInstance = W2v()
    
    
    #train data set
    trCorpus, trTargets, trCategories, trPolarities = readData(sys.argv[1])
    trainTfidf = tfidfInstance.tfidf(trCorpus)    
    trainWn = wordNetInstance.shortestPath(trTargets)
    #trainW2v = w2vInstance.semantic(trTargets)
    trainMatrix = combineFeature(trainTfidf, trainWn)
    
    #test data set
    teCorpus, teTargets, teCategories, tePolarities = readData(sys.argv[2])
    testTfidf = tfidfInstance.tfidf(teCorpus)    
    testWn = wordNetInstance.shortestPath(teTargets)
    # testW2v = w2vInstance.semantic(teTargets)
    testMatrix = combineFeature(testTfidf, testWn) 
    
    #write result
    result = open(sys.argv[3], "a+")
    result.write("-----------\n")
    classifierInstance = Classifier(trainMatrix, trCategories, testMatrix, teCategories)
    methods = ["tree", "knn", "svm", "gbdt", "essemble"]
    for i in range(len(methods)):
        key = methods[i]
        precision, recall, f1 = classifierInstance.classification(key)
        value = str(precision) + "-" + str(recall) + "-" + str(f1)
        result.write(key + "\t" + value + "\n")
    result.close()
    
    
    
    

    
    
    
