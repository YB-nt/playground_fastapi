from enum import Enum

from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Notebook(BaseModel):
    """메모"""

    id: int
    title: str
    contents: str
    created_at: datetime


# 굳이 정의 X
# class NoteBookIndex(BaseModel):
#     """메모 목록"""

#     notebook_id: int
#     title: str
#     index: bool
#     created_at: datetime


@app.get("/notes/list")
async def list_notebook():
    """메모 목록 보여주기"""

    return {}


@app.get("/notes")
async def get_notebook(notebook_id: int, notebook: Notebook):
    """메모 보여주기"""

    return {}


@app.post("/notes")
async def write_notebook(notebook_id: int, notebook: Notebook):
    """메모 추가"""
    # TODO : 데이터 베이스 조회 ->  저장된 리스트 보여주기 title 명만

    return {"notebook_id": notebook_id, "notebook": notebook}


@app.put("/notes")
async def edit_notebook(notebook_id: int, notebook: Notebook):
    """메모 수정"""
    # TODO :기존에 존재하는 데이터인지 확인  -> 예외처리
    #      NOTEBOOK 에 대해서 UPDATE 진행
    #      데이터 선택기준 : title 비교 ? Id 값비교

    return {"notebook_id": notebook_id, "notebook": notebook}


@app.delete("/notes")
async def delete_notebook(notebook_id: int, notebook: Notebook):
    """메모 삭제"""
    # TODO :기존에 존재하는 데이터인지 확인  -> 예외처리
    #      NOTEBOOK 에 대해서 DELETE 진행

    return {"notebook_id": notebook_id, "notebook": notebook}
