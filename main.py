from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    description:str
    published_at:Optional[bool]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blog/category")
async def show():
    return {"data": "all category"}

@app.get("/blog/{id}")
async def show(id:int):
    return {"data": id}

@app.get("/blog/{id}/comments")
async def comments(id):
    return {"data": {id:"comments"}}

@app.post("/blog")
async def create_blog(blog:Blog):
    return {"data": "created"}

