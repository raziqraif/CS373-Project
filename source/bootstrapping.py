# Input: number of bootstraps B
# numpy matrix X of features, with n rows (samples), d columns (features)
# numpy vector y of scalar values, with n rows (samples), 1 column
# Output: numpy vector z of B rows, 1 column

import numpy as np
import probclearn
import probcpredict


def run(B, X, y):
    n = X.shape[0]
    d = X.shape[1]
    z = np.zeros((B, 1))
    for i in range(B):
        u = np.zeros((n, 1))
        S = np.empty((0, 1))

        for j in range(n):
            k = np.random.randint(0, n, 1)
            u[j] = int(k)
            S = np.union1d(S, [k])

        T = list()

        X_train = np.zeros((n, d))
        y_train = np.zeros((n, 1))

        for s in range(n):
            if s not in S:
                T.append(s)

        index = 0
        for j in range(n):

            X_train[index] = X[int(u[j])]
            y_train[index] = y[int(u[j])]
            index += 1

        q, mu_positive, mu_negative, sigma2_positive, sigma2_negative = probclearn.run(X_train, y_train)
        z[i] = 0

        for t in T:
            if y[t] != probcpredict.run(q, mu_positive, mu_negative, sigma2_positive, sigma2_negative,
                                            np.array([X[t]]).T):
                z[i] += 1

        z[i] /= len(T)

    return z
