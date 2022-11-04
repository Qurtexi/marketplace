from datetime import datetime

from pydantic import BaseModel
from typing import Text, Optional


class PostModel(BaseModel):
    title: str
    content: Text


class PostDetailsModel(BaseModel):
    id: int
    created_at: datetime
    content: Text
    title: str
    user_name: str
