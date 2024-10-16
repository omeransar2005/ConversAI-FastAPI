import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='app/.env')

# Debug print to check if the environment variable is loaded
api_key = os.getenv("GROQ_API_KEY")
print(api_key)
if api_key is None:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")
else:
    print("GROQ_API_KEY loaded successfully.")

# Set up Groq client
client = Groq(api_key=api_key)

# Set the system prompt for the chatbot
system_prompt = {
    "role": "system",
    "content": "You are a helpful assistant with good conversational skills."
}

# Initialize chat history with the system prompt
chat_history = [system_prompt]

def get_groq_chatbot_response(user_message: str) -> str:
    """
    This function takes user input, sends it to Groq API, and returns the chatbot response.
    """
    # Add user's message to the chat history
    chat_history.append({"role": "user", "content": user_message})
    
    try:
        # Send the conversation history to the Groq API
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=chat_history,
            max_tokens=100,
            temperature=1.2
        )

        # Extract the assistant's reply from the response
        assistant_response = response.choices[0].message.content

        # Append the response to the chat history
        chat_history.append({
            "role": "assistant",
            "content": assistant_response
        })

        # Return the assistant's response
        return assistant_response

    except Exception as e:
        return "Sorry, I couldn't process your request."
