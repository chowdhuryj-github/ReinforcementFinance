
"""
Consider the case of an unbiased coin. Agents are allowed to bet for free on the outcome of the coin toss.
A agent might bet randomly on heads or tails. The reward is 1 USD if the agent wins and nothing if they lose.
The agent's goal is to maximize the total reward. 
"""


# importing required libraries
import numpy as np
from numpy.random import default_rng

# instantiating a random number generator object
rng = default_rng(seed=100)

# the state space being 1 or 0
state_space = [1, 0]

# the action space
action_space = [1, 0]

# defining the epoch
def epoch():
    total_reward = 0
    for _ in range(100):
        random_bet = rng.choice(action_space)
        random_coin_toss = rng.choice(state_space)
        if random_bet == random_coin_toss:
            total_reward += 1
    return total_reward

# multiple sequences of bets in a numpy array
rl = np.array([epoch() for _ in range(250)])

# first ten elements
print("First Ten Elements: ", rl[:10])

# calculating the mean
print("The Mean: ", rl.mean())
