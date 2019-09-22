# Report

Following document describes solution algorithm and its results in detail.

## Learning Algorithm

Agent is trained using Deep Q-Learning (DQN) algorithm, which is similar to Q-Learning, but has following tweaks:
1. Q-values are calculated using deep network (Q-network) instead of the Q-table. 
 The network is trained to output Q-values for each action for a given state. 
2. Experience replay - agent's actions and environment's responses are recorded and used multiple times (randomly sampled) to train an agent. 
3. Fixed Q-targets - to calculate target Q-value, algorithm uses network with slightly different weights
  to avoid training Q-network on direct outputs of itself.

Learning step:
 * Calculate target Q-value using reward and fixed Q-target network output for the next action
 * Update Q-network with back propagation using target Q-value as target with MSE loss
 * Update fixed Q-target network weights to be slightly closer to learned Q-network
 
Following hyper-params used:
 * Experience Replay buffer size: 50000
 * Batch size: 64
 * Gamma (discount factor): 0.99
 * Fixed Q-target network weights update rate: 1e-3
 * Q-network learning rate: 5e-4
 * Update frequency: every 4 steps

### Q-Network
Q-network has following layers:
 * input layer: 37 features (environment state vector dimension)
 * linear (fully connected) layer: 37 x 100, with leaky ReLU activation
 * linear (fully connected) layer: 100 x 50, with leaky ReLU activation
 * linear (fully connected) layer: 50 x 4 (number of actions)

## Results
With given algorithm, Q-network architecture and hyperparameters, the environment was solved in 370 episodes.

Following plot shows recorded episodes score and score averaged over 100 episodes:

![DQN Plot](images/plot.png?raw=true "DQN Plot")

## Ideas for Future Work
 * DQN has number of improvements to try: double DQN, prioritized experience replay, dueling DQN, noised DQN
 * Stack several states from the environment and use 1D convolution to capture temporal features
 * Train from pixel values, also stacking frames and using 3D convolution to capture temporal features
 
 