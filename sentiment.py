#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     sentiment.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-30 18:14:12
# MODIFIED: 2016-03-30 18:14:17

import numpy as np
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

class Sentiment:
    def VSPolarity(self, corpus):
        self.result = []
        for sentence in corpus:
            vs = vaderSentiment(sentence)
            aList = [vs["neg"], vs["neu"], vs["pos"]]
            self.result.append(aList)
        return np.array(self.result)
        
    def TBPolarity(self, corpus):
        self.result = []
        for sentence in corpus:
            tb = TextBlob(sentence, analyzer = NaiveBayesAnalyzer())
            pos = tb.sentiment[1]
            neg = tb.sentiment[2]
            aList = [pos, neg]
            self.result.append(aList)
        return np.array(self.result)