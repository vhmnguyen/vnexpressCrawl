from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from myapp import db_session
from src.models import WeatherNavBar


def get_weather_navbar():

    driver = webdriver.Chrome()
    driver.get('https://vnexpress.net')

    weather = driver.find_element(By.XPATH, "/html/body/header/div/a")
    hover = ActionChains(driver).move_to_element(weather)
    hover.perform()

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    location_list = soup.find('ul', class_='list-address')
    locations = location_list.find_all('li')

    with db_session() as session:
        for location in locations:

            class_names = location.a.get('data-name', [])
            name = ' '.join(class_names) if isinstance(class_names, list) else class_names

            if location.find('a'):
                url = location.find('a')['href']
            else:
                continue

            element_to_db = WeatherNavBar(
                url=url,
                location=name
            )
            session.add(element_to_db)
        session.commit()

    driver.quit()


if __name__ == '__main__':
    get_weather_navbar()
