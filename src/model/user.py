import sqlite3
import logging

def create_user(user_name, password):
    con = sqlite3.connect("db/munex.db")
    cursor = con.cursor()
    query = f"insert into user values (NULL, '{user_name}','{password}')"
    logging.info(query)
    cursor.execute(query)
    con.commit()
    con.close()
    return True