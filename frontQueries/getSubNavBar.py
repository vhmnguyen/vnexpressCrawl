from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from myapp import db_session
from src.models import SubNavBar


def check_if_exists(url_to_check):
    with db_session() as session:
        if session.query(SubNavBar.url).filter(SubNavBar.url == url_to_check).first() is None:
            return 0
        return 1

def get_from_dropdown():

    driver = webdriver.Chrome()
    driver.get("https://vnexpress.net")

    wait = WebDriverWait(driver, 3)
    dropdown = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/header/div/a")))
    dropdown.click()

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    menu_section = soup.find('section', class_='wrap-all-menu')
    container_div = menu_section.find('div', class_='container')
    row_menu_div = container_div.find('div', class_='row-menu')
    sub_navbar_elements = row_menu_div.find_all('li')

    with db_session() as session:
        for element in sub_navbar_elements:
            # Get the URL
            if element.find('a')['href'].startswith('http') and element.find('a'):
                url = element.find('a')['href']
            else:
                continue

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

    # Close the WebDriver
    driver.quit()


if __name__ == '__main__':
    get_from_dropdown()
