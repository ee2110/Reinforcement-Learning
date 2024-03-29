# Multi-Armed Bandit Problem

The multi-armed bandit (MAB) problem often refer to arm of a K-slot machine to pull for maximize the total reward in a series of trials. It can model the real-world learning and optimization problems. In marketing terms, a multi-armed bandit solution is a smarter or more complex version of A/B testing that uses machine learning algorithms to dynamically allocate traffic to variations that are performing well, while allocating less traffic to variations that are underperforming.

In reinforcement learning (RL), the agent always need to balance between exploitation and exploration in order to learn the optimal target values. Therefore, some mechanism are proposed to deal with this exploration-exploitation dilemma.

### Algorithms:
1. Epsilon-greedy policy
2. Softmax exploration
3. Upper confidence bound (UCB)
4. Thompson sampling

#### Epsilon-Greedy Policy
The epsilon-greedy policy is commonly applied in several RL approaches such as Q-learning and DQN. With the epsilon-greedy policy, the agent are allowed to explore the environment with a probability of epsilon to select random actions, otherwise, it will select the maximum value with a probability 1-epsilon.


#### Softmax Exploration
Softmax exploration, also known as Boltzmann exploration, is another strategy used for finding an optimal bandit by select action using probability of Boltzmann distribution.

<img src="https://github.com/ee2110/Reinforcement-Learning/blob/master/img/Probability%20boltzmann%20distribution.JPG" width="30%">


#### Upper Confidence Bound (UCB)
Instead of choosing actions based on probability, the upper confidence bound (UCB) selecting the best action based on a confidence interval. The UCB will more focus on explore the actions that has a high UCB rather than other. For example, confidence interval of an arm is [0.3, 0.8], this indicate the range of mean value of that arm, the 0.3 is the lower confidence bound, whereas 0.8 is the UCB. The UCB selects a machine that has a high UCB to explore.

<img src="https://github.com/ee2110/Reinforcement-Learning/blob/master/img/UCB.jpg" width="30%">

where N(a) is the number of times the arm was pulled and t is the total number of rounds.


#### Thompson sampling
Thompson sampling (TS) is another popularly used algorithm to overcome the exploration-exploitation dilemma. It is a probabilistic algorithm and is based on a prior distribution. The term prior distribution indicate that it is initial distributions calculated based on prior mean sample rewards for each of the k arms. Using Bernoulli rewards, the value of beta distribution [alpha, beta] lies within the interval [0,1]. Alpha represents the number of times we receive the positive rewards and beta represents the number of times we receive the negative rewards. The generalization to multiple variables is called a Dirichlet distribution. The beta distribution is a suitable model for the random behavior of percentages and proportions.


<img src="https://github.com/ee2110/Reinforcement-Learning/blob/master/img/Beta_distribution.jpg" width="30%">


### Highlights
1. The selection of optimal arm is always the same in the same game regardless the method or hyperparameter used.

2. As mentioned in [4], all of the actions are given chance equivalently by using the epsilon-greedy policy, but in softmax exploration, the action are selected based on a probability from the Boltzmann distribution. Although epsilon-greedy action selection is an effective and popular means of balancing exploration and exploitation in reinforcement learning, one drawback is that when it explores it chooses equally among all actions. This means that it is as likely to choose the worst-appearing action as it is to choose the next-to-best action. In tasks where the worst actions are very bad, this may be unsatisfactory. The obvious solution is to vary the action probabilities as a graded function of estimated value. The greedy action is still given the highest selection probability, but all the others are ranked and weighted according to their value estimates. These are called softmax action selection rules.


References:
1) https://www.optimizely.com/optimization-glossary/multi-armed-bandit/
2) Vermorel J., Mohri M. (2005) Multi-armed Bandit Algorithms and Empirical Evaluation. In: Gama J., Camacho R., Brazdil P.B., Jorge A.M., Torgo L. (eds) Machine Learning: ECML 2005. ECML 2005. Lecture Notes in Computer Science, vol 3720. Springer, Berlin, Heidelberg. https://doi.org/10.1007/11564096_42
3) Hands-On Reinforcement Learning with Python: Master reinforcement and deep reinforcement learning using OpenAI Gym and TensorFlow, by Sudharsan RavichandiranJun 2018, Packt Publishing Ltd
4) http://incompleteideas.net/book/first/ebook/node17.html