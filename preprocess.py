#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     preprocess.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 15:08:31
# MODIFIED: 2016-03-28 15:08:36

import sys
import os
import nltk
from nltk import stem
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup as BS

def nltkProcess(text):
    if not text:
        print "Empty text in nltkProcess()!"
        exit()
        
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(text) 
    noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    lmtzr = ""
    for w in noStopwords:
        lmtzr += WordNetLemmatizer().lemmatize(w) + " "
    return lmtzr

    # stem = []
    # for w in lmtzr:
        # stem.append(PorterStemmer().stem(w))
    # print stem
    # return stem

def writeFile(sampleSets, writeFile):
    result = open(writeFile, "w+")
    result.write("id\ttext\ttarget\tcategory\tpolarity\n")
    for i in range(len(sampleSets)):
        if len(sampleSets[i]) < 5:
            print "sampleSets length error!"
            exit()
        id = sampleSets[i][0]
        text = sampleSets[i][1]
        target = sampleSets[i][2]
        category = sampleSets[i][3]
        polarity = sampleSets[i][4]
        print id
        print target
        result.write(id + "\t" + text.encode('utf-8') + "\t" + target.encode('utf-8') + "\t" + category + "\t" + polarity + "\n")
    print "preprocess.py writeFile() done!"
    result.close()

def getSample(sentences):
    sampleSets = []
    for each in sentences:
        id = each["id"]
        opinions = each.opinions
        if not opinions:
            continue
        text = nltkProcess(each.text)
        opinionSet = [a for a in opinions.find_all('opinion')]
        for i in range(len(opinionSet)):
            target = opinionSet[i]["target"]
            category = opinionSet[i]["category"]
            polarity = opinionSet[i]["polarity"]
            curList = [id, text, target, category, polarity]
            sampleSets.append(curList)
        #test usage!
        #return sampleSets
    return sampleSets

def readData(inputFile):
    with open(inputFile, "r") as fin:
        content = BS(fin.read(), "lxml")
        sentences = [a for a in content.find_all('sentence')]
        sampleSets = getSample(sentences)
        print "preprocess.py readData() done!"
        return sampleSets

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: input raw dataSet!"
        print "sys.argv[2]: output preResult filePath!"
        exit()
        
    sampleSets = readData(sys.argv[1])
    writeFile(sampleSets, sys.argv[2])
        
    