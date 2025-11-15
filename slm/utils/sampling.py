import torch
import torch.nn.functional as F

def sample_logits(logits, temperature=1.0):
    """
    Basic temperature sampling.
    """
    logits = logits / temperature
    probs = F.softmax(logits[-1], dim=-1)
    idx = torch.multinomial(probs, num_samples=1)
    return idx.item()
