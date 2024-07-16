from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship, Relationship

from myapp import BaseModel


class Images(BaseModel):
    __tablename__ = 'images'
    image_src = Column(LONGTEXT)
    alt = Column(LONGTEXT)

    # Links with articles
    article_src = Column(String(length=255), ForeignKey('articles.url'))
    images_parent_article = relationship('Articles', back_populates='children_images')
