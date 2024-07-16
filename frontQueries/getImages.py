import requests
from bs4 import BeautifulSoup

from myapp import db_session
from src.models import Articles, Images


# Get urls from articles db
def get_articles_urls():
    url_list = []
    with db_session() as session:
        rows = session.query(Articles)
        for row in rows:
            if row.url.startswith('https://video'):
                continue
            url_list.append(row.url)
    return url_list

# Check if image_src already exists in table
def check_exists(image_src_to_check):
    with db_session() as session:
        if session.query(Images.image_src).filter(Images.image_src == image_src_to_check).first() is None:
            return 0
        return 1

# Main func
def get_images():
    articles_urls = get_articles_urls()
    with db_session() as session:
        for article in articles_urls:
            page = requests.get(article)
            soup = BeautifulSoup(page.content, 'html.parser')

            article_images = soup.find_all('img')

            for article_image in article_images:
                image_src = article_image.get('src')
                if not image_src:
                    continue
                alt = article_image.get('alt')

                if check_exists(image_src) == 1:
                    continue

                image_to_db = Images(
                    image_src=image_src,
                    alt=alt,
                    article_src=article
                )
                session.add(image_to_db)
                session.commit()


if __name__ == '__main__':
    get_images()
