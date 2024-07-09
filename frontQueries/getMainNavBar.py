from bs4 import BeautifulSoup
import requests

from myapp import db_session
from src.models import MainNavBar

URL = "https://vnexpress.net"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

parent_list = soup.find('ul', class_='parent')
main_nav_bar_elements = parent_list.find_all('li')


def check_if_exists(url_to_check):
    with db_session() as session:
        if session.query(MainNavBar.url).filter(MainNavBar.url == url_to_check).first() is None:
            return 0
        return 1

def get_main_navbar():
    with db_session() as session:
        for element in main_nav_bar_elements:
            # Get the URL
            if element.find('a')['href'].startswith('/') and element.find('a'):
                url = element.find('a')['href']
            else:
                continue

            # Get name, join class names into a single string
            class_names = element.a.get('title', [])
            name = ' '.join(class_names) if isinstance(class_names, list) else class_names

            if check_if_exists(url) == 1:
                continue
            else:
                # Create MainNavBar object
                element_to_db = MainNavBar(
                    url=url,
                    name=name
                )
                session.add(element_to_db)
        session.commit()


if __name__ == '__main__':
    get_main_navbar()
