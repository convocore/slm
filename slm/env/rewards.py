def compute_social_rewards(conversation):
    """
    Simple novelty reward (placeholder).
    """
    if not conversation:
        return 0.0

    unique_lines = len({t for _, t in conversation})
    total = len(conversation)

    return float(unique_lines) / float(total)
