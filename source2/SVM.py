from sklearn import svm
import numpy as np

# X: list of d-dimensional points (example: [[x0, y0], [x1, y1], ...]).
# y: list of labels corresponding to the vectors in X.
# return: trained sklearn SVC Classifier.
def train(X, y, lamb):
    from sklearn.svm import SVC
    svc = SVC(kernel='poly', degree=4, C=lamb)
    svc.fit(X, y)
    return svc

# X: list of d-dimensional points to classify.
# svc: SVCClassifier as returned by train() above.
# return: predicted labels associated with the vectors in X.
def test(X, svc):
    return svc.predict(X)
