from Parser import Parser
from db_connection import DB_my_connection
from selenium.common.exceptions import WebDriverException


def parser_VI():
    all_links = Parser().get_all_links()
    errors_list = []
    OK_list = []
    for link in all_links:
        parser = Parser()
        last_page = parser.get_last_page(link=link)
        try:
            data = parser.parser_page(last_page=last_page, link=link)
            DB_my_connection().insert_in_db_params(data)
            OK_list.append(link)
        except WebDriverException:
            pass
    print(f'спарсили всего категорий {OK_list}')
    print(f'Не получилось спарсить {errors_list}')


if __name__ == "__main__":
    parser_VI()
