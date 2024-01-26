def chatbot():
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

def get_response(user_input):
    # Add your logic here to generate a response based on user input
    # You can use if statements, functions, or even machine learning models

    # Here's an example that answers basic questions
    if "what is your name" in user_input.lower():
        response = "My name is Chatbot. How can I help you?"
    elif "how are you" in user_input.lower():
        response = "I'm doing well, thank you! How about you?"
    elif "what is the capital of France" in user_input.lower():
        response = "The capital of France is Paris."
    elif "how do I calculate the area of a circle" in user_input.lower():
        response = "To calculate the area of a circle, you can use the formula: A = πr^2, where A is the area and r is the radius."
    else:
        response = "I'm sorry, I don't have an answer for that question. Is there anything else I can help you with?"

    return response

# Start the chatbot
chatbot()