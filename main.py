from Parser import Parser
from db_connection import DB_my_connection
from selenium.common.exceptions import WebDriverException


def parser_VI():
    all_links = Parser().get_all_links()
    for link in all_links:
        parser = Parser()
        last_page = parser.get_last_page(link=link)
        for page in range(1, last_page):
            try:
                data = parser.parser_page(page=page, link=link)
                DB_my_connection().insert_in_db_params(data)
            except WebDriverException:
                pass


if __name__ == "__main__":
    parser_VI()
