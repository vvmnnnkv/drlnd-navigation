import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.linear1 = nn.Linear(state_size, 100)
        self.linear2 = nn.Linear(100, 50)
        self.linear3 = nn.Linear(50, action_size)
        self.leaky_relu = nn.LeakyReLU()

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.linear1(state)
        x = self.leaky_relu(x)
        x = self.linear2(x)
        x = self.leaky_relu(x)
        x = self.linear3(x)
        return x
