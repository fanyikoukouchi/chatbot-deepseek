from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import List, Dict
import json
from app.core.config import settings
from app.api.auth import get_current_user
import httpx

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, message: str, user_id: str):
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            # Process the message and get response from DeepSeek API
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{settings.DEEPSEEK_API_URL}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "messages": [{"role": "user", "content": data}],
                        "model": "deepseek-chat"
                    }
                )
                response_data = response.json()
                bot_response = response_data["choices"][0]["message"]["content"]
                
                # Send the response back to the user
                await manager.send_personal_message(
                    json.dumps({
                        "type": "message",
                        "content": bot_response,
                        "sender": "bot"
                    }),
                    user_id
                )
    except WebSocketDisconnect:
        manager.disconnect(user_id)

@router.get("/history")
async def get_chat_history(current_user: dict = Depends(get_current_user)):
    # TODO: Implement chat history retrieval from database
    return []

@router.post("/message")
async def send_message(message: dict, current_user: dict = Depends(get_current_user)):
    # TODO: Implement message storage in database
    return {"status": "success"} 