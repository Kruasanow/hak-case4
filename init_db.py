import psycopg2
import pandas as pd

def db():
    conn = psycopg2.connect(
        host="localhost",
        user="hackaton",
        password="vkathebest",
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
    cur.execute('DROP TABLE IF EXISTS markedbase;')
    cur.execute("""
                CREATE TABLE markedbase (
                    username varchar(50),
                    file varchar(255),
                    hash varchar(255),
                    fprint varchar(255),
                    line1 varchar(250),
                    line2 varchar(250),
                    line3 varchar(250),
                    date varchar(250),
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
    # conn.commit()
    # cur.close()
    # conn.close()

    # conn = db()
    # cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users;')
    cur.execute("""
                CREATE TABLE users (
                    usr varchar(50),
                    password varchar(50)
                );
                """)
    
    # cur.execute('DROP TABLE IF EXISTS filedata;')
    # cur.execute("""
    #             CREATE TABLE filedata (
    #                 basename varchar(50),
    #                  varchar(50)
    #             );
    #             """)
    conn.commit()
    cur.close()
    conn.close()

