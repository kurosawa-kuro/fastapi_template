from fastapi import FastAPI
from blog.routers import task

app = FastAPI()

app.include_router(task.router)
# app.include_router(done.router)
# Base.metadata.create_all(engine)

@app.get("/hello")
async def create():
    return {'data':'hello world'}

