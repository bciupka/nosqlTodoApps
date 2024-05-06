from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import Annotated
from datetime import datetime


class Todo(Document):
    id: PydanticObjectId
    title: Annotated[str, Field(max_length=50)]
    description: Annotated[str, Field(max_length=100)]
    due_date: datetime


class TodoUpdate(BaseModel):
    description: Annotated[str, Field(max_length=100)]
    due_date: datetime


class TodoIn(TodoUpdate):
    title: Annotated[str, Field(max_length=50)]
