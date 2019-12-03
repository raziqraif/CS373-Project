from sklearn.cluster import KMeans
import numpy as np
import numpy.linalg as la

# X: list of d-dimensional points (example: [[x0, y0], [x1, y1], ...])
# k: number of centers (example: 3)
# returns: list of k d-dimensional cluster centers, list of k labels.
def train(X, y, k):
    kmeans = KMeans(n_clusters=int(k), random_state=0).fit(X)
    centers = kmeans.cluster_centers_

    # count number of nouns and non-nouns closest to each center
    noun = np.zeros(k)
    not_noun = np.zeros(k)
    associated_centers = kmeans.predict(X)
    for i in range(len(X)):
        if(y[i] == 0): # not noun
            not_noun[associated_centers[i]] += 1
        else: # noun
            noun[associated_centers[i]] += 1

    # determine labels of cluster centers
    labels = np.zeros(k)
    for i in range(k):
        if(noun[i] > not_noun[i]):
            labels[i] = True
        else:
            labels[i] = False

    return [centers, labels]

# X: list of d-dimensional points to classify.
# centers, labels: as returned from KMeans.train (above).
# return: labels associated with the vectors in X.
def test(X, tr):
    centers = tr[0]
    labels = tr[1]
    ret = np.zeros(len(X))
    for i in range(len(X)):
        min_dist = np.inner(centers[0]-X[i],centers[0]-X[i]) + 1
        for j in range(len(centers)):
            dist = np.inner(centers[j]-X[i], centers[j]-X[i])
            if(dist < min_dist):
                min_dist = dist
                ret[i] = labels[j]
    return ret
