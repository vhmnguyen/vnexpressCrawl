from myapp import BaseModel

class Articles(BaseModel):
    url: str | None = None
    api_url: str | None = None
    title: str | None = None
    published_date: str | None = None

    tag: str | None = None
