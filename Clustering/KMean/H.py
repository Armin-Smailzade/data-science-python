import numpy as np

Initial = np.loadtxt(".\Matrix.txt", delimiter=' ', dtype=np.float)

Matrix = np.loadtxt(".\Matrix.txt", delimiter=' ', dtype=np.float)


minVal = np.amin(Matrix[np.nonzero(Matrix)])

min2 = Matrix[Matrix>0].min()

index = np.argwhere(Matrix == min2)[0]

cluster = [index[0]+1 , index[1]+1]

np.delete(Matrix, np.s_[index[0]], axis=0)
np.delete(Matrix, np.s_[index[1]], axis=1)

newRow = []
 

def Distance(a, b):
    
    sm = 0
    for i in a:
        for j in b:
            sm += Initial[i-1, j-1]
    
    distance = sm/len(a)*len(b)
    return distance
    
    
