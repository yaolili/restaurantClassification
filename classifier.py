#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     classfier.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-29 12:07:35
# MODIFIED: 2016-03-30 09:20:17

class Classifier:
    def __init__(self, trainMatrix, trainLabels, testMatrix, testLabels):
        self.X_train = trainMatrix 
        self.y_train = trainLabels
        self.X_test = testMatrix
        
        #fit transform if there exit NAN or INFINITE
        #otherwise you'll get error when clf.predict()
        self.X_test = Imputer().fit_transform(self.X_test) 
        if np.isnan(self.X_test).any():
            print "nan in X_test!"
            exit()
            
        self.y_test = testLabels
        
    def classfication(self, classifier):
        
        if classifier == 'tree':
            #max_depth = 4 is best
            # max_depth = np.arange(1, 10)
            # clf = GridSearchCV(tree.DecisionTreeClassifier(), param_grid = {'max_depth': max_depth})
            clf = tree.DecisionTreeClassifier(max_depth = 4)
            
        elif classifier == 'knn':
            #n_neighbors = 9 is best
            #but default is 5, better than 9?
            # n_neighbors = np.arange(1, 10)  
            # clf = GridSearchCV(KNeighborsClassifier(), param_grid = {'n_neighbors': n_neighbors})
            clf = KNeighborsClassifier(n_neighbors = 9)
            
        elif classifier == 'svm':
            #{'kernel': 'rbf', 'C': 100, 'gamma': 0.001}
            # param_grid = [{'C': [1, 10, 100, 1000], 'kernel': ['linear']}, {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']}]
            # clf = GridSearchCV(svm.SVC(), param_grid)
            clf = svm.SVC(kernel='rbf', gamma = 0.001, C = 100)
            
        elif classifier == 'gbdt':
            # max_depth = np.arange(1, 10)
            # n_estimators = [10, 100, 1000]
            # learning_rate = [0.1, 0.2, 0.3, 0.4, 0.5]
            # clf = GridSearchCV(GradientBoostingClassifier(), param_grid = {'max_depth': max_depth, 'n_estimators': n_estimators, 'learning_rate': learning_rate})
            clf = GradientBoostingClassifier(n_estimators = 1000, max_depth = 10)
            
        elif classifier == 'essemble':
            #{'n_estimators': 10, 'max_depth': 6}
            # max_depth = np.arange(1, 10)
            # n_estimators = [10, 100, 1000]
            # clf = GridSearchCV(RandomForestClassifier(), param_grid = {'max_depth': max_depth, 'n_estimators': n_estimators})
            clf = RandomForestClassifier(n_estimators = 1000, random_state=15325)
            
        elif classifier == 'nb':
            clf = MultinomialNB()
            print clf
        else:
            print "Invalid classifier in Class Classification __init__()!"
            exit()
        
        clf.fit(self.X_train, self.y_train) 
        self.y_pred = clf.predict(self.X_test)
        
    def evaluate(self):  
        m_precision = metrics.precision_score(self.y_test, self.y_pred)
        m_recall = metrics.recall_score(self.y_test, self.y_pred) 
        return format(m_precision), format(m_recall), format(metrics.f1_score(self.y_test, self.y_pred))       
        
        
