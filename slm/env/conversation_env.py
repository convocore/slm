from .rewards import compute_social_rewards

class ConversationEnv:
    """
    Multi-agent interaction environment.
    """

    def __init__(self, agents, max_turns=10):
        self.agents = agents
        self.max_turns = max_turns

    def run_episode(self, prompts):
        log = []
        state = {a.name: prompts.get(a.name, "") for a in self.agents}

        for _ in range(self.max_turns):
            for agent in self.agents:
                text = agent.generate(state[agent.name])
                log.append((agent.name, text))
                for other in self.agents:
                    if other != agent:
                        state[other.name] = text

        reward = compute_social_rewards(log)
        return log, reward
