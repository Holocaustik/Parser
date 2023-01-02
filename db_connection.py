import datetime
import sqlite3 as sq


class DB_my_connection():
    def __init__(self, table_name=None):
        self.table_name = table_name

    def create_db(self):
        with sq.connect('db/VIdb.db') as con:
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE mainDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE,
                    product_name TEXT,
                    product_price INTEGER
                )""")

    def insert_in_db_params(self, dict: list = []):
        with sq.connect('db/VIdb.db') as con:
            cursor = con.cursor()
            text_for_insert_value_in_table = f'INSERT INTO mainDB VALUES (NULL, "{datetime.date.today().strftime("d.%m.%Y")}", ?, ?)'
            cursor.executemany(text_for_insert_value_in_table, dict)
            con.commit()