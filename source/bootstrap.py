

# take 100 sample subsets of complete dataset
# train classifier on that subset
# determine accuracy (correct/total) of trained classifier, using complete dataset
# return

import random
import SVM
import KMeans
import numpy as np

# X: complete dataset input features
# y: labels corresponding to X
# B: number of samples to use in each randomly sampled bootstrap
# Type: either SVM or KMeans
# param: margin radius for SVM or K for KMeans
# return: average accuracy of subset-trained classifier
def single(X, y, B, Type, param):
    X_train,y_train = [],[]
    for i in range(B):
        id = random.randint(0, len(X)-1)
        X_train.append(np.array([X[id][j] for j in range(len(X[0]))]))
        y_train.append(y[id])

    # # SVM
    # ret = SVM.train(X_train, y_train, lam)
    # y_predicted = SVM.test(X, ret)
    # KMeans
    ret = Type.train(X_train, y_train, param)
    y_predicted = Type.test(X, ret)

    accuracy = 1.0*sum(abs(np.array(y) - np.array(y_predicted)))/len(X)
    return accuracy
