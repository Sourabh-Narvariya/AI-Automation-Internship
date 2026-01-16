from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
from IPython.display import display


# TEXT GENERATION 
text_model = pipeline("text-generation", model="gpt2")

text_prompt = input("Enter text prompt: ")
text_output = text_model(text_prompt, max_length=80)

print("\nGenerated Text:")
print(text_output[0]["generated_text"])


# IMAGE GENERATION 
model_id = "runwayml/stable-diffusion-v1-5"

image_model = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

image_model = image_model.to("cuda") 

image_prompt = input("\nDescribe image to generate: ")

image = image_model(image_prompt).images[0]

# 

display(image)

print("Image displayed successfully")
