import datetime
import sqlite3 as sq
import pandas as pd


class DB_my_connection():
    def __init__(self, table_name=None):
        self.table_name = table_name

    def create_db(self):
        with sq.connect('db/VIdb.db') as con:
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE mainDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE,
                    code text,
                    product_name TEXT,
                    product_price INTEGER
                )""")

    def insert_in_db_params(self, dict: list = []):
        with sq.connect('db/VIdb.db') as con:
            cursor = con.cursor()
            text_for_insert_value_in_table = f'INSERT INTO mainDB VALUES (NULL, "{datetime.date.today().strftime("%d.%m.%Y")}", ?, ?, ?)'
            cursor.executemany(text_for_insert_value_in_table, dict)
            con.commit()


    def get_in_db_params(self, dict: list = []):
        with sq.connect('db/VIdb.db') as con:
            cursor = con.cursor()
            sqlite_select_query = """SELECT * from mainDB"""
            cursor.execute(sqlite_select_query)
            num = cursor.fetchall()
            con.commit()
        return num

    def save_to_excel(self, data: list | dict | tuple = None, name='ozon'):
        num = pd.DataFrame(data)
        num.to_excel(f'{name}.xlsx', header=1)

if __name__ == "__main__":
    DB_my_connection().create_db()
    # num = DB_my_connection().get_in_db_params()
    # DB_my_connection().save_to_excel(num)