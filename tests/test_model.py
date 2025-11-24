import torch
from slm.model.slm_model import SLMModel

def test_model_forward():
    model = SLMModel()
    tokens = torch.randint(0, 100, (1, 5))
    out = model(tokens)
    assert out.shape == (1, 5, model.tokenizer.vocab_size)
