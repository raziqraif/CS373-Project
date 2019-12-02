import KMeans

cluster, labels = KMeans.train([[0, 0], [0, 1], [100, 0], [100, 1]], [0, 0, 1, 1], 2)

print(KMeans.test([[51, 0]], cluster, labels))
