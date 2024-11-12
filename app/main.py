from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()


class KakaoRequest(BaseModel):
    intent: Dict[str, Any]
    userRequest: Dict[str, Any]
    bot: Dict[str, Any]
    action: Dict[str, Any]


def create_basic_response(text: str) -> dict:
    """포맷생성"""
    return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": text}}]}}


@app.post("/webhook")
async def kakao_webhook(request: KakaoRequest):
    utterance = request.userRequest.get("utterance", "")

    intent_name = request.intent.get("name", "")

    if intent_name == "인사":
        response_text = "안녕하세요! 무엇을 도와드릴까요?"
    elif intent_name == "날씨":
        response_text = "오늘의 날씨를 알려드립니다."
    else:
        response_text = "죄송합니다. 이해하지 못했습니다."

    response = create_basic_response(response_text)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
