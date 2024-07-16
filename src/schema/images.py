from myapp import BaseModel

class Images(BaseModel):
    image_src: str | None = None
    alt: str | None = None
