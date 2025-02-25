
"""
with probability matching, the agent will not achieve a perfect outcome, but the agent will improve the average
total reward by more than 75%
"""

# importing the required libraries
import numpy as np
from numpy.random import default_rng
from tqdm import tqdm

# defining the state space where 4 is five times as likely as any other die
state_space = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6]

# instantiating a random number generator object
rng = default_rng(seed=100)

# defining the epoch function
def epoch():
    # defining the action space
    action_space = [1, 2, 3, 4, 5, 6]
    total_reward = 0
    for _ in range(600):
        action_taken = rng.choice(action_space)
        dice_roll = rng.choice(state_space)
        if(action_taken == dice_roll):
            total_reward += 1
        action_space.append(dice_roll)
    return total_reward

# multiple sequences of bets in a numpy array
rl = np.array([epoch() for _ in tqdm(range(100), desc="Processing", unit="Iteration")])

# printing out the first ten rewards
print("First Ten Rewards: ", rl[:10])

# printing out the average reward
print("Average Reward: ", rl.mean())