import random
import math
import sys
import matplotlib.pyplot as plt

def cluster(centroids, datapoints):

    # for each point find the nearest Center
    for p in datapoints:
        minD = distance(p[0], centroids[0][0])
        p[1] = centroids[0][0]
        for c in centroids:
            d = distance(p[0], c[0])
            if(d < minD):
                minD = d
                p[1] = c[0]
    return datapoints

# Update the centers
def calculateCentroid(centroids, datapoints):

    # for each Center find it's points
    for c in centroids:
        x=0
        y=0
        count = 0
        for p in points:
            # if a Point's Label is center C
            if p[1] == c[0]:
                # include it in (x1+x2,.../points + y1+y2,.../points)
                x += p[0][0]
                y += p[0][1]
                count += 1
        c[0] = [x/count, y/count]

    return centroids

def distance(p, c):
    d = 0.0
    for i in range(2):
        d += ((p[i] - c[i]) ** 2)
    return math.sqrt(d)

def unshared_copy(inList):
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList
    
def plus(data, centers):
    
    # Find the minimum distance from the centers for each point 
    distances = []
    for point in data:
        dmin = distance(point[0], centers[0][0])
        for center in centers:
            d1 = distance(point[0], center[0])
            if(d1 < dmin):
                dmin = d1
        distances.append(dmin)
    sumOfDistances = sum(distances)
    
    # Normalize the distances
    normalize = []
    for point in distances:
        normalize.append(math.ceil((point/sumOfDistances)*100)/100)
    
    # Roulette Wheel (an array of points which each point has a space proportional to it's probability)    
    partitions = []
    part = 0.0
    for p in normalize:
        part += p
        partitions.append(math.ceil((part)*100)/100)     
    
    # Picking a point from the Roulette Wheel
    rand = random.uniform(0, 1)
    centerIndex = 0
    for p in partitions:
        if rand < p:
            centerIndex = partitions.index(p)
            break
    
    return data[centerIndex]
    
############################################## Input
with open(sys.argv[1]) as f:
    k, m = [int(x) for x in f.readline().split()]
    points = [list([list([float(x) for x in line.split()]),[]]) for line in f]

pointC = unshared_copy(points)

centers = []

############################################## K-Mean
# Initialize The First Center Randomly
centers.append(random.choice(pointC))

#Select The Second Center based on the probability 
centers.append(plus(pointC, centers))

# 5000 Iterations for K-Mean
for i in range(5000):
    points = cluster(centers, points)
    centers = calculateCentroid(centers, points)

############################################## Plot
# Clusters
for p in points:
    if p[1][0] == centers[0][0][0]:
        plt.scatter(p[0][0], p[0][1], s=125, c='red')
    else:
        plt.scatter(p[0][0], p[0][1], s=125, c='blue')
# Centers
for c in centers:
    plt.scatter(c[0][0], c[0][1], s=125, c='yellow')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()

# Final Centers : [[1.8, 2.867], [1.032, 1.212]]
######################