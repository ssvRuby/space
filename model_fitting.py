from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

import numpy as np


def cross_val(X, y, n_splits=3):
    np.random.seed(0)

    estimators = {
        'KNeighborsClassifier': KNeighborsClassifier(),
        'SVC': SVC(),
        'GaussianNB': GaussianNB(),
        'RandomForestClassifier': RandomForestClassifier(),
        'ExtraTreesClassifier': ExtraTreesClassifier(),
        'DecisionTreeClassifier': DecisionTreeClassifier(),
        'GradientBoostingClassifier': GradientBoostingClassifier(),
        'AdaBoostClassifier': AdaBoostClassifier(),
        'HistGradientBoostingClassifier': HistGradientBoostingClassifier(),
        'BaggingClassifier': BaggingClassifier(KNeighborsClassifier())
    }

    kfold = KFold(n_splits=n_splits, shuffle=True)

    for estimator_name, estimator_object in estimators.items():

        scores = cross_val_score(estimator=estimator_object, X=X, y=y, cv=kfold)

        print(f'{estimator_name:>30}: ' +
              f'mean accuracy ={scores.mean():.2%};' +
              f'standard deviation ={scores.std():.2%}; ')
