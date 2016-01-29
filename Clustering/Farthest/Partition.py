import math
import numpy as np

class Clustering (object):

    #def __init__(self, fileName, K):
        #self.K = K
        #self.points = np.loadtxt(fileName, delimiter=',', skiprows=1, dtype=np.float64)

    
    def Farthest(self, Data, K):    

        Centers = [Data[0]]
        Data.remove([0,0])

            
        while len(Centers) < K:
            
            max1 = c.Distance(Centers[0], Data[0])
            point = Data[0]

            for i in Centers:
            
                for j in Data:
                    
                    max2 = c.Distance(i, j)
                    
                    if max1 < max2:
                        max1 = max2
                        point = j
                    
            Centers.append(point)
            Data.remove(point)
            
        
        print Centers
            
    def Distance(self, x1, x2):
        
        return math.sqrt(math.pow(x2[1] - x1[1], 2) + math.pow(x2[0] - x1[0], 2))
    

Data = [[0,0], [0,5], [1,1], [2,2], [3,3], [1,2], [5,5]]
K = 3
c = Clustering()
c.Farthest(Data, K)
