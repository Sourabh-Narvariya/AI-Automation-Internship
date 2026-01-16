import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_API_KEY") 

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

prompt_template = """
You are an expert {role}.
Explain {topic} in a {style} way for {audience}.
Keep the explanation {length}.
"""

variations = [
    {
        "role": "AI engineer",
        "topic": "Artificial Intelligence",
        "style": "simple",
        "audience": "school students",
        "length": "short"
    },
    {
        "role": "Data Scientist",
        "topic": "Machine Learning",
        "style": "technical",
        "audience": "college students",
        "length": "medium"
    },
    {
        "role": "Teacher",
        "topic": "Deep Learning",
        "style": "easy",
        "audience": "beginners",
        "length": "detailed"
    }
]

# Test each variation
for i, var in enumerate(variations, start=1):
    print(f"\n--- Prompt Variation {i} ---")

    final_prompt = prompt_template.format(**var)
    response = model.generate_content(final_prompt)

    print("Prompt Used:")
    print(final_prompt)

    print("Generated Output:")
    print(response.text)
