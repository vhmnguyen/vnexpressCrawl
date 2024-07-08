from sqlalchemy import (Column, String)

from myapp import BaseModel


class WeatherNavBar(BaseModel):
    __tablename__ = 'weather_navbar'
    url = Column(String(length=255))
    location = Column(String(length=255))
