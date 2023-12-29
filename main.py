import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

user = 'root'
password = 'college'
host = 'localhost'
port = 3306
database = 'employees'


def get_sqlalchemy_connection():
    url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(url=url)
    connection = engine.connect()
    return connection


def get_mysql_connection():
    connection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database,
    )
    return connection


def main(connector):
    try:
        if connector == 'sqlalchemy':
            connection = get_sqlalchemy_connection()
        elif connector == 'mysql':
            connection = get_mysql_connection()
        print(f'Connection to the {host} for user {user} created successfully.')
    except Exception as ex:
        print('Connection could not be made due to the following error: \n', ex)

    filename = './src/query.sql'
    with open(filename, 'r') as query:
        df = pd.read_sql_query(query.read(), connection)

    print(df.head())


if __name__ == '__main__':
    connector = 'sqlalchemy'
    main(connector=connector)
