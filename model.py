import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import get_peft_model, LoraConfig
from config import Config

def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    
    model = AutoModelForCausalLM.from_pretrained(
        Config.MODEL_NAME,
        load_in_8bit=(Config.QUANTIZATION == "8bit"),
        device_map="auto",
        torch_dtype=torch.float16
    )
    
    lora_config = LoraConfig(
        r=Config.LORA_RANK,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)
    
    if Config.GRADIENT_CHECKPOINTING:
        model.gradient_checkpointing_enable()
    
    model.print_trainable_parameters()
    
    return model, tokenizer