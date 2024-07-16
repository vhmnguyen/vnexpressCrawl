from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship

from myapp import BaseModel


class Authors(BaseModel):
    __tablename__ = 'authors'
    name = Column(String(length=255), unique=True)

    # Links with articles
    author_children_articles = relationship('Articles', back_populates='parent_author')
