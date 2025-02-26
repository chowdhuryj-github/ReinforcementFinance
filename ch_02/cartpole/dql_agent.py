
"""
we implement a DQL agent in multiple steps. this allows for a more detailed discussion of the single elements
that make up the agent. such an approach is justified because this DQL agent will serve as a blueprint for the
DQL agent that will be applied to financial problems
"""

# all necessary imports
import os
import random
import warnings
import numpy as np
import tensorflow as tf
import gymnasium as gym
from tensorflow import keras
from collections import deque



# the warnings
warnings.simplefilter('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['PYTHONHASHSEED'] = '0'

# new imports
from tensorflow.python.framework.ops import disable_eager_execution

# speeds up training of the neural network
disable_eager_execution()

# defining the optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)

# random seed
random.seed(100)
tf.random.set_seed(100)


# setting up the DQL agent class
class DQLAgent:

    
    # setting up the constructor
    def __init__(self):

        # the initial epsilon with which exploration is implemented
        self.epsilon = 1.0

        # the factor by which epsilon is diminished
        self.epsilon_decay = 0.9975

        # minimum for epsilon
        self.epsilon_min = 0.1

        # the deque object that collect past experiences
        self.memory = deque(maxlen=2000)

        # numer of experiences used for replay
        self.batch_size = 32

        # factor to discount future rewards
        self.gamma = 0.9

        # list object to collect total rewards
        self.total_rewards = list()

        # parameter to store maximum total reward achieved
        self.max_total_rewards = 0

        # initiates the instantiation of the DNN
        self.create_model()

        # instantiating the cartpole environment
        self.env = gym.make('CartPole-v1')


    # function for creating the model
    def _create_model(self):
        self.model = Sequential()
        self.model.add(Dense(24, activation='relu', input_dim=4))
        self.model.add(Dense(24, activation='relu'))
        self.model.add(Dense(2, activation='linear'))
        self.model.compile(loss='mse', optimizer=optimizer)