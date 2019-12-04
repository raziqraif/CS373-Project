import numpy as np
import bootstrap as bs

# data vars
words = []
X = []
y = []

f = open('data.txt', 'r')
s = 0
while(True):
    line = f.readline()[:-1]
    if(not line):
        break
    line = line.split(" ")

    vec = []
    for xi in line[1:-1]:
        vec.append(float(xi))

    words.append(line[0])
    X.append(np.array(vec))
    if line[-1] == 'True':
        y.append(1)
    elif line[-1] == 'False':
        y.append(-1)
    # y.append(line[-1])

    print words[s], X[s], y[s]
    s+=1

X = np.asarray(X)
y = np.asarray(y)
print bs.run(100, X, y)
