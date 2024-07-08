from sqlalchemy import (Column, String)

from myapp import BaseModel


class SubNavBar(BaseModel):
    __tablename__ = 'sub_navbar'
    url = Column(String(length=255))
    name = Column(String(length=255))
