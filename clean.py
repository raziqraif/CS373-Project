
data = {}

# common.txt has a list of commonly used English words.
# read the words from common.txt and store them
f = open('common.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    data[line] = []

# glove.txt has the glove vectors (features) of a set of English words
# read through the dataset, and if the word is a 'common' word, we store its features
f = open('glove50.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    line = line.split(" ")
    if(line[0] in data.keys()):
        for xi in line[1:]:
            data[line[0]].append(float(xi))

# pos.txt has the labels of a set of English words (noun vs non-nouns)
# append the labels to the corresponding words
f = open('pos.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    line = line.split("\\")
    if(line[0] in data.keys()):
        data[line[0]].append("N" in line[1])

for key, value in sorted(data.iteritems()):
    if(len(value)%50 != 1 or len(value) < 2):
        continue
    print key,
    for pt in value:
        print pt,
    print

