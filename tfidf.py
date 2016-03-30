#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     tfidf.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 17:56:37
# MODIFIED: 2016-03-28 17:56:39


from sklearn.feature_extraction.text import TfidfVectorizer

class Tfidf:
    def tfidf(self, corpus):
        vect = TfidfVectorizer(min_df = 1, norm = "l1")
        matrix = vect.fit_transform(corpus).toarray()
        return matrix
        
    
    
    
    