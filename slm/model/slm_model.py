import torch
import torch.nn as nn
from .tokenizer import SimpleTokenizer

class SLMModel(nn.Module):
    """
    Base SLM transformer decoder.
    """

    def __init__(self, vocab_size=8000, d_model=512, n_layers=4, n_heads=8):
        super().__init__()

        self.tokenizer = SimpleTokenizer(vocab_size)

        self.embedding = nn.Embedding(vocab_size, d_model)
        self.positional = nn.Embedding(2048, d_model)

        layer = nn.TransformerDecoderLayer(
            d_model=d_model,
            nhead=n_heads,
            batch_first=True
        )
        self.decoder = nn.TransformerDecoder(layer, num_layers=n_layers)

        self.output = nn.Linear(d_model, vocab_size)

    def forward(self, tokens):
        seq_len = tokens.size(1)
        pos = torch.arange(seq_len, device=tokens.device).unsqueeze(0)
        x = self.embedding(tokens) + self.positional(pos)
        decoded = self.decoder(x, x)
        return self.output(decoded)
