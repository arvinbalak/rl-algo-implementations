import numpy as np

class MDP:
    '''A simple MDP class.  It includes the following members'''

    def __init__(self,T,R,discount):
        '''Constructor for the MDP class

        Inputs:
        T -- Transition function: |A| x |S| x |S'| array
        R -- Reward function: |A| x |S| array
        discount -- discount factor: scalar in [0,1)

        The constructor verifies that the inputs are valid and sets
        corresponding variables in a MDP object'''

        assert T.ndim == 3, "Invalid transition function: it should have 3 dimensions"
        self.nActions = T.shape[0]
        self.nStates = T.shape[1]
        assert T.shape == (self.nActions,self.nStates,self.nStates), "Invalid transition function: it has dimensionality " + repr(T.shape) + ", but it should be (nActions,nStates,nStates)"
        assert (abs(T.sum(2)-1) < 1e-5).all(), "Invalid transition function: some transition probability does not equal 1"
        self.T = T
        assert R.ndim == 2, "Invalid reward function: it should have 2 dimensions" 
        assert R.shape == (self.nActions,self.nStates), "Invalid reward function: it has dimensionality " + repr(R.shape) + ", but it should be (nActions,nStates)"
        self.R = R
        assert 0 <= discount < 1, "Invalid discount factor: it should be in [0,1)"
        self.discount = discount


''' Construct a simple maze MDP

  Grid world layout:

  ---------------------
  |  0 |  1 |  2 |  3 |
  ---------------------
  |  4 |  5 |  6 |  7 |
  ---------------------
  |  8 |  9 | 10 | 11 |
  ---------------------
  | 12 | 13 | 14 | 15 |
  ---------------------

  Goal state: 15 
  Bad state: 9
  End state: 16

  The end state is an absorbing state that the agent transitions 
  to after visiting the goal state.

  There are 17 states in total (including the end state) 
  and 4 actions (up, down, left, right).'''
class MDPMaze(MDP):
    def __init__(self):
        # Transition function: |A| x |S| x |S'| array
        T = np.zeros([4, 17, 17])
        a = 0.8;  # intended move
        b = 0.1;  # lateral move

        # up (a = 0)

        T[0, 0, 0] = a + b;
        T[0, 0, 1] = b;

        T[0, 1, 0] = b;
        T[0, 1, 1] = a;
        T[0, 1, 2] = b;

        T[0, 2, 1] = b;
        T[0, 2, 2] = a;
        T[0, 2, 3] = b;

        T[0, 3, 2] = b;
        T[0, 3, 3] = a + b;

        T[0, 4, 4] = b;
        T[0, 4, 0] = a;
        T[0, 4, 5] = b;

        T[0, 5, 4] = b;
        T[0, 5, 1] = a;
        T[0, 5, 6] = b;

        T[0, 6, 5] = b;
        T[0, 6, 2] = a;
        T[0, 6, 7] = b;

        T[0, 7, 6] = b;
        T[0, 7, 3] = a;
        T[0, 7, 7] = b;

        T[0, 8, 8] = b;
        T[0, 8, 4] = a;
        T[0, 8, 9] = b;

        T[0, 9, 8] = b;
        T[0, 9, 5] = a;
        T[0, 9, 10] = b;

        T[0, 10, 9] = b;
        T[0, 10, 6] = a;
        T[0, 10, 11] = b;

        T[0, 11, 10] = b;
        T[0, 11, 7] = a;
        T[0, 11, 11] = b;

        T[0, 12, 12] = b;
        T[0, 12, 8] = a;
        T[0, 12, 13] = b;

        T[0, 13, 12] = b;
        T[0, 13, 9] = a;
        T[0, 13, 14] = b;

        T[0, 14, 13] = b;
        T[0, 14, 10] = a;
        T[0, 14, 15] = b;

        T[0, 15, 16] = 1;
        T[0, 16, 16] = 1;

        # down (a = 1)

        T[1, 0, 0] = b;
        T[1, 0, 4] = a;
        T[1, 0, 1] = b;

        T[1, 1, 0] = b;
        T[1, 1, 5] = a;
        T[1, 1, 2] = b;

        T[1, 2, 1] = b;
        T[1, 2, 6] = a;
        T[1, 2, 3] = b;

        T[1, 3, 2] = b;
        T[1, 3, 7] = a;
        T[1, 3, 3] = b;

        T[1, 4, 4] = b;
        T[1, 4, 8] = a;
        T[1, 4, 5] = b;

        T[1, 5, 4] = b;
        T[1, 5, 9] = a;
        T[1, 5, 6] = b;

        T[1, 6, 5] = b;
        T[1, 6, 10] = a;
        T[1, 6, 7] = b;

        T[1, 7, 6] = b;
        T[1, 7, 11] = a;
        T[1, 7, 7] = b;

        T[1, 8, 8] = b;
        T[1, 8, 12] = a;
        T[1, 8, 9] = b;

        T[1, 9, 8] = b;
        T[1, 9, 13] = a;
        T[1, 9, 10] = b;

        T[1, 10, 9] = b;
        T[1, 10, 14] = a;
        T[1, 10, 11] = b;

        T[1, 11, 10] = b;
        T[1, 11, 15] = a;
        T[1, 11, 11] = b;

        T[1, 12, 12] = a + b;
        T[1, 12, 13] = b;

        T[1, 13, 12] = b;
        T[1, 13, 13] = a;
        T[1, 13, 14] = b;

        T[1, 14, 13] = b;
        T[1, 14, 14] = a;
        T[1, 14, 15] = b;

        T[1, 15, 16] = 1;
        T[1, 16, 16] = 1;

        # left (a = 2)

        T[2, 0, 0] = a + b;
        T[2, 0, 4] = b;

        T[2, 1, 1] = b;
        T[2, 1, 0] = a;
        T[2, 1, 5] = b;

        T[2, 2, 2] = b;
        T[2, 2, 1] = a;
        T[2, 2, 6] = b;

        T[2, 3, 3] = b;
        T[2, 3, 2] = a;
        T[2, 3, 7] = b;

        T[2, 4, 0] = b;
        T[2, 4, 4] = a;
        T[2, 4, 8] = b;

        T[2, 5, 1] = b;
        T[2, 5, 4] = a;
        T[2, 5, 9] = b;

        T[2, 6, 2] = b;
        T[2, 6, 5] = a;
        T[2, 6, 10] = b;

        T[2, 7, 3] = b;
        T[2, 7, 6] = a;
        T[2, 7, 11] = b;

        T[2, 8, 4] = b;
        T[2, 8, 8] = a;
        T[2, 8, 12] = b;

        T[2, 9, 5] = b;
        T[2, 9, 8] = a;
        T[2, 9, 13] = b;

        T[2, 10, 6] = b;
        T[2, 10, 9] = a;
        T[2, 10, 14] = b;

        T[2, 11, 7] = b;
        T[2, 11, 10] = a;
        T[2, 11, 15] = b;

        T[2, 12, 8] = b;
        T[2, 12, 12] = a + b;

        T[2, 13, 9] = b;
        T[2, 13, 12] = a;
        T[2, 13, 13] = b;

        T[2, 14, 10] = b;
        T[2, 14, 13] = a;
        T[2, 14, 14] = b;

        T[2, 15, 16] = 1;
        T[2, 16, 16] = 1;

        # right (a = 3)

        T[3, 0, 0] = b;
        T[3, 0, 1] = a;
        T[3, 0, 4] = b;

        T[3, 1, 1] = b;
        T[3, 1, 2] = a;
        T[3, 1, 5] = b;

        T[3, 2, 2] = b;
        T[3, 2, 3] = a;
        T[3, 2, 6] = b;

        T[3, 3, 3] = a + b;
        T[3, 3, 7] = b;

        T[3, 4, 0] = b;
        T[3, 4, 5] = a;
        T[3, 4, 8] = b;

        T[3, 5, 1] = b;
        T[3, 5, 6] = a;
        T[3, 5, 9] = b;

        T[3, 6, 2] = b;
        T[3, 6, 7] = a;
        T[3, 6, 10] = b;

        T[3, 7, 3] = b;
        T[3, 7, 7] = a;
        T[3, 7, 11] = b;

        T[3, 8, 4] = b;
        T[3, 8, 9] = a;
        T[3, 8, 12] = b;

        T[3, 9, 5] = b;
        T[3, 9, 10] = a;
        T[3, 9, 13] = b;

        T[3, 10, 6] = b;
        T[3, 10, 11] = a;
        T[3, 10, 14] = b;

        T[3, 11, 7] = b;
        T[3, 11, 11] = a;
        T[3, 11, 15] = b;

        T[3, 12, 8] = b;
        T[3, 12, 13] = a;
        T[3, 12, 12] = b;

        T[3, 13, 9] = b;
        T[3, 13, 14] = a;
        T[3, 13, 13] = b;

        T[3, 14, 10] = b;
        T[3, 14, 15] = a;
        T[3, 14, 14] = b;

        T[3, 15, 16] = 1;
        T[3, 16, 16] = 1;

        # Reward function: |A| x |S| array
        R = -1 * np.ones([4, 17]);

        # set rewards
        R[:, 15] = 100;  # goal state
        R[:, 9] = -70;  # bad state
        R[:, 16] = 0;  # end state

        # Discount factor: scalar in [0,1)
        discount = 0.95

        # MDP object
        super().__init__(T,R,discount)

class MDPBase:
    def __init__(self, mdp, sampleReward=np.random.normal):
        self.mdp = mdp
        self.sampleReward = sampleReward

    def sampleRewardAndNextState(self, state, action):
        '''Procedure to sample a reward and the next state
        reward ~ Pr(r)
        nextState ~ Pr(s'|s,a)

        Inputs:
        state -- current state
        action -- action to be executed

        Outputs:
        reward -- sampled reward
        nextState -- sampled next state
        '''

        reward = self.sampleReward(self.mdp.R[action, state])
        cumProb = np.cumsum(self.mdp.T[action, state, :])
        nextState = np.where(cumProb >= np.random.rand(1))[0][0]
        return [reward, nextState]

    def sampleSoftmaxPolicy(self, policyParams, state):
        '''Procedure to sample an action from stochastic policy
        pi(a|s) = exp(policyParams(a,s))/[sum_a' exp(policyParams(a',s))])
        This function should be called by reinforce() to selection actions

        Inputs:
        policyParams -- parameters of a softmax policy (|A|x|S| array)
        state -- current state

        Outputs:
        action -- sampled action
        '''
        all_actions = list(range(self.mdp.nActions))
        softmax = self.softmax(np.array(policyParams[:, state]))

        # sample an action from probabilites
        action = np.random.choice(all_actions, p=softmax)

        return action

