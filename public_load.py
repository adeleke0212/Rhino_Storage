import psycopg2
import os
import json
import pandas as pd
from configparser import ConfigParser
from public_create import Staging_public
from sqlalchemy import create_engine
from public_create import Staging_public
# from sql.loading import database_connector


config = ConfigParser()

config.read('.env')

# create table commands
TRANSACTIONS = config['DB_PUBLIC_TABLES']['PUB_CUSTOMERS']
CUSTOMERS = config['DB_PUBLIC_TABLES']['PUB_TRANSACTIONS']
STORAGES = config['DB_PUBLIC_TABLES']['PUB_STORAGES']
ADDRESS = config['DB_PUBLIC_TABLES']['PUB_ADDRESS']


# database connection
DB_HOST = config['DB_STAGING_CONN']['host']
DB_PASSWORD = config['DB_STAGING_CONN']['password']
DB_PORT = config['DB_STAGING_CONN']['port']
DB_USER = config['DB_STAGING_CONN']['user']
DB_DATABASE = config['DB_STAGING_CONN']['database']


def connect_database():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT,
                            user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
    return conn


connect_database()

# create public tables


def create_transactions():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(Staging_public.transactions.format(TRANSACTIONS))
    connection.commit()
    cursor.close()
    connection.close()
    print('transactions table created')


def create_customers():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(Staging_public.customers.format(CUSTOMERS))
    connection.commit()
    cursor.close()
    connection.close()
    print('customers table created')


def create_address():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(Staging_public.address.format(ADDRESS))
    connection.commit()
    cursor.close()
    connection.close()
    print('address table created')


def create_storages():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(Staging_public.storages.format(STORAGES))
    connection.commit()
    cursor.close()
    connection.close()
    print('storage table created')


def createAllTables():
    create_address()
    create_customers()
    create_transactions()
    create_storages()


createAllTables()


def connectAndLoadAddress():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Adeleke84@localhost:5432/Reno_Storage_DB")
    # conn_string = 'postgresql://username:password@host/database_name'

    # db = create_engine(conn_string)
    conn = engine.connect()
    conn1 = connect_database()
    # Auto-commit transfers all changes that you make immediately to the database.
    # Manual commit requires your confirmation before committing
    conn1.autocommit = True
    cursor = conn1.cursor()
    # drop table if it already exists
    cursor.execute('drop table if exists address')
    # create table postgres
    cursor.execute(Staging_public.address)
    # import the csv file to create a dataframe
    address_df = pd.read_csv('Datasets/address.csv')
    # df to sql
    # df to sql(sql table, alchemy connector)
    address_df.to_sql('address', con=conn, if_exists='replace',
                      schema='public', index=False)

    sql1 = '''select * from address;'''
    cursor.execute(sql1)
    cursor.fetchone()
    conn1.commit()
    conn1.close()
    print('connected and added to address table')


def connectAndLoadCustomers():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Adeleke84@localhost:5432/Reno_Storage_DB")
    # conn_string = 'postgresql://username:password@host/database_name'
    # db = create_engine(conn_string)
    conn = engine.connect()
    conn1 = connect_database()
    conn1.autocommit = True
    cursor = conn1.cursor()
    # drop table if it already exists
    cursor.execute('drop table if exists customers')
    # create table sql postgres
    cursor.execute(Staging_public.customers)
    # import the csv file to create a dataframe
    address_df = pd.read_csv('Datasets/customers.csv')
    # df to sql
    # df to sql(sql table, alchemy connector)
    address_df.to_sql('customers', con=conn, if_exists='replace',
                      schema='public', index=False)

    sql1 = '''select * from customers;'''
    cursor.execute(sql1)
    cursor.fetchone()
    conn1.commit()
    conn1.close()
    print('connected and added to customers table')


# connectAndLoadAddress()


def connectAndLoadStorages():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Adeleke84@localhost:5432/Reno_Storage_DB")
    # conn_string = 'postgresql://username:password@host/database_name'

    # db = create_engine(conn_string)
    conn = engine.connect()
    conn1 = connect_database()
    conn1.autocommit = True
    cursor = conn1.cursor()
    # drop table if it already exists
    cursor.execute('drop table if exists storages')
    # create table syntax into postgres
    cursor.execute(Staging_public.storages)
    # import the csv file to create a dataframe
    address_df = pd.read_csv('Datasets/storages.csv')
    # df to sql
    # df to sql(sql table, alchemy connector)
    address_df.to_sql('storages', con=conn, if_exists='replace',
                      schema='public', index=False)

    sql1 = '''select * from storages;'''
    cursor.execute(sql1)
    cursor.fetchone()
    conn1.commit()
    conn1.close()
    print('connected and added to storages table')


def connectAndLoadTransactions():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Adeleke84@localhost:5432/Reno_Storage_DB")
    # conn_string = 'postgresql://username:password@host/database_name'

    # db = create_engine(conn_string)
    conn = engine.connect()
    conn1 = connect_database()
    conn1.autocommit = True
    cursor = conn1.cursor()
    # drop table if it already exists
    cursor.execute('drop table if exists transactions')
    cursor.execute(Staging_public.transactions)
    # import the csv file to create a dataframe
    address_df = pd.read_csv('Datasets/transactions.csv')
    # df to sql
    # df to sql(sql table, alchemy connector)
    address_df.to_sql('transactions', con=conn, if_exists='replace',
                      schema='public', index=False)

    sql1 = '''select * from transactions;'''
    cursor.execute(sql1)
    cursor.fetchone()
    conn1.commit()
    conn1.close()
    print('connected and added to transactions table')


# all public load csv into postgres table inside 1 function


def loadAllToPublicSchema():
    connectAndLoadAddress()
    connectAndLoadCustomers()
    connectAndLoadStorages()
    connectAndLoadTransactions()


loadAllToPublicSchema()

# Insert from public to adeleke_amoda created schema loading.py
