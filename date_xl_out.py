import psycopg2
import pandas as pd
from init_db import db

def do_xl_by_date(start,stop,res_name):
    # Подключение к базе данных
    conn = db()

    # Ввод переменных дат
    start_date = start
    end_date = stop

    # Выполнение запроса к базе данных с параметрами и сохранение результата в объект DataFrame
    # query = "SELECT * FROM test WHERE created_at >= %s AND created_at < %s;"
    query = "SELECT * FROM markedbase WHERE metrica BETWEEN %s AND %s;"
    
    try:
        df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    except Exception:
        print('trouble')
    # Закрытие соединения с базой данных
    conn.close()

    # Сохранение результата в Excel-файл
    df.to_excel(res_name, index=False)