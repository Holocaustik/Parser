from Parser import Parser
from db_connection import DB_my_connection

brand_list = ['vihr-1007', 'zubr-665', 'interskol-19', 'fubag-103', 'champion-602', 'dde-13498', 'huter-1008/', 'patriot-426', 'makita-1']


def parser_VI(brand_list: list = []):
    for brand in brand_list:
        parser = Parser(brand)
        last_page = parser.get_last_page()
        for page in range(1, last_page):
            result_one_page = parser.parser_page(page)
            DB_my_connection().insert_in_db_params(result_one_page)


if __name__ == "__main__":
    parser_VI(brand_list)
