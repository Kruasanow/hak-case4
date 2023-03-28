from init_db import db


def get_datename():
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM datename;")
    get_list = cur.fetchall()
    print(get_list)
    return get_list

# get_datename()