from model import Todo, TodoUpdate
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


async def init():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(
        client.TodoBeanie,
        document_models=[
            Todo,
        ],
    )


async def todo_list():
    return await Todo.all().to_list()


async def todo_create(data: Todo):
    await data.insert()
    return data


async def todo_get(title: str):
    todo = await Todo.find_one(Todo.title == title)
    return todo


async def todo_update(title: str, updated: TodoUpdate):
    todo = await Todo.find_one(Todo.title == title)
    if todo:
        todo.description = updated.description
        todo.due_date = updated.due_date
        await todo.save()

    return todo


async def todo_delete(title: str):
    todo = await Todo.find_one(Todo.title == title)
    if todo:
        deleted = await todo.delete()
        return deleted
    return
