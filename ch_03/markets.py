
"""
the goal here is to implement a Finance environment as a prediction game. 
 - the environment uses static historical financial time series data to generate the states of the environment
 - the state is given by four floating point numbers representing four most recent data points in the time series
 - the value to be predicted is either 0 or 1

 - 0 means the financial time series value drops to a lower level ("market goes down")
 - 1 means the time series value rises to a higher level ("market goes up")
"""


# importing the necessary libraries
import os
import random
import numpy as np
import pandas as pd

# setting the seed for reproducibility
random.seed(100)

# setting deterministic hashing in python
os.environ['PYTHONHASHSEED'] = '0'

# action space class
class ActionSpace:
    def sample(self):
        return random.randint(0, 1)
    
# creating a action space result
action_space = ActionSpace()

# printing out the results of the action space
# the .sample() returns a random action
print([action_space.sample() for _ in range(10)])


# the finance class
class Finance:

    # the url link for the data set
    url = 'https://certificate.tpq.io/rl4finance.csv'

    # the constructor
    def __init__(self, symbol, feature, min_accuracy=0.485, n_features=4):

        # symbol for the time series to be used for the prediction game
        self.symbol = symbol

        # the type of feature to be used to define the state of the environment
        self.feature = feature

        # the number of feature values to be provided to the agent
        self.n_features = n_features

        # the action space object that is used for random action sampling
        self.action_space = ActionSpace()

        # minimum prediction accuracy required for agent to continue with the prediction game
        self.min_accuracy = min_accuracy

        # retrieval of financial time series data from the remote source
        self._get_data()

        # method call for data preparation
        self._prepare_data()