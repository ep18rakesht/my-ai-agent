import ollama

# Stores the full conversation so the agent remembers context
conversation_history = []

def chat(user_message):
    """Send a message and get a response from the local AI agent."""
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Call the local Ollama model
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Answer questions clearly and honestly. If you don't know something, say so."
            }
        ] + conversation_history
    )
    
    # Extract the reply
    assistant_message = response["message"]["content"]
    
    # Add reply to history (memory!)
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message


def main():
    """Main loop — keeps the chatbot running until you type 'quit'."""
    print("=" * 50)
    print("  🤖 Your Local AI Agent is ready!")
    print("  Powered by Llama 3.2 on YOUR laptop.")
    print("  Type your question and press Enter.")
    print("  Type 'quit' to exit.")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Agent: Goodbye! 👋")
            break
        
        if not user_input:
            continue
        
        print("\nAgent: thinking...")
        response = chat(user_input)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()