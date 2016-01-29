import sys
import math
import random

class Point:

    def __init__(self, coords):
        self.coords = coords

    def __repr__(self):
        return str(self.coords)

class Cluster:

    def __init__(self, points):
        self.points = points
        self.centroid = self.calculateCentroid()

    def __repr__(self):
        return str(self.points)

    def update(self, points):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        '''
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid)
        return shift

    def calculateCentroid(self):
        '''
        Finds a virtual center point for a group of n-dimensional points
        '''
        numPoints = len(self.points)
        # Get a list of all coordinates in this cluster
        coords = [p.coords for p in self.points]

        # Reformat that so all x's are together, all y'z etc.
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]

        return Point(centroid_coords)

def kmeans(points, k, cutoff):

    # Pick out k random points to use as our initial centroids
    initial = random.sample(points, k)

    # Create k clusters using those centroids
    clusters = [Cluster([p]) for p in initial]

    # Loop through the dataset until the clusters stabilize
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [ [] for c in clusters]
        clusterCount = len(clusters)

        # Start counting loops
        loopCounter += 1
        # For every point in the dataset ...
        for p in points:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(p, clusters[0].centroid)

            # Set the cluster this point belongs to
            clusterIndex = 0

            # For the remainder of the clusters ...
            for i in range(clusterCount - 1):
                # calculate the distance of that point to each other cluster's
                # centroid.
                distance = getDistance(p, clusters[i+1].centroid)
                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is, and set the point to belong
                # to that cluster
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i+1
            lists[clusterIndex].append(p)

        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0

        # As many times as there are clusters ...
        for i in range(clusterCount):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])
            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)

        # If the centroids have stopped moving much, say we're done!
        if biggest_shift < cutoff:
            print "Converged after %s iterations" % loopCounter
            break
    return clusters

def getDistance(a, b):
    d = 0
    for i in xrange(2):
        d += ((a.coords[i] - b.coords[i]) ** 2)
    return math.sqrt(d)



with open(sys.argv[1]) as f:
    k, m = [int(x) for x in f.readline().split()]
    points = [Point(list([float(x) for x in line.split()])) for line in f]

# When do we say the optimization has 'converged' and stop updating clusters
opt_cutoff = 0.5

# Cluster those data!
clusters = kmeans(points, k, opt_cutoff)

# Print our clusters
#for c in enumerate(clusters):
print " Cluster: ""\t Centroid :", clusters
