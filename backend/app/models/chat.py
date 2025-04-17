from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Conversation(BaseModel):
    __tablename__ = "conversations"

    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    messages = relationship("Message", back_populates="conversation")

class Message(BaseModel):
    __tablename__ = "messages"

    content = Column(Text, nullable=False)
    role = Column(String, nullable=False)  # 'user' or 'bot'
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    conversation = relationship("Conversation", back_populates="messages") 