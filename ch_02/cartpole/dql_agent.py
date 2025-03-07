

# need to figure out how to make this work

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
from keras.layers import Dense
from keras.models import Sequential
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


class DQLAgent(DQLAgent):
    
    def act(self, state):
        if random.random() < self.epsilon:

            # choosing a random action
            return self.env.action_space.sample()
        
        # choosing a action according to the current optimal policy
        return np.argmax(self.model.predict(state)[0])
    
    def replay(self):

        # random chooses a batch of past experiences for replay
        batch = random.sample(self.memory, self.batch_size)
        for state, action, next_state, reward, done in batch:
            if not done:
                reward += self.gamma * np.amax(

                    # combines the immediate and discounted future reward
                    self.model.predict(next_state)[0])
            
            # generates the values for state-action pairs
            target = self.model.predict(state)

            # updates the values for the state-action pairs
            target[0, action] = reward

            # trains / updates the DNN to account for the updated value
            self.model.fit(state, target, epochs=2, verbose=False)
        if self.epsilon > self.epsilon_min:

            # reduces the epsilon by the epsilon_decay factor
            self.epsilon *= self.epsilon_decay


class DQLAgent(DQLAgent):

    def learn(self, episodes):
        for e in range(1, episodes + 1):

            # the environment is reset
            state, _ = self.env.reset()

            # the state object is reshaped
            state = np.reshape(state, [1, 4])
            for f in range(1, 5000):

                # action is chosen according to the .act() method
                action = self.act(state)

                # relevant data points are collected for replay
                next_state, reward, done, trunc, _ = self.env.step(action)

                # state object is rehsaped
                next_state = np.reshape(next_state, [1, 4])

                # relevant data points are collected
                self.memory.append([state, action, next_state, reward, done])

                # state variable is updated to the current state
                state = next_state
                if done or trunc:

                    # once terminated, total reward is collected
                    self.trewards.append(f)

                    # maximum total reward is updated if necessary
                    self.max_treward = max(self.max_treward, f)
                    templ = f'episode={e:4d} | treward={f:4d}'
                    templ += f' | max={self.max_treward:4d}'
                    print(templ, end="\r")
                    break
            if len(self.memory) > self.batch_size:

                # replay is initiated as soon as there are enough experienes
                self.replay()
        print()


class DQLAgent(DQLAgent):
    def test(self, episodes):
        for e in range(1, episodes + 1):
            state, _ = self.env.reset()
            state = np.reshape(state, [1, 4])
            for f in range(1, 5001):

                # only actions according to the optimal policy are chosen
                action = np.argmax(self.model.predict(state)[0])
                state, reward, done, trunc, _ = self.env.step(action)
                state = np.reshape(state, [1, 4])
                if done or trunc:
                    print(f, end='')
                    break



