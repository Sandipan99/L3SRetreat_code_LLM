from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login


m = "bigcode/starcoder"
login(token='')
tokenizer = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, device_map='auto')

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(model.device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
