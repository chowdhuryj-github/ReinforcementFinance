
"""
the agent can do better by simply betting on most likely outcome as derived from past results
"""

# importing the libraries
from collections import Counter

# importing required libraries
import numpy as np
from numpy.random import default_rng

# instantiating a random number generator object
rng = default_rng(seed=100)

# defining the state space
state_space = [1, 1, 1, 1, 0]

# defining the epoch function
def epoch(n):
    total_reward = 0
    action_space = [0, 1]
    for _ in range(n):
        frequency = Counter(action_space)
        action_chosen = frequency.most_common()[0][0]
        random_coin_toss = rng.choice(state_space)
        if action_chosen == random_coin_toss:
            total_reward += 1

        # update of action space with highest frequency
        action_space.append(random_coin_toss)
    return total_reward


# multiple sequences of bets in a numpy array
rl = np.array([epoch(100) for _ in range(250)])

# selecting the first ten elements
print("First Ten Elements: ", rl[:10])

# printing out the mean
print("The Mean: ", rl.mean())