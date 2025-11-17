# Simple Keyword-Based Chatbot with Logging System
# This chatbot detects keywords and responds with pre-written messages

# Import datetime for timestamped logging
from datetime import datetime

# Function to log interactions
def log_interaction(user_input, bot_response):
    """
    Logs each conversation with timestamp
    Args:
        user_input: What the user typed
        bot_response: What the bot replied
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[LOG {timestamp}] User: '{user_input}' | Bot: '{bot_response}'")

# Main chatbot function
def chatbot():
    """
    Main chatbot that detects keywords and responds accordingly
    """
    print("=" * 50)
    print("KEYWORD CHATBOT - Now with Logging!")
    print("=" * 50)
    print("Try keywords like: hello, help, study")
    print("Type 'quit' to exit\n")
    
    # Keep track of conversation count
    conversation_count = 0
    
    # Main loop - keeps chatbot running
    while True:
        # Get user input and convert to lowercase for easier matching
        msg = input("Say something: ").lower()
        
        # Exit condition
        if msg == "quit":
            print("\n👋 Thanks for chatting! Goodbye!")
            print(f"Total conversations: {conversation_count}")
            break
        
        # Increment conversation counter
        conversation_count += 1
        
        # Initialize response variable
        response = ""
        
        # Check for "hello" keyword
        if "hello" in msg or "hi" in msg:
            response = "Hello! Ready to study?"
            print(response)
        
        # Check for "help" keyword
        elif "help" in msg:
            response = "Sure! What topic do you need help with?"
            print(response)
        
        # Check for "study" keyword
        elif "study" in msg or "learn" in msg:
            response = "Let's learn something new today!"
            print(response)
        
        # Check for "bye" or "goodbye"
        elif "bye" in msg or "goodbye" in msg:
            response = "See you later! Keep studying!"
            print(response)
        
        # Default response for unknown keywords
        else:
            response = "I'm still learning! Try different words!"
            print(response)
        
        # Log this interaction
        log_interaction(msg, response)
        print()  # Empty line for readability

# Run the chatbot
if __name__ == "__main__":
    chatbot()