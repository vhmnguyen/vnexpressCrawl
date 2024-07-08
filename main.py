from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from myapp import db_session
from src.models import Articles as ArticlesModel
from src.models import Authors as AuthorsModel

app = FastAPI()


# Define pydantic article model
class ArticleSchema(BaseModel):
    url: str | None = None
    title: str | None = None

    class Config:
        from_attributes = True


# Define pydantic author model
class AuthorSchema(BaseModel):
    name: str | None = None

    class Config:
        from_attributes = True


# Get article by title
@app.get("/article/{article_title}")
async def get_article(article_title: str):
    with db_session() as session:
        article_found = session.query(ArticlesModel).filter(ArticlesModel.title.startswith(article_title)).all()
        if article_found is None:
            raise HTTPException(status_code=404, detail="Article not found")
    return article_found

# Delete article by id
@app.delete("/article/{article_id}")
async def delete_article(article_id: str):
    with db_session() as session:
        article_found = session.query(ArticlesModel).filter(ArticlesModel.id == article_id).first()
        if article_found is None:
            raise HTTPException(status_code=404, detail="Article not found")
        session.delete(article_found)
        session.commit()
    return {"message": "Article deleted"}

# Update article based on ID
@app.put("/article/{article_id}", response_model=ArticleSchema)
async def update_article(article_id: str, article_update: ArticleSchema):
    with db_session() as session:
        article_found = session.query(ArticlesModel).filter(ArticlesModel.id == article_id).first()
        if article_found is None:
            raise HTTPException(status_code=404, detail="Author not found")
        article_found.title = article_update.title
        session.commit()
        session.refresh(article_found)
    return article_found



# Get author by name
@app.get("/author/{author_name}")
async def get_author(author_name: str):
    with db_session() as session:
        author_found = session.query(AuthorsModel).filter(AuthorsModel.name.startswith(author_name)).all()
        if author_found is None:
            raise HTTPException(status_code=404, detail="Article not found")
    return author_found


# Update author by id


@app.get("/")
async def root():
    return {"message": "Hello World"}
