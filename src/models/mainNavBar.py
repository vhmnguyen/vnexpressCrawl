from sqlalchemy import (Column, String)

from myapp import BaseModel


class MainNavBar(BaseModel):
    __tablename__ = 'main_navbar'
    url = Column(String(length=255))
    name = Column(String(length=255))
