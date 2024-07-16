from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from myapp import BaseModel


class SubNavBar(BaseModel):
    __tablename__ = 'sub_navbar'
    url = Column(String(length=255), unique=True, nullable=False)
    name = Column(String(length=255))

    # Links with articles
    children_articles = relationship('Articles', back_populates='parent_tag')

    # Links with main navbar
    parent_category = Column(String(length=255), ForeignKey('main_navbar.url'))
    parent_category_relationship = relationship('MainNavBar', back_populates='children_categories')

    # TODO: link with mainNavBar
    # Can do: count '/'. if count >= 2: remove from that point on
    # Take that as mainNavBar
