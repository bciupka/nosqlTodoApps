from motor import motor_asyncio
from models import Todo

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoApp
collection = database.todo


async def fetch_one_todo(title: str):
    result = await collection.find_one({"title": title})
    return result


async def fetch_all_todos():
    results = collection.find({})
    list_of_todos = []
    async for result in results:
        list_of_todos.append(Todo(**result))
    return list_of_todos


async def create_todo(todo: dict):
    await collection.insert_one(todo)
    response = await collection.find_one({"title": todo["title"]})
    return response


async def modify_todo(title: str, data: dict):
    await collection.update_one(
        {"title": title},
        {"$set": {"description": data["description"], "due_date": data["due_date"]}},
    )
    result = await collection.find_one({"title": title})
    return result


async def delete_todo(title: str):
    await collection.delete_one({"title": title})
    return True
