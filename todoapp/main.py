from fastapi import FastAPI, HTTPException, status
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    delete_todo,
    modify_todo,
)
from models import TodoBase, Todo

app = FastAPI()


@app.get("/all_todos")
async def get_all_todos() -> list[Todo]:
    result = await fetch_all_todos()
    return result


@app.get("/todo/{title}")
async def get_todo(title: str) -> Todo:
    result = await fetch_one_todo(title)
    if result:
        return result
    raise HTTPException(404, f"No data with this title: {title}")


@app.post("/add_todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> Todo:
    todo_dict = todo.model_dump()
    response = await create_todo(todo_dict)
    if response:
        return response
    raise HTTPException(400)


@app.put("/change_todo/{title}", status_code=status.HTTP_201_CREATED)
async def change_todo(title: str, data: TodoBase) -> Todo:
    response = await modify_todo(title, data.model_dump())
    if response:
        return response
    raise HTTPException(400)


@app.delete("/del_todo/{title}", status_code=status.HTTP_204_NO_CONTENT)
async def del_todo(title: str):
    await delete_todo(title)
    return
