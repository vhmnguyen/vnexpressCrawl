from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship

from myapp import BaseModel


class MainNavBar(BaseModel):
    __tablename__ = 'main_navbar'
    url = Column(String(length=255), unique=True)
    name = Column(String(length=255))

    # Links with subNavBar
    children_categories = relationship('SubNavBar', back_populates='parent_category_relationship')
