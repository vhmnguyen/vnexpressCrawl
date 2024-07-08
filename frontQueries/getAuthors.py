import requests
from bs4 import BeautifulSoup

from myapp import db_session
from src.models import Articles, Authors


def get_article_url():
    url_list = []
    with db_session() as session:
        rows = session.query(Articles)
        for row in rows:
            if row.url is not None and row.url != '#':
                url_list.append(row.url)
            else:
                continue
    return url_list


def check_if_exists(name_to_check):
    with db_session() as session:
        if session.query(Authors.name).filter(Authors.name == name_to_check).first() is None:
            return 0
        return 1


def get_authors():
    article_urls = get_article_url()
    for article_url in article_urls:
        page = requests.get(article_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        author_list = soup.find_all('p', 'author_mail')

        with db_session() as session:
            for author in author_list:
                if author.strong is None:
                    continue
                else:
                    author_name = author.strong.string

                if check_if_exists(author_name) == 1:
                    continue
                else:
                    author_to_db = Authors(name=author_name)
                session.add(author_to_db)
            session.commit()


if __name__ == '__main__':
    get_authors()
