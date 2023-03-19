from init_db import db



def ins_data(date, name, addpole=None):
    conn = db()

    cur = conn.cursor()

    cur.execute(
                'INSERT INTO datename ('
                'date, name,'
                'addpole'
                ')'
        'VALUES ('
                '%s, %s, %s'
                ')',
                (
                date, name, addpole,
                )
                )
    conn.commit()

    cur.close()
    conn.close()
