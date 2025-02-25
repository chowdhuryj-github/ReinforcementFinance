
"""
consider a biased die. for this die, the probability of 4 will be 5 times as likely as any other number of the
six sided die. this code simulates 600 bets on the outcome of the die. 
"""

# importing the required libraries
import numpy as np
from numpy.random import default_rng
from tqdm import tqdm
import time


# defining the state space where 4 is five times as likely as any other die
state_space = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6]

# defining the action space
action_space = [1, 2, 3, 4, 5, 6]

# instantiating a random number generator object
rng = default_rng(seed=100)

# defining the epoch function
def epoch():
    total_reward = 0
    for _ in range(600):
        action_taken = rng.choice(action_space)
        dice_roll = rng.choice(state_space)
        if(action_taken == dice_roll):
            total_reward += 1
    return total_reward

# multiple sequences of bets in a numpy array
rl = np.array([epoch() for _ in tqdm(range(100), desc="Processing", unit="Iteration")])

# printing out the first ten rewards
print("First Ten Rewards: ", rl[:10])

# printing out the average reward
print("Average Reward: ", rl.mean())