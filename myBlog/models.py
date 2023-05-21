from typing import Optional
from sqlmodel import Field
import pynecone as pc
from datetime import datetime

class Blogs(pc.Model,table=True):
    author:str
    title:str
    path:str
    content:str
    pagenumber:int
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())