import logging
import sqlite3

def create_user(user_name, password):
    con = sqlite3.connect("db/munex.db")
    cursor = con.cursor()
    query = f"insert into user values (NULL, '{user_name}','{password}')"
    logging.info(query)
    cursor.execute(query)
    con.commit()
    con.close()
    return True

def exists(user_name):
    con = sqlite3.connect("db/munex.db")
    cursor = con.cursor()
    query = f"select id, password from user where name = '{user_name}'"
    logging.info(query)
    results = cursor.execute(query).fetchall()
    if len(results) == 0:
        return False, None
    return True, results[0][0], results[0][1]
    
def set_token(id, token, expires_at):
    con = sqlite3.connect("db/munex.db")
    cursor = con.cursor()
    query = (f"""update user set token = '{token}', 
                token_expires_at = '{expires_at}'
                where id = {id}
    """)
    logging.info(query)
    cursor.execute(query)
    con.commit()
    con.close()
    return True