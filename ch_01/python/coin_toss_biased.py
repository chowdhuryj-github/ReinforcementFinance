
"""
Now assume that the coin is biased, so that we get heads in 80% of the coin tosses.
Bettting just on heads would get a total reward of $80 and tails $20
But what about random betting strategy?
"""

# importing required libraries
import numpy as np
from numpy.random import default_rng

# instantiating a random number generator object
rng = default_rng(seed=100)

# defining the biased state space
state_space = [1, 1, 1, 1, 0]

# action space
action_space = [1, 0]

# defining the epoch function
def epoch():
    total_reward = 0
    for _ in range(100):
        random_bet = rng.choice(action_space)
        random_coin_toss = rng.choice(state_space)
        if random_bet == random_coin_toss:
            total_reward += 1
    return total_reward

# multiple sequence of bets
rl = np.array([epoch() for _ in range(250)])

# displaying the first ten elements
print("First Ten Elements: ", rl[:10])

# displaying the mean
print("The Mean: ", rl.mean())

"""
the total reward is the same as before on average. Without learning, the agent in unable to capitalize on the
bias
"""