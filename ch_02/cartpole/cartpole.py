
# importing the required libraries
import gymnasium as gym

# creating the cartpole environment
env = gym.make('CartPole-v1')

# viewing the action spave
print("The Action Space: ", env.action_space.n)

# taking 10 samples of the action space
print("10 Samples: ", [env.action_space.sample() for _ in range(10)])

# the observation space of the environment (state space)
# parameters: cart position, cart velocity, pole angle, pole angular velocity
print("Observation Space: ", env.observation_space)

# the shape of the observation space
print("Shape of Observation Space: ", env.observation_space.shape)  

# resetting the environment to a default randomized state
print("Resetting the Environment: ", env.reset(seed=100))

# moving the environment taking a step using a action
print("Move Cart Left: ", env.step(0))

# moving the environment taking a step using a action
print("Move Car Right: ", env.step(1))