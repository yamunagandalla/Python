print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hi! How can I help you?")
    
    elif "name" in user:
        print("Chatbot: I am a Python chatbot.")
    
    elif "help" in user:
        print("Chatbot: I can chat with you and answer simple questions.")
    
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break
    
    else:
        print("Chatbot: Sorry, I didn't understand that.")
