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


# def upassw(usr,password):
#         conn = db()
#         cur = conn.cursor()

#         cur.execute('INSERT INTO users'
#                 '('
#                 'usr,password'
#                 ')'
#         'VALUES ('
#                 '%s, %s'
#                 ')'
#                 (
#                 usr, password
#                 )
#                 )
#         conn.commit()

#         cur.close()
#         conn.close()

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
            continue
        else:
            print('good')
            t = True
    return t