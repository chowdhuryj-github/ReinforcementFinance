
"""
this is a dice roll implementation of the theory probability matching
"""

# importing the libraries
from collections import Counter

# importing the required libraies
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

# instantiating a random number generator object
rng = default_rng(seed=100)

# defining the state space
state_space = [1, 6, 6, 6, 6, 6]

# defining a function for the epochs
def epoch(n):
    total_reward = 0
    action_space = [1, 2, 3, 4, 5, 6]
    for _ in range(n):
        frequency = Counter(action_space)
        action_chosen = frequency.most_common()[0][0]
        random_die_toss = rng.choice(state_space)
        if action_chosen == random_die_toss:
            dice_reward = reward(action_chosen)
            total_reward += dice_reward
        
        # updating the action space
        action_space.append(random_die_toss)
    
    # returning the total reward
    return total_reward


# defining a function for returning the reward
def reward(action_chosen):

    # the reward from the dice roll
    if action_chosen == 1:
        return 1
    elif action_chosen == 2:
        return 2
    elif action_chosen == 3:
        return 3
    elif action_chosen == 4:
        return 4
    elif action_chosen == 5:
        return 5
    elif action_chosen == 6:
        return 6

# multiple sequences of bets in a numpy array
rl = np.array([epoch(100) for _ in range(250)])

# selecting the first ten elements
print("First Ten Elements: ", rl[:10])

# printing out the mean
print("The Mean: ", rl.mean())


# storing a list of iterations
iterations = []
for i in range(1, 251):
    iterations.append(i)

# plotting the graph
plt.plot(iterations, rl)
print("Mean Reward is: ", rl.mean(), "\n")
plt.axhline(y=rl.mean(), color="r", linestyle="--", label="Mean Reward")
plt.title("The Total Reward over each Iteration")
plt.xlabel("Iterations")
plt.ylabel("Reward")
plt.legend()

# setting up the title
plt.title(f"Total Reward of State Space")

# saving the figure
plt.savefig(f"C:\GitHub\ReinforcementFinance\ch_01\plots\RewardStateSpaceDie.png")

# displaying the plot
plt.show()

