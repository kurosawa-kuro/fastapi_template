from typing import Optional
from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None,example='クリーニングを取りに行く')
    

class TaskCreate(BaseModel):
    title: Optional[str] = Field(None,example='クリーニングを取りに行く')

class TaskCreateResponse(BaseModel):
    id: int
    title: Optional[str] = Field(None,example='クリーニングを取りに行く')

    class Config:
        orm_mode = True

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None,example='クリーニングを取りに行く')
    done:bool = Field(False,description='完了フラグ')

    class Config:
        orm_mode = True



