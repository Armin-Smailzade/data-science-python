import numpy as np
 
class Decoder(object):

    def __init__(self, initialProb, transProb, obsProb):
        self.N = initialProb.shape[0]
        self.initialProb = initialProb
        self.transProb = transProb
        self.obsProb = obsProb
        assert self.initialProb.shape == (self.N, 1)
        assert self.transProb.shape == (self.N, self.N)
        assert self.obsProb.shape[0] == self.N
 
    def Obs(self, obs):
        return self.obsProb[:, obs, None]
 
    def Decode(self, obs):
        trellis = np.zeros((self.N, len(obs)))
        backpt = np.ones((self.N, len(obs)), 'int32') * -1
 
        # initialization
        trellis[:, 0] = np.squeeze(self.initialProb * self.Obs(obs[0]))
 
        for t in xrange(1, len(obs)):
            trellis[:, t] = (trellis[:, t-1, None].dot(self.Obs(obs[t]).T) * self.transProb).max(0)
            backpt[:, t] = (np.tile(trellis[:, t-1, None], [1, self.N]) * self.transProb).argmax(0)
        # termination
        tokens = [trellis[:, -1].argmax()]
        for i in xrange(len(obs)-1, 0, -1):
            tokens.append(backpt[tokens[-1], i])
        return tokens[::-1]
         
#number of states 2:  A, B
#number of symbols 3: x, y, z
#initial state probability 
pi = np.array([[0.5,0.5]]).T
trans = np.array([[0.641,0.359],[0.729,0.271]])
obs = np.array([[0.117,0.691,0.192],[0.097,0.42,0.483]])
#xyxzzxyxyy
data =[0,1,0,2,2,0,1,0,1,1]
v = Decoder(pi,trans,obs)
print v.Decode(data)
