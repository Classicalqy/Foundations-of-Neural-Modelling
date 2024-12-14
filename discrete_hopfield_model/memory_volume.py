from memory import Hopfield_Model,np
def recall_test(memory, noise_level, times):
    flip_mask = np.random.rand(N) < noise_level
    noisy = np.where(flip_mask, 1 - memory, memory)
    hopfield.process(noisy,time=times)
    if np.array_equal(noisy, memory):
        return 1
    else:
        return 0
    
#initialization
N, num_of_memories = 50, 1
noise_level = 0.1
tries_per_memory = 1000
times = 100
ans = []
for num_of_memories in range(1,14):
    np.random.seed(42)
    memories = np.random.choice([0, 1],size=(num_of_memories, N))

    hopfield = Hopfield_Model(num_of_neurons=N)
    hopfield.hebbian(memories)

    total_success = 0
    total_tries = num_of_memories * tries_per_memory
    for memory in memories:
        for _ in range(tries_per_memory):
            total_success += recall_test(memory, noise_level, times)
    ans.append(total_success/total_tries)
    print('num_of_memories:',num_of_memories,', success_ratio:',total_success/total_tries)
    
import matplotlib.pyplot as plt
x = np.arange(1,14)
plt.bar(x, ans, color='blue', alpha=0.7)
plt.xlabel('Number of Memories')
plt.ylabel('Success Ratio')

plt.savefig('/Users/qiyuchen/Desktop/2.png')
