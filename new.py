import pandas as pd
import psycopg2
from init_db import db

#  создание таблицы последний скрытый столбец которой будет заполняться автоматически текущей датой и временем
#  '''
# CREATE TABLE test (
#     full_name varchar(50),
#     mail varchar(50),
#     phone varchar(50),
#     time varchar(50),
#     city varchar(50),
#     address varchar(50),
#     er_id varchar(50),
#     state varchar(50),
#     loyalty varchar(50),
#     created_at timestamp GENERATED ALWAYS AS (now()) STORED
# );
# '''


name_file = 'data1.xlsx'
name_sheet = 'data'
name_table = 'test'

df = pd.read_excel(name_file, sheet_name=name_sheet)

print(list(df.columns))

conn = db()

cursor = conn.cursor()


# Загружаем данные из DataFrame
for index, row in df.iterrows():
    insert_query = f"""
    INSERT INTO {name_table} (full_name, mail, phone, time, city, address, er_id, state, loyalty)
    VALUES ({row['full_name']}, {row['mail']}, {row['phone']}, {row['time']},{row['city']}, {row['address']}, {row['er_id']}, {row['state']}, {row['loyalty']};
    """
    cursor.execute(insert_query)

conn.commit()
conn.close()
