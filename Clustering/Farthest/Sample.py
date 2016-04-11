import matplotlib.pyplot as plt, math, random, sys


def dist(v, w, m):
    d = 0
    for i in range(0, m-1):
        d += ((v[i] - w[i]) ** 2)
        return math.sqrt(d)

def farthest(points, k, m):
    centers = [points.pop(points.index(random.choice(points)))]

    while len(centers) < k:
        distance = []
        for c in centers:
            for p in points:
                distance.append((p, dist(p, c, m)))

        centers.append(points.pop(points.index(max(distance, key = lambda pt : pt[1])[0])))

    return centers


with open(sys.argv[1]) as f:
    k, m = [int(x) for x in f.readline().split()]
    points = [tuple([float(x) for x in line.split()]) for line in f]

centers = farthest(points, k, m)

for c in centers:
    plt.scatter(c[0], c[1], s=125, c='red')

for p in points:
    plt.scatter(c[0], c[1], s=125, c='blue')

plt.show()
