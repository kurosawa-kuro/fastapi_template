from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    return {'data':'list_tasks'}

@router.post("/tasks")
async def create_task():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass

