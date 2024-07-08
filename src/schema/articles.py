from myapp import BaseModel

class Articles(BaseModel):
    url: str | None = None
    title: str | None = None
    published_date: str | None = None
