import torch
import torch.nn as nn
import torch.nn.functional as F

class EpisodicMemory(nn.Module):
    """
    Slot-based memory with attention retrieval.
    """

    def __init__(self, memory_slots=32, d_model=512):
        super().__init__()
        self.memory = nn.Parameter(torch.randn(memory_slots, d_model))
        self.qproj = nn.Linear(d_model, d_model)

    def retrieve(self, query=None):
        if query is None:
            return self.memory.mean(dim=0)

        q = self.qproj(query)
        attn = torch.matmul(self.memory, q)
        w = F.softmax(attn, dim=0)
        return (w.unsqueeze(1) * self.memory).sum(dim=0)
