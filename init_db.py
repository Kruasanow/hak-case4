import psycopg2
import pandas as pd

def db():
    conn = psycopg2.connect(
        host="localhost",
        user="ubuntu18",
        password="rusanow",
        database="hack_db"
    )
    return conn


def init_db():
    conn = db()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS test;')
    cur.execute("""
                CREATE TABLE test (
                    full_name varchar(50),
                    mail varchar(50),
                    phone varchar(50),
                    time varchar(50),
                    city varchar(50),
                    address varchar(50),
                    er_id varchar(50),
                    state varchar(50),
                    loyalty varchar(50),
                    metrica TIMESTAMP DEFAULT NOW() NOT NULL
                );
                """)
    cur.execute('DROP TABLE IF EXISTS datename;')
    cur.execute("""
                CREATE TABLE datename (
                    date varchar(50),
                    name varchar(50),
                    addpole varchar(50)
                );
                """)
    conn.commit()
    cur.close()
    conn.close()


    conn = db()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users;')
    cur.execute("""
                CREATE TABLE users (
                    usr varchar(50),
                    password varchar(50)
                );
                """)
    conn.commit()
    cur.close()
    conn.close()



# name_file = 'data33.csv'
# name_sheet = 'data'
# name_table = 'test'
# df = pd.read_csv(name_file)
# print(list(df.columns))
# k1 = list(df['full_name'])
# k2 = list(df['mail'])
# k3 = list(df['phone'])
# k4 = list(df['time'])
# k5 = list(df['city'])
# k6 = list(df['address'])
# k7 = list(df['er_id'])
# k8 = list(df['state'])
# k9 = list(df['loyalty'])
# data_lists =[]
# for i in range(len(k1)):
#     data_lists.append([str(k1[i]),str(k2[i]),str(k3[i]),str(k4[i]),str(k5[i]),str(k6[i]),str(k7[i]),str(k8[i]),str(k9[i])])
# conn = db()
# cur = conn.cursor()
# print(df['full_name'][0])
# # Загружаем данные из DataFrame
# for data in data_lists:
#     cur.execute("INSERT INTO test VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
# conn.commit()
# cur.close()
# conn.close()


# go_db()
# add_base()
