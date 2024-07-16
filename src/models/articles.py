from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from myapp import BaseModel


class Articles(BaseModel):
    __tablename__ = 'articles'
    url = Column(String(length=255), unique=True)
    api_url = Column(String(length=255))
    title = Column(String(length=255))
    published_date = Column(String(length=255))

    # Links with sub navbar
    tag = Column(String(length=255), ForeignKey('sub_navbar.url'))
    parent_tag = relationship('SubNavBar', back_populates='children_articles')

    # Links with images
    children_images = relationship('Images', back_populates='images_parent_article')

    # Links with authors
    author = Column(String(length=255), ForeignKey('authors.name'))
    parent_author = relationship('Authors', back_populates='author_children_articles')

    # TODO: add related articles
