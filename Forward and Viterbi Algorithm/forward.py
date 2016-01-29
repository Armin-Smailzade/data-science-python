'''
@author: Armin
'''
import numpy as np

class forward(object):
    

    def __init__(self, initialTable, transitionTable, emissionTable, alphaTable):
        self.initialTable = initialTable
        self.transitonTable = transitionTable 
        self.emissionTable = emissionTable
        self.alphaTable = alphaTable

    def Initialization(self):
        
        for i in range(len(alphaTable[0][:])):
            alphaTable[0][i] = np.multiply(self.initialTable[i], self.emissionTable[i][0])

        
    def Alphas(self, obs):

        obsIndex = 0
        sumA = 0
        
        for t in range(len(alphaTable)-1):
            t += 1
            for j in range(len(alphaTable[t])):
                for i in range(len(self.initialTable)):
                    sumA += self.transitonTable[i][j] * alphaTable[t-1][i] * self.emissionTable[j][obs[obsIndex]]
                alphaTable[t][j] = sumA
                sumA = 0
            obsIndex += 1
        
        print("Alphas ")
        print(alphaTable)

####################### Data Import#############################

# States = {S1, S2, S3}
# Symbols = {x, y, z}

InitialTable = np.loadtxt("forward_Data/InitialTable.txt", delimiter=',', dtype=np.float64)

TransitionTable = np.loadtxt("forward_Data/TransitionTable.txt", delimiter=',', dtype=np.float64)

EmissionTable = np.loadtxt("forward_Data/EmissionTable.txt", delimiter=',', dtype=np.float64)

####################### Data #############################
#This is the table where we keep alphas
alphaTable = np.zeros((3,3), dtype= np.float64)

# Data = xxz
data = [0,0,2]

test = forward(InitialTable, TransitionTable, EmissionTable, alphaTable)
test.Initialization()
test.Alphas(data)