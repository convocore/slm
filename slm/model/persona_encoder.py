import torch.nn as nn

class PersonaEncoder(nn.Module):
    def __init__(self, persona_dim=128, d_model=512):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(persona_dim, d_model),
            nn.ReLU(),
            nn.Linear(d_model, d_model)
        )

    def forward(self, x):
        return self.net(x)
