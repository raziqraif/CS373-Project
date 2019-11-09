import numpy as np

# data vars
words = []
X = []
y = []

f = open('data.txt', 'r')
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
    y.append(line[-1])

print(words[10], X[10], y[10])
