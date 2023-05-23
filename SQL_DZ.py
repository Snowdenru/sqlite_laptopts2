import sqlite3

conn = sqlite3.connect('laptops.db')

cursor = conn.cursor()
cursor.execute("""
                CREATE TABLE if not exists Company(
                    id integer PRIMARY KEY,
                    Company_name text
                    ) """)
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists Model(
                   id integer PRIMARY KEY,
                   Model_name text,
                   Company_id integer,
                   OS_id integer,
                   RAM_id integer,
                   FOREIGN KEY(OS_id) REFERENCES OS(id),
                   FOREIGN KEY(RAM_id) REFERENCES RAM(id),
                   FOREIGN KEY(Company_id) REFERENCES Company(id))""")
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists OS(
                   id integer PRIMARY KEY,
                   OS_name text)""")
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists Series(
                   id integer PRIMARY KEY,
                   Series_name text,
                   Model_id integer,
                   FOREIGN KEY(Model_id) REFERENCES Model(id))""")
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists RAM(
                   id integer PRIMARY KEY,
                   RAM_name text)""")
conn.commit()

conn.close() # не забываем закрывать соединение


