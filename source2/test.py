import KMeans

cluster, labels = KMeans.train([[0, 0], [0, 1], [100, 0], [100, 1]], [0, 0, 1, 1], 2)

print(KMeans.test([[51, 0]], cluster, labels))

import SVM
import random
import numpy as np

X_train, y_train = [],[]
for i in range(100):
    r = random.uniform(0, 1)
    theta = random.uniform(0, 6.283)
    X_train.append([r*np.cos(theta), r*np.sin(theta)])
    y_train.append(0)
    X_train.append([(2+r)*np.cos(theta), (2+r)*np.sin(theta)])
    y_train.append(1)

svc = SVM.train(X_train, y_train, 0.1)

print(SVM.test([[0, 0], [2, 0]], svc))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plotX = [[6.0*i/100 - 3, 6.0*j/100 - 3] for j in range(0, 100) for i in range(0, 100)]
plotY = SVM.test(plotX, svc)
plt.scatter([x[0] for x in plotX], [x[1] for x in plotX], c=plotY)
plt.savefig('test.png')
