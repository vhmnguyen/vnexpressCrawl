import requests
from bs4 import BeautifulSoup

from myapp import db_session
from src.models import MainNavBar, Articles


def get_subpage_url():
    url_list = []
    with db_session() as session:
        rows = session.query(MainNavBar)
        for row in rows:
            if row.url.startswith('/'):
                subpage_url = f'https://vnexpress.net{row.url}'
            else:
                continue
            url_list.append(subpage_url)
    return url_list

def check_if_exists(title_to_check):
    with db_session() as session:
        if session.query(Articles.title).filter(Articles.title == title_to_check).first() is None:
            return 0
        return 1

def get_published_date(url):
    if url == '#' or url is None:
        return ''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    published_date = soup.find('span', class_='date')
    return published_date.text if published_date is not None else ''

def get_sub_articles():
    subpage_urls = get_subpage_url()
    for subpage_url in subpage_urls:
        page = requests.get(subpage_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        newslist = soup.find_all('article')

        with db_session() as session:
            for news in newslist:
                if news.a is None:
                    continue
                else:
                    url = news.a.get('href')
                    published_date = get_published_date(url)
                    class_titles = news.a.get('title', [])
                    title = ' '.join(class_titles) if isinstance(class_titles, list) else class_titles

                if check_if_exists(title) == 1:
                    continue
                else:
                    element_to_db = Articles(
                        url=url,
                        title=title,
                        published_date=published_date
                    )
                    session.add(element_to_db)
            session.commit()


if __name__ == '__main__':
    get_sub_articles()
