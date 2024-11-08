from enum import Enum

from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, Optional
from pydantic import BaseModel
from datetime import datetime
from database.supabase import ConnSupabase


app = FastAPI()
db = ConnSupabase().client


class MemoBase(BaseModel):
    title: str
    content: str


class Memo(MemoBase):
    id: int
    updated_at: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True


class MemoCreate(MemoBase):
    # 이렇게 분리를 해두어야지 api 문서가 체계적으로 생성된다.
    pass


class MemoEdit(MemoBase):
    pass


@app.post("/notes")
async def create_note(note: MemoCreate):
    """메모 추가"""
    try:
        response = (
            db.table("notes")
            .insert({"title": note.title, "content": note.content})
            .execute()
        )
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/notes/{memo_id}")
async def get_note(memo_id):
    """메모 보여주기"""
    try:
        response = (
            db.table("notes")
            .select("*")
            .order("created_at", desc=True)
            .eq("id", memo_id)
            .single()
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Memo not found")
        return response.data

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/notes/{memo_id}")
async def edit_note(memo_id: int, memo: MemoEdit):
    """메모 수정"""
    result = db.table("notes").select("*").eq("id", memo_id).single().execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Memo not found")
    else:
        response = (
            db.table("notes")
            .update({"title": memo.title, "content": memo.content})
            .eq("id", memo_id)
            .execute()
        )

        return response.data


@app.delete("/notes/{memo_id}")
async def delete_note(memo_id: int):
    """메모 삭제"""
    # TODO :기존에 존재하는 데이터인지 확인  -> 예외처리
    #      note 에 대해서 DELETE 진행
    result = db.table("notes").select("*").eq("id", memo_id).single().execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Memo not found")
    else:
        response = db.table("notes").delete().eq("id", memo_id).execute()

    return response.data
