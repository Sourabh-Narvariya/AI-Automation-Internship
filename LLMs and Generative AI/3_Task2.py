#  Use Hugging Face pipeline to generate text from a prompt using transformers.
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "the future of AI development in india is"
result = generator(prompt, max_new_tokens=50, do_sample=True, temperature=0.7)
print(result[0]["generated_text"])