import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from myapp import db_session
from src.models import Articles as ArticlesModel
from src.models import Images as ImagesModel
from src.models import MainNavBar as MainNavBarModel
from src.models import SubNavBar as SubNavBarModel

app = FastAPI()


# Define pydantic article model
class ArticleSchema(BaseModel):
    url: str | None = None
    title: str | None = None

    class Config:
        from_attributes = True


# Define pydantic main navbar model
class MainNavBarSchema(BaseModel):
    url: str | None = None
    name: str | None = None

    class Config:
        from_attributes = True


# Define pydantic sub navbar model
class SubNavBarSchema(BaseModel):
    url: str | None = None
    name: str | None = None

    class Config:
        from_attributes = True


# Define pydantic author model
class AuthorSchema(BaseModel):
    name: str | None = None

    class Config:
        from_attributes = True


# Define pydantic image model
class ImageSchema(BaseModel):
    image_src: str | None = None
    alt: str | None = None

    class Config:
        from_attributes = True


# Get main categories, default
@app.get("/")
async def get_main_categories():
    with db_session() as session:
        main_categories = session.query(MainNavBarModel).all()
    return main_categories


# Open categories, display articles within that category
@app.get("/{category}")
async def get_articles_by_main_category(category: str):
    with db_session() as session:
        articles = session.query(ArticlesModel).filter(ArticlesModel.tag == '/' + category).all()
        sub_categories = session.query(SubNavBarModel).filter(SubNavBarModel.parent_category == '/' + category).all()
    return {'sub categories': sub_categories,
            'articles': articles}


# TODO
#   Error: 404 Not Found
#   Srsly no clue how to do this mate
# Open sub categories, display articles within that subcategory
@app.get("/{sub_category}")
async def get_articles_by_sub_category(sub_category: str):
    with db_session() as session:
        pass
    return {'articles': 'TODO'}


# Get article based on article's api url
@app.get("/article/{article_api_url}")
async def get_article(article_api_url: str):
    with db_session() as session:
        article = session.query(ArticlesModel).filter(ArticlesModel.api_url == article_api_url).first()
        images = session.query(ImagesModel).filter(ImagesModel.article_src == article.url).all()
    return {'article': article,
            'images': images}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
