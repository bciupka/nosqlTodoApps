from beanie import Document
from pydantic import BaseModel, Field
from typing import Annotated
from datetime import datetime


class TodoBase(BaseModel):
    description: Annotated[str, Field(max_length=100)]
    due_date: datetime


class Todo(Document, TodoBase):
    title: Annotated[str, Field(max_length=50)]


class TodoUpdate(TodoBase):
    pass
