from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_message: str  # User's input message

class ChatResponse(BaseModel):
    response: str  # Chatbot's response
