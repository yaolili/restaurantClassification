#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     wordNet.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 20:53:15
# MODIFIED: 2016-03-28 20:53:16

import enchant
import sys
import numpy as np
from nltk.corpus import wordnet as wn

class WordNet:
    def shortestPath(self, targets):
        score = []
        labels = ["food", "restaurants", "service", "ambience", "drinks", "location"]
        enWords = enchant.Dict("en_US")
        for i in range(len(targets)):
            if enWords.check(targets[i]):
                all = wn.synsets(targets[i], wn.NOUN)
                if all:
                    t = all[0]
                    curDist = []
                    for j in range(len(labels)):
                        label = wn.synsets(labels[j], wn.NOUN)[0]
                        distance = t.shortest_path_distance(label)
                        curDist.append(distance)
                else:
                    curDist = [sys.maxint, sys.maxint, sys.maxint, sys.maxint, sys.maxint, sys.maxint]
            else:
                curDist = [sys.maxint, sys.maxint, sys.maxint, sys.maxint, sys.maxint, sys.maxint]
            score.append(curDist)
        array = np.array(score)
        print "WordNet done!"
        return array
