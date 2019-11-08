
data = {}

f = open('common.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    data[line] = []

f = open('glove50.txt', 'r')
while(True):
    line = f.readline()[:-1] # consume newline
    if(not line):
        break
    line = line.split(" ")
    if(line[0] in data.keys()):
        for xi in line[1:]:
            data[line[0]].append(float(xi))

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

