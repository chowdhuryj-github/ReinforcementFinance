
"""
A learning agent can gain a edge by basing the betting strategy on the previous outcomes observed.
We can record all the observed outcomes and choose randomly from the set of previous outcomes.
Hence, the bias is reflected in the number of times the agent randomly bets on heads compared to tails
"""

# importing required libraries
import numpy as np
from numpy.random import default_rng

# instantiating a random number generator object
rng = default_rng(seed=100)

# the biased state space
state_space = [1, 1, 1, 1, 0]

# defining the epoch function
def epoch(n):
    total_reward = 0
    action_space = [1, 0]
    for _ in range(n):
        random_bet = rng.choice(action_space)
        random_coin_toss = rng.choice(state_space)
        if random_bet == random_coin_toss:
            total_reward += 1
        action_space.append(random_coin_toss)
    
    return total_reward

# multiple sequences of bets in a numpy array
rl = np.array([epoch(100) for _ in range(250)])

# selecting the first ten elements
print("First Ten Elements: ", rl[:10])

# printing out the mean
print("The Mean: ", rl.mean())

"""
This strategy, while not optimal is observed in experiments involving human beings. This is called
probability matching.
"""