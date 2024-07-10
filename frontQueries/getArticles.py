# TODO: currently not getting articles from main categories. Fix it

import re

import requests
from bs4 import BeautifulSoup
from text_unidecode import unidecode

from myapp import db_session
from src.models import SubNavBar, Articles, MainNavBar


def get_subpage_url():
    url_list = set()
    with db_session() as session:
        # Get main categories' urls
        main_cat_rows = session.query(MainNavBar)
        for row in main_cat_rows:
            if row.url == '#' or row.url is None:
                continue
            subpage_url = f'https://vnexpress.net{row.url}'
            url_list.add(subpage_url)

        # Get sub categories' urls
        sub_cat_rows = session.query(SubNavBar)
        for row in sub_cat_rows:
            if row.url == '#' or row.url is None:
                continue
            subpage_url = f'https://vnexpress.net{row.url}'
            url_list.add(subpage_url)
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

def get_tag(url):
    tag_name = None
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    header_tags = soup.find('ul', class_='breadcrumb')

    # If cant find header tags
    if not header_tags:
        return

    # Find tags, get the last one
    tags_list = header_tags.find_all('a')
    tag = ''
    for a_tag in tags_list:
        tag = a_tag.get('href')
        tag_name = a_tag.get('title')

    # Check if tag exists in subnav db, if not, add it to subnav db
    with db_session() as session:
        if session.query(SubNavBar.url).filter(SubNavBar.url == tag).first() is None:
            element_to_db = SubNavBar(url=tag,
                                      name=tag_name)
            session.add(element_to_db)
            session.commit()
    return tag

def get_sub_articles():
    subpage_urls = get_subpage_url()
    for subpage_url in subpage_urls:
        page = requests.get(subpage_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        newslist = soup.find_all('article')

        with db_session() as session:
            for news in newslist:
                if not news.a:
                    continue

                url = news.a.get('href')

                # If url == '#' or url == None
                if not url or not url.startswith('https'):
                    continue

                published_date = get_published_date(url)
                class_titles = news.a.get('title', [])
                title = ' '.join(class_titles) if isinstance(class_titles, list) else class_titles

                if check_if_exists(title):
                    continue

                api_url = re.sub(r'[^A-Za-z0-9 ]+', '', unidecode(title.lower())).replace(' ', '-')
                tag = get_tag(url)

                element_to_db = Articles(
                    url=url,
                    api_url=api_url,
                    title=title,
                    published_date=published_date,
                    tag=tag
                )
                session.add(element_to_db)
                session.commit()


if __name__ == '__main__':
    get_sub_articles()
