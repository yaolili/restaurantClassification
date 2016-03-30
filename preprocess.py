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

def nltkProcess(text, type):
    if not text:
        print "Empty text in nltkProcess()!"
        exit()
        
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(text) 
    if type == "0":
        noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    else:
        noStopwords = [w.lower() for w in tokens]
    lmtzr = ""
    for w in noStopwords:
        lmtzr += WordNetLemmatizer().lemmatize(w) + " "
    return lmtzr

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
        result.write(id + "\t" + text.encode('utf-8') + "\t" + target.encode('utf-8') + "\t" + category + "\t" + polarity + "\n")
    print "preprocess.py writeFile() done!"
    result.close()

def getSample(sentences, type):
    sampleSets = []
    for each in sentences:
        id = each["id"]
        opinions = each.opinions
        if not opinions:
            continue
        text = nltkProcess(each.text, type)
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

def readData(inputFile, type):
    with open(inputFile, "r") as fin:
        content = BS(fin.read(), "lxml")
        sentences = [a for a in content.find_all('sentence')]
        sampleSets = getSample(sentences, type)
        print "preprocess.py readData() done!"
        return sampleSets

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: input raw dataSet!"
        print "sys.argv[2]: output preResult filePath!"
        print "sys.argv[3]: operation type, 0: remove stopwords from text, 1 without removing"
        exit()
        
    sampleSets = readData(sys.argv[1], sys.argv[3])
    writeFile(sampleSets, sys.argv[2])
        
    