import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

print("Gemini Chatbot")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Chatbot:", response.text)
