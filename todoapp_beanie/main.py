from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init, todo_create, todo_list
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
