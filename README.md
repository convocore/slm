# SLM: Social Language Models

SLM is a lightweight framework for building and training conversational agents that interact with each other in a simulated environment. It is designed for research, experimentation, and local development. This repository provides all code needed to create persona driven agents, run multi agent conversations, and train them through self play.

SLM is built on Python and PyTorch. It does not include any large pretrained models. Instead, it provides the structure needed to create and train your own small models or experiment with new ideas in social agent design.

## Features

1. Transformer based language model backbone
2. Persona vectors for controlling agent style and behavior
3. Social intent vectors to influence interaction patterns
4. Episodic memory module for simple internal state
5. Multi agent conversation environment
6. Simple reward function for training through self play
7. Easy to modify components for custom agent behavior

## Requirements

Python 3.9 or newer is recommended.

Required libraries:

- torch
- numpy
- pyyaml

These are listed in requirements.txt.

## Installation

Clone this repository:

git clone https://github.com/convocore/slm.git

Install dependencies:

pip install -r requirements.txt

Or install using the modern pyproject.toml:

pip install .

## Project Structure

slm/
    model/        Core model components
    env/          Conversation environment and reward functions
    utils/        Helper functions
    training/     Self play training loop
examples/
    personas/     Example persona definitions
data/
    conversations/ Conversation logs can be saved here
tests/            Basic test suite

## Running a Simple Example

There is a simple example script in:

examples/run_conversation.py

It can be extended to load agents, run conversations, and print results.

## Creating Agents

To create an agent, you will define:

- persona vector
- social intent vector
- model instance
- optimizer
- generate method

Personas can be loaded from the YAML files in examples/personas.

## Training

To run the self play training loop:

python -m slm.training.train_selfplay

This will create agents, run conversations, compute a reward, and update the model parameters.

## Customization

All major components are designed to be easy to replace or modify. Examples:

- Change the model architecture
- Replace the memory module
- Build custom reward functions
- Modify the environment rules
- Create new personas
- Add new sampling or generation logic

## Goal of the Project

SLM is intended as a starting point for experimenting with multi agent language systems that interact socially. It is a research tool and a sandbox for new ideas.

## License

See LICENSE for details.
