import math

def Farthest(Data, K):    

    Centers = [Data[0]]
    Data.remove([0,0])
        
    while len(Centers) < K:
        
        max1 = Distance(Centers[0], Data[0])
        point = Data[0]

        for i in Centers:
        
            for j in Data:
                
                max2 = Distance(i, j)
                
                if max1 < max2:
                    max1 = max2
                    point = j
                
        Centers.append(point)
        Data.remove(point)
        
    return Centers
        
def Distance(x1, x2):
    
    return math.sqrt(math.pow(x2[1] - x1[1], 2) + math.pow(x2[0] - x1[0], 2))
    

Data = [[0,0], [0,5], [1,1], [2,2], [3,3], [1,2], [5,5]]
K = 3
print (Farthest(Data, K))
