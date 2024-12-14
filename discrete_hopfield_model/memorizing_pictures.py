from memory import Hopfield_Model, np
import matplotlib.pyplot as plt

num_of_memories = 2
state1 = np.array([[0, 1, 0, 1, 0, 0],[1, 0, 1, 0, 0, 1],[1, 1, 0, 0, 1, 0],[1, 1, 1, 0, 1, 1],[1, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0,]])
state2 = np.array([[1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 1],[0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0],[1, 1, 1, 1, 1, 0]])
states = [state1.flatten(), state2.flatten()]
plt.imshow(state1)
plt.colorbar() 
plt.title('Store Image 1')
plt.savefig('/Users/qiyuchen/Desktop/1.png')
plt.clf()
plt.imshow(state2)
plt.colorbar() 
plt.title('Store Image 2')
plt.savefig('/Users/qiyuchen/Desktop/2.png')
plt.clf()
initial = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
plt.imshow(initial)
plt.colorbar() 
plt.title('Initial State')
plt.savefig('/Users/qiyuchen/Desktop/0percent_initial.png')

initial = initial.flatten()
hopfield = Hopfield_Model(num_of_neurons=36)
hopfield.hebbian(states=states)
output = hopfield.process(state=initial, time=1000)
output = np.array([output[0:6],output[6:12],output[12:18],output[18:24],output[24:30],output[30:36]])

plt.imshow(output)
plt.colorbar() 
plt.title('Result')
plt.savefig('/Users/qiyuchen/Desktop/0percent_result.png')
plt.clf()