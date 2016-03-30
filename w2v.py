#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     w2v.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 20:36:21
# MODIFIED: 2016-03-28 20:36:22

import enchant
import numpy as np
import gensim
import scipy.stats

class W2v:
    def semantic(self, targets):
        score = []
        model = gensim.models.Word2Vec.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary = True) 
        print "w2v load GoogleNews-vectors-negative300.bin done!"
        labels = ["food", "restaurants", "service", "ambience", "drinks", "location"]
        enWords = enchant.Dict("en_US")
        for i in range(len(targets)):
            if enWords.check(targets[i]):
                curScore = []
                for j in range(len(labels)):
                    s = model.similarity(targets[i], labels[j])
                    curScore.append(s)
            else:
                curScore = [0, 0, 0, 0, 0, 0]
            score.append(curScore)
        array = np.array(score)
        return array