# basic_chatbot.py

# Define a dictionary with some predefined responses
responses = {
    "hello": "Hello vishwash! How can I assist you today?",
    "hi": "Hi vishwash! How can I help?",
    "how are you": "I'm just a program, but I'm functioning as expected!",
    "bye": "Goodbye vishwash! Have a great day!",
    "what is your name": "I am a chatbot, your virtual assistant!",
    "who created you": "I was created by a developer using Python.",
    "what can you do": "I can chat with you and help with basic tasks. Ask me anything!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the time": "Sorry, I can't tell time yet, but you can check your device!",
    "thank you": "You're welcome! If you have more questions, feel free to ask.",
    "default": "Sorry, I don't understand that. Can you please rephrase?",
    "my favourite song": "Kabhi Jo Baadal Barse "
}

def chatbot_response(user_input):
  
    user_input = user_input.lower()
    
    
    return responses.get(user_input, responses["default"])

def main():
    print("Chatbot: Hello vishwash! Type 'bye' to exit the chat.")
    
    while True:
        
        user_input = input("You: ")
        
        
        response = chatbot_response(user_input)
        
        
        print(f"Chatbot: {response}")
        
        
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()

 
