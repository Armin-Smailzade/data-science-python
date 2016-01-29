import random
import math
import sys
import matplotlib.pyplot as plt

def Matrix(points, centers):

    b = 2.7
    matrix = [[], []]
    for j in range(len(centers)):
        sumE = 0
        for i in points:
            x = -b * distance(i, centers[j])
            sumE += math.exp(x)
        
        for i in points:
            x = -b * distance(i, centers[j])
            e = math.exp(x)
            matrix[j].append(e/sumE * 100)

    return matrix
    
def calProb(matrix, points):
    prob = []
    #for each row in the matrix calculate the probability
    for row in matrix:
        i = 0
        denominator = sum(row)
        nominator = 0
        for probs in row:
            nominator += probs*points[i] # how to calculate the nominator ?
            i += 1
        prob.append(nominator/denominator)

    return prob
    
def distance(p, c):
    d = 0.0
    for i in range(2):
        d += ((p[i] - c[i]) ** 2)
    return math.sqrt(d)

def unshared_copy(inList):
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList
############################################## Input

# get the DataSet, K, M
with open(sys.argv[1]) as f:
    k, m = [int(x) for x in f.readline().split()]
    # each point = [ [coordinates], [Label] ]
    points = [list([float(x) for x in line.split()]) for line in f]

pointC = unshared_copy(points)

centers = []
############################################## K-Mean
# Initialize First Centers Randomly
while len(centers) < m:
    centers.append(random.choice(pointC))

# pick a random guess for the probability of each center
prob = []
rand = random.uniform(0, 1)
prob.append(rand)
prob.append(1-rand)


for i in range(5000):
    # Calculate the matrix
    matrix = Matrix(points, centers)
    # Calculate the prob by matrix
    prob = calProb(matrix, points)


    

