import gym
import numpy as np
env = gym.make('FrozenLake-v0')

# Set learning parameters
lr = 0.8
gamma = 0.95
num_episodes = 2000
#Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])
#create lists to contain total rewards and steps per episode
#jList = []
rList = []
for i in range(num_episodes):
    #Reset environment and get first new observation
    s = env.reset()
    total_reward = 0
    d = False
    j = 0
    #The Q-Table learning algorithm
    while j < 99:
        j+=1
        #Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        #Get new state and reward from environment
        s1,r,d,_ = env.step(a)
        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] + lr*(r + gamma*np.max(Q[s1,:]) - Q[s,a])
        total_reward += r
        s = s1
        if d == True:
            break
    #jList.append(j)
    rList.append(total_reward)

    print ("Score over time: " +  str(sum(rList)/num_episodes))

    print ("Final Q-Table Values")
print (Q)