import sqlite3

def load_data(data, db_conn):
    if data is not None:
        data.to_sql('people', db_conn, if_exists='replace', index=False)
        print("Data loaded into database")
