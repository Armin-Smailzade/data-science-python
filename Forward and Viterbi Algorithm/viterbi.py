'''
@author: Armin
'''
import numpy as np

class viterbi(object):
    
####################### Constructor #####################

    def __init__(self, initialTable, transitionTable, emissionTable, deltaTable, psTable):
        self.initialTable = initialTable
        self.transitionTable = transitionTable 
        self.emissionTable = emissionTable
        self.deltaTable = deltaTable
        self.psTable = psTable

####################### Functions #######################
    def Initialization(self):
        for i in range(len(self.deltaTable[0])):
            self.deltaTable[0][i] = np.multiply(InitialTable[i], EmissionTable[i][1])
        
    def Deltas(self, obs):
        
        obsIndex = 1
        psIndex = 1
        v = []
        delta = 0

        for d in range(len(self.deltaTable)-1):
            d += 1
            for j in range(len(self.deltaTable[d])):
                for i in range(len(self.transitionTable)):
                    v.append(self.deltaTable[d-1][i] * self.transitionTable[i][j])
                delta = max(v) * self.emissionTable[j][obs[obsIndex]]
                self.deltaTable[d][j] = delta
                self.psTable[psIndex][j] = max(v)
                delta = 0
                v = []
            obsIndex += 1
            psIndex += 1
        print("Delta Table")
        print(self.deltaTable)
        print("Psi Table")
        print(self.psTable)

####################### Data Import #############################

# States = {S, R, F}
# Symbols = {U, N}

InitialTable = np.loadtxt("Viterbi_Data/InitialTable.txt", delimiter=',', dtype=np.float64)

TransitionTable = np.loadtxt("Viterbi_Data/TransitionTable.txt", delimiter=',', dtype=np.float64)

EmissionTable = np.loadtxt("Viterbi_Data/EmissionTable.txt", delimiter=',', dtype=np.float64)

####################### Data #############################
#This is the table where we keep deltas
deltaTable = np.zeros((3,3), dtype= np.float64)

#Back Tracking
psTable = np.zeros((3,3), dtype= np.float64)

# Data = NUU
data = [1, 0, 0]

test = viterbi(InitialTable, TransitionTable, EmissionTable, deltaTable, psTable)
test.Initialization()
test.Deltas(data)
