
"""
It is straight forward to implement a agent that only takes random actions. It can't be expected that the agent
will achieve a high total reward on average. However, every once in a while, such a agent will be lucky.
"""

import gymnasium as gym

class RandomAgent:

    # the constructor
    def __init__(self):
        self.env = gym.make('CartPole-v1')

    # function for running the episodes
    def play(self, episodes=1):

        # creating a list for recording the total rewards
        self.total_rewards = list()

        # the for loop for going through episodes
        for episode in range(episodes):

            # resetting the environment
            self.env.reset()

            # a iteration of taking 100 steps
            for step in range(1, 100):

                # the chosen action
                action = self.env.action_space.sample()

                # executing the action
                state, reward, done, truncated, info = self.env.step(action)

                # done indicates that the episode is completed
                if done:

                    # stores the total number of steps in the rewards
                    self.total_rewards.append(step)
                    break


# creating a agent object
ra = RandomAgent()

# calling the method
ra.play(15)

# printing out all the rewards
print('List of Rewards: ', ra.total_rewards)

# calculating the average reward
print("Average Reward: ", round(sum(ra.total_rewards) / len(ra.total_rewards), 2))

"""
the results illustrate that the random agent doesn't go on for long. The total reward is seen to be around 20
"""