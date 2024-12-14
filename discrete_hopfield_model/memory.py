import numpy as np

#define a Hopfield Model
class Hopfield_Model:
    def __init__(self, num_of_neurons):
        self.num_of_neurons = num_of_neurons
        self.weights = np.zeros((num_of_neurons, num_of_neurons))
        
    #Hebbian Theory
    def hebbian(self, states):
        for state in states:
            adjusted_state = state*2 - 1
            self.weights += np.outer(adjusted_state, adjusted_state)
        np.fill_diagonal(self.weights, 0)
        self.weights /= self.num_of_neurons
        
    #update Algorithm
    def update(self, state):
        for i in range(self.num_of_neurons):
            judge = np.dot(self.weights, state)
            if judge[i] >= 0:
                state[i] = 1
            else: state[i] = 0
        return state
    
    #processing    
    def process(self, state, time):
        for _ in range(time):
            state = self.update(state)
        return state

'''    
N = 100
num_of_memories = 1
noise_level = 0.1
tries_per_memory = 50

memories = np.random.choice([0, 1],size=(num_of_memories, N))

hopfield = Hopfield_Model(num_of_neurons=N)
hopfield.hebbian(memories)
test = np.random.choice([0,1],size=(100,))
output = hopfield.process(test,time=100)
print(memories)
print(output)
'''