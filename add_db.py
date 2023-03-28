from init_db import db
import datetime


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

def ins_file_data(user, file, date=None, hash=None, fprint=None, line1=None, line2=None, line3=None):
    conn = db()
    cur = conn.cursor()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # current_time = datetime.datetime.fromtimestamp(cf)
    cur.execute(
        'INSERT INTO markedbase (username, file, hash, fprint, line1, line2, line3, date, metrica) '
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (user, file, hash, fprint, line1, line2, line3, date, current_time)
    )
    conn.commit()
    cur.close()
    conn.close()
                # hash,'
                # 'fprint, line1,'
                # 'line2, line3,'

def check_passw(usr,passwd):
    u = usr
    p = passwd
    conn = db()
    cur = conn.cursor()

    cur.execute('SELECT date, name FROM datename;')
    a = cur.fetchall()
    print(a)
    t = False
    for i in a:
        if i[0] != u or i[1] != p:
            print('wrong')
            status = 'wrong identifier...'
            continue
        else:
            print('good')
            status = 'true'
            t = True
    return [t, status]