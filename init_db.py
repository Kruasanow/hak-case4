import psycopg2

#  создание таблицы последний скрытый столбец которой будет заполняться автоматически текущей датой и временем


def db():
    conn = psycopg2.connect(
        host="localhost",
        user="hackaton",
        password="vkathebest",
        database="hack_db"
    )
    return conn



conn = db()

cur = conn.cursor()

# cur.execute("""
#             CREATE TABLE test (
#                 full_name varchar(50),
#                 mail varchar(50),
#                 phone varchar(50),
#                 time varchar(50),
#                 city varchar(50),
#                 address varchar(50),
#                 er_id varchar(50),
#                 state varchar(50),
#                 loyalty varchar(50),
#                 metrica TIMESTAMP DEFAULT NOW() NOT NULL
#             );
#             """)

# cur.execute("""
#         ALTER TABLE test
#         DROP COLUMN metrica;
#         """)

conn.commit()



cur.close()
conn.close()
