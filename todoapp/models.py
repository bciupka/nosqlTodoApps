from pydantic import BaseModel, Field
from typing import Annotated
from datetime import datetime


class TodoBase(BaseModel):
    description: Annotated[str, Field(max_length=300)]
    due_date: datetime


class Todo(TodoBase):
    title: Annotated[str, Field(max_length=50)]
