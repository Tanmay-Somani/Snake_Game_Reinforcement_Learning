# Snake Game with Double Deep Q-Learning Network

## Overview

This project implements the classic Snake game using a Double Deep Q-Learning Network (DDQN) for reinforcement learning. The agent learns to play the game by optimizing its strategy through experience, aiming to achieve the highest possible score.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Results](#results)
- [Future Work](#future-work)


## Features

- Classic Snake game mechanics.
- Agent trained using DDQN for improved learning efficiency.
- Visual representation of the game with real-time updates.
- Configurable parameters for training (learning rate, discount factor, etc.).

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snake-game-ddqn.git
   cd snake-game-ddqn
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Snake game and train the agent, use the following command:

```bash
python main.py
```

### Training the Agent

You can configure the training parameters in `config.py`. Adjust the following settings as needed:

- `LEARNING_RATE`: Learning rate for the Q-learning algorithm.
- `DISCOUNT_FACTOR`: Discount factor for future rewards.
- `EPISODES`: Number of training episodes.
- `MAX_STEPS`: Maximum steps per episode.

## Algorithm Explanation

### Double Deep Q-Learning

DDQN is an enhancement of the DQN algorithm, addressing the issue of overestimation of action values. It utilizes two separate neural networks to reduce bias in the Q-value updates:

1. **Online Network**: This network is updated continuously during training and is responsible for selecting actions.
2. **Target Network**: This network is updated less frequently and is used to compute the target Q-values, providing stability to the learning process.

### Training Process

The agent learns by interacting with the environment, storing experiences in a replay buffer, and updating the Q-values based on the rewards received. The training loop involves:

- Selecting an action using the epsilon-greedy policy.
- Executing the action and observing the reward and next state.
- Storing the experience in the replay buffer.
- Sampling a batch of experiences for training.
- Updating the Q-values based on the target computed using the target network.

## Results

After training, the agent can navigate the Snake game effectively, demonstrating learned strategies. The performance can be visualized in real-time during the training process.

## Future Work

- Implement additional features such as different game modes or levels.
- Experiment with hyperparameter tuning for improved performance.
- Expand the model to incorporate other reinforcement learning techniques.
