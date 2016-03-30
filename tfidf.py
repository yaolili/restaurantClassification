#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     tfidf.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 17:56:37
# MODIFIED: 2016-03-28 17:56:39

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class Tfidf:
    def tfidf(self, trCorpus, teCorpus):
        vect = TfidfVectorizer(min_df = 1, norm = "l1")
        trainMatrix = vect.fit_transform(trCorpus).toarray()
        testMatrix = vect.transform(teCorpus).toarray()
        print "Tfidf done!"
        return trainMatrix, testMatrix
        
    
    
    
    