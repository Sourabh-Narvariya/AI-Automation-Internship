import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY")


model = genai.GenerativeModel('gemini-2.5-flash')
prompt = input("Enter your prompt: ")
response = model.generate_content(prompt)
print(response.text)
