import sys
import getopt
import random
import matplotlib.pyplot as plt
from pandas import *

def findCenter(data, k, dim):
    #find the centers of the clusters using maximum distance between points 
    #find the centers as well as calculate the distance to the center for each POINT
    centers = [[random.choice(data)[0], 0.0]] #center coord, radius
    numCenters = len(centers)
    
    while numCenters < k:
        maxLen = 0.0
        maxDP = None
        for d in data:
            c = numCenters-1
            d[1][c] = findDistance(d[0], centers[c][0], dim)
            if(d[1][c] > maxLen) and d[0] not in centers:
                maxLen = d[1][c] 
                maxDP = d[0]
        if numCenters < k and maxDP is not None and maxDP not in centers:
            centers.append([maxDP, 0.0])
            numCenters = len(centers)
        
    for d in data:
        c = numCenters - 1
        d[1][c] = findDistance(d[0], centers[c][0], dim)
        
    return centers

def findDistance(x, y, dim):
    #find the distance between two points in n dimension
    d = 0.0
    for i in xrange(dim):
        d += (y[i] - x[i]) ** 2
    return (d**0.5)


def splitClusters(data, centers, k, dim):
    #split data points into clusters and calculate the radius of the cluster
    clusters = [[[], []] for i in xrange(k)]
    
    for d in data:
        d[2] = d[1].index(min(d[1]))
        clusters[d[2]][0].append(d[0][0])
        clusters[d[2]][1].append(d[0][1])
    
    for c in xrange(k):
        points = len(clusters[c][0])
        for p in xrange(points):
            centers[c][1] = max(centers[c][1], findDistance([clusters[c][0][p], clusters[c][1][p]], centers[c][0],dim))

    return clusters

def plotClusters(centers, clusters):
    #plot the clusters and their radius
    fig = plt.figure()
    ax = plt.subplot(111)
    
    lenClusters = len(clusters)
    for c in xrange(lenClusters):
        ax.plot(clusters[c][0], clusters[c][1], 'o', label = 'Cluster %d (%1.1f, %1.1f)' % (c, centers[c][0][0], centers[c][0][1]))
        circle = plt.Circle((centers[c][0][0], centers[c][0][1]), centers[c][1], file=False)
        ax.add_patch(circle)
    
    ax.axis([-10.5, 15.5, -10.5, 15.5])
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.65, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    
def init_board_gauss(N, k, dim):
    #creates dummy data of N points for k clusters in n dimensions
    n = float(N)/k 
    X = []
    for i in range(k):
        c = [random.uniform(1, 4) for j in xrange(dim)]
        s = random.uniform(0.5, 0.5)
        x = []
        while len(x) < n:
            p = [np.random.normal(c[j], s) for j in xrange(dim)]
            x.append(p)
        X.extend(x)
    X = X[:N]
    return X 

#parsing input
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:ad:k:n:", ["ifile="])
except getopt.GetoptError:
    print ('assignment1.py -i <inputfile or assignment1.py -a')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('assignment1.py -i <inputfile or assignment1.py -a')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-a", "--auto"):
        auto = True
    elif opt in ("-k"):
        k = int(arg)
    elif opt in ("-d"):
        dim = int(arg)
    elif opt in ("-n"):
        n = int(arg)

if auto:
    points = init_board_gauss(n, k, dim)
    dp = []
    f = open("ast2.txt", "w")
    f.write("%d\t%d\n" % (k, dim))
    for p in points:
        dp.append([p, [0.0 for i in xrange(k)], None])
        for x in p:
            f.write("%f\t" % x)
        f.write("\n")
    f.close()
else:
    i = 0
    dp = []
    for l in open(inputfile, "r"):
        if i == 0:
            k, dim = [int(x) for x in l.split()]
            i = 1
        else:
            dp.append([[float(x) for x in l.split()], [0.0 for i in xrange(k)], None])

centers = findCenter(dp, k, dim)
clusters = splitClusters(dp, centers, k, dim)
plotClusters(centers, clusters)


            

                                 
