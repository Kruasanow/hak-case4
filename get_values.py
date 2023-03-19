from init_db import db

def select_values():
    conn = db()
    cur = conn.cursor()

    cur.execute('SELECT * from datename;')
    out = list(cur.fetchall())
    print(out)
    print(dir(out))
    out_name = out[-1][1]
    out_date = out[-1][0]
    return [out_name, out_date]