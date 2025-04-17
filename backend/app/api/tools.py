from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
import httpx
from app.core.config import settings
from app.api.auth import get_current_user

router = APIRouter()

@router.get("/list")
async def list_tools(current_user: dict = Depends(get_current_user)):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.DEEPSEEK_API_URL}/tools",
                headers={
                    "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                }
            )
            return response.json()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch tools: {str(e)}"
        )

@router.post("/execute")
async def execute_tool(
    tool_request: dict,
    current_user: dict = Depends(get_current_user)
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.DEEPSEEK_API_URL}/tools/execute",
                headers={
                    "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=tool_request
            )
            return response.json()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to execute tool: {str(e)}"
        )

@router.get("/status/{tool_id}")
async def get_tool_status(
    tool_id: str,
    current_user: dict = Depends(get_current_user)
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.DEEPSEEK_API_URL}/tools/{tool_id}/status",
                headers={
                    "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                }
            )
            return response.json()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get tool status: {str(e)}"
        ) 