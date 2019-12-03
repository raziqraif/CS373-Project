from sklearn import svm
import numpy as np

# X: list of d-dimensional points (example: [[x0, y0], [x1, y1], ...]).
# y: list of labels corresponding to the vectors in X.
# return: trained sklearn SVC Classifier.
def train(X, y, lamb):
    from sklearn.svm import SVC
    ret = SVC(kernel='poly', degree=10, C=lamb, gamma='auto')
    # print(X, y)
    try:
        ret.fit(X, y)
    except ValueError:
        return -1
    return [ret]

# X: list of d-dimensional points to classify.
# svc: SVCClassifier as returned by train() above.
# return: predicted labels associated with the vectors in X.
def test(X, svc):
    if(svc == -1):
         return np.ones(len(X))
    return svc[0].predict(X)
