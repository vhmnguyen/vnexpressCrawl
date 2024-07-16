# TODO: create new function
#       --> gets url
#       --> count number of '/'
#           --> turn url into list of characters
#           --> while count < 2: add character to a list
#           --> turn that list into string
#       --> return parent's directory url

from myapp import db_session
from src.models import SubNavBar, MainNavBar


def get_parent_directory(url):
    url_list_form = list(url)
    url_list_to_return = []
    count = 0
    for character in url_list_form:
        if character == '/':
            count += 1
        if count >= 2:
            return ''.join(url_list_to_return)
        else:
            url_list_to_return.append(character)
    return ''.join(url_list_to_return)

def get_parent_from_existing_data():
    with db_session() as session:
        sub_categories = session.query(SubNavBar).all()
        for category in sub_categories:
            category_parent = get_parent_directory(category.url)

            # Check if url exists in main navbar, if not, add
            if session.query(MainNavBar.url).filter(MainNavBar.url == category_parent).first() is None:
                element_to_db = MainNavBar(url=category_parent)
                session.add(element_to_db)
                session.commit()

            category.parent_category = category_parent
            session.commit()
    pass


if __name__ == '__main__':
    get_parent_from_existing_data()
