from model import Todo
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
