import torch.nn as nn

class SocialHead(nn.Module):
    def __init__(self, social_dim=64, d_model=512):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(social_dim, d_model),
            nn.Tanh(),
            nn.Linear(d_model, d_model)
        )

    def forward(self, x):
        return self.net(x)
