
# PyBot - Rule-Based AI Chatbot

def chatbot_response(user_input):
    message = user_input.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii", "hiii"]:
        return "Hello! Welcome to PyBot. How can I help you?"

    elif "good morning" in message:
        return "Good morning! Have a productive day!"

    elif "good evening" in message:
        return "Good evening! How can I assist you?"

    # Chatbot identity
    elif "your name" in message or "who are you" in message:
        return "I am PyBot, a rule-based chatbot built using Python and Streamlit."

    # AI information
    elif "what is ai" in message or "artificial intelligence" in message:
        return (
            "Artificial Intelligence (AI) enables computers to perform "
            "tasks that usually require human intelligence."
        )

    elif "machine learning" in message:
        return (
            "Machine Learning is a branch of AI that helps computers "
            "learn patterns from data and make predictions."
        )

    elif "deep learning" in message:
        return (
            "Deep Learning uses neural networks with multiple layers "
            "to learn complex patterns from data."
        )

    # Programming
    elif "python" in message:
        return (
            "Python is a beginner-friendly programming language widely "
            "used in AI, Machine Learning, data science, and web development."
        )

    elif "streamlit" in message:
        return (
            "Streamlit is a Python framework for creating interactive "
            "web applications, including AI and data science demos."
        )

    # General conversation
    elif "how are you" in message:
        return "I am doing well! Thanks for asking. How can I help you?"

    elif "thank" in message:
        return "You're welcome! Feel free to ask me another question."

    elif "help" in message:
        return (
            "You can ask me about Python, AI, Machine Learning, "
            "Deep Learning, or Streamlit."
        )

    # Goodbye
    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Thanks for chatting with PyBot."

    # Fallback
    else:
        return (
            "I'm still learning! Please ask me about Python, AI, "
            "Machine Learning, Deep Learning, or Streamlit."
        )


