from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from database import init, todo_create, todo_list, todo_get, todo_update, todo_delete
from model import Todo, TodoUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/add_todo")
async def add_todo(data: Todo) -> Todo:
    todo = await todo_create(data)
    return todo


@app.get("/list_todos")
async def list_todos() -> list[Todo]:
    todos = await todo_list()
    return todos


@app.get("/get_todo")
async def get_todo(title: str) -> Todo:
    todo = await todo_get(title)
    if todo:
        return todo
    raise HTTPException(404, "No such Todo in DB")


@app.put("/update_todo")
async def update_todo(title: str, updated: TodoUpdate) -> Todo:
    todo = await todo_update(title, updated)
    if todo:
        return todo
    raise HTTPException(
        status.HTTP_406_NOT_ACCEPTABLE, "Cant update Todo that doesnt exist"
    )


@app.delete("/delete_todo", status_code=204)
async def delete_todo(title: str):
    result = await todo_delete(title)
    if result:
        return
    raise HTTPException(
        status.HTTP_406_NOT_ACCEPTABLE, "Cant delete Todo that doesnt exist"
    )
