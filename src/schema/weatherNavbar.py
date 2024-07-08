from myapp import BaseModel

class WeatherNavBar(BaseModel):
    url: str | None = None
    location: str | None = None
