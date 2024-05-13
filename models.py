from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class BlogPost:
    title: str
    content: str
    author: str
    id: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
    comments: list = None
    likes: list = None
    dislikes: list = None

@dataclass
class Comment:
    post_id: str
    author: str
    content: str
    id: Optional[str] = None
    created_at: datetime = datetime.now()

@dataclass
class Like:
    post_id: str
    user_id: str
    id: Optional[str] = None

@dataclass
class Dislike:
    post_id: str
    user_id: str
    id: Optional[str] = None