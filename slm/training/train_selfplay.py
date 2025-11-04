import torch
from slm.env.conversation_env import ConversationEnv

def train(agents, steps=20):
    env = ConversationEnv(agents)

    for s in range(steps):
        logs, reward = env.run_episode({a.name: "Begin." for a in agents})

        for agent in agents:
            loss = -reward
            agent.optimizer.zero_grad()
            loss.backward()
            agent.optimizer.step()

        print("Step", s, "Reward:", reward)
