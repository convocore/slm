import json
from swarms.structs.swarm_router import SwarmRouter, SwarmType
from swarms_agents import build_swarms_agent


def run_swarms_workflow(task: str, strategy: str, agent_registry_json: str):
    """
    Execute Swarms workflow using Arctic registry definitions.
    agent_registry_json = JSON string: [{id,label,systemPrompt}, ...]
    """

    registry = json.loads(agent_registry_json)

    # Convert Arctic agents → Swarms Agents (Python)
    python_agents = []
    for entry in registry:
        python_agents.append(
            build_swarms_agent(
                id=entry["id"],
                label=entry["label"],
                system_prompt=entry["systemPrompt"],
            )
        )

    strategy_map = {
        "sequential": SwarmType.SequentialWorkflow,
        "concurrent": SwarmType.ConcurrentWorkflow,
        "moa": SwarmType.MixtureOfAgents,
    }

    swarm_type = strategy_map.get(strategy, SwarmType.SequentialWorkflow)

    # If MOA, pick last as aggregator
    aggregator = python_agents[-1] if strategy == "moa" else None

    router = SwarmRouter(
        swarm_type=swarm_type,
        agents=python_agents,
        aggregator_agent=aggregator,
    )

    out = router.run(task)
    return out
