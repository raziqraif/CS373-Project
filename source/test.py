# import data

WORDS = [] # word, in string form
X = [] # 50-dimensional GloVe vector
y = [] # label, 0 or 1

print("reading data...")
f = open('dataset/data.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    words = line.split(" ")
    WORDS.append(words[0])
    vec = []
    for i in range(50):
        vec.append(float(words[i+1]))
    X.append(vec)
    if(words[51] == 'True'):
        y.append(1)
    else:
        y.append(0)

print("done.")

# test bootstrapping
import bootstrap
import numpy as np
import SVM
import KMeans

import sys

Bmin, Bmax, Bstep = 1, 20, 1
if(sys.argv[1] == "SVM"):
    Cmin, Cmax, Cstep = 0.1, 2, 0.1
else:
    Cmin,Cmax,Cstep = 1, 100, 5
samples = 20
accuracy = []
Brange = np.arange(Bmin, Bmax, Bstep)
Crange = np.arange(Cmin, Cmax, Cstep)
for B in Brange:
    accuracy.append([])
    for C in Crange:
        if(C > B):
            accuracy[-1].append(0)
            continue
        avg = 0
        for j in range(samples):
            if(sys.argv[1] == "SVM"):
                avg += bootstrap.single(X, y, int(B), SVM, C)
            else:
                avg += bootstrap.single(X, y, int(B), KMeans, C)
        avg /= samples
        accuracy[-1].append(avg)
    print(B)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.contourf(Crange, Brange, accuracy)
# plt.xlabel("SVM Margin")
plt.ylabel("Bootstraps")
if(sys.argv[1] == "SVM"):
    plt.xlabel("SVM Margin")
    plt.title("B and C vs Accuracy")
else:
    plt.xlabel("K")
    plt.title("B and K vs Accuracy")
plt.colorbar()
plt.savefig('out.png')
