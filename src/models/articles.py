from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from myapp import BaseModel


class Articles(BaseModel):
    __tablename__ = 'articles'
    url = Column(String(length=255))
    title = Column(String(length=255))
    published_date = Column(String(length=255))
