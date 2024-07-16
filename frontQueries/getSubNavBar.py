import requests
from bs4 import BeautifulSoup

from myapp import db_session
from src.models import SubNavBar, MainNavBar


def check_if_exists(url_to_check):
    with db_session() as session:
        if session.query(SubNavBar.url).filter(SubNavBar.url == url_to_check).first() is None:
            return 0
        return 1

def get_from_main_navbar():
    url_list = []
    with db_session() as session:
        rows = session.query(MainNavBar)
        for row in rows:
            if row.url != '/':
                subpage_url = f'https://vnexpress.net{row.url}'
            else:
                continue
            url_list.append(subpage_url)
    return url_list

def get_sub_navbar():
    subpage_urls = get_from_main_navbar()
    for subpage_url in subpage_urls:
        page = requests.get(subpage_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        if subpage_url == 'https://vnexpress.net/the-thao/euro-2024':
            sub_categories = soup.find('ul', class_='main-menu-euro')
        else:
            sub_categories = soup.find('ul', class_='ul-nav-folder')
        if sub_categories is None:
            continue
        sub_navbar_list = sub_categories.find_all('li')

        with db_session() as session:
            for element in sub_navbar_list:
                if element.find('a')['href'].startswith('https://vnexpress.net') and element.find('a'):
                    url = element.find('a')['href'].replace('https://vnexpress.net', '')
                else:
                    if element.find('a')['href'].startswith('https'):
                        continue
                    url = element.find('a')['href']

                # Get name, join class names into a single string
                class_names = element.a.get('title', [])
                name = ' '.join(class_names) if isinstance(class_names, list) else class_names

                if check_if_exists(url) == 1:
                    continue
                else:
                    # Create SubNavBar object
                    element_to_db = SubNavBar(
                        url=url,
                        name=name
                    )
                    session.add(element_to_db)
                session.commit()


if __name__ == '__main__':
    get_sub_navbar()
