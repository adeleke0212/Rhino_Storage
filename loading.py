from sqlalchemy import create_engine
import pandas as pd
import os
import psycopg2
from configparser import ConfigParser
from sql.create import Staging
from public_create import Staging_public
from sql.insert import Staging as Insert


# use sys to import from other directory, check ms word documentation
# Timi said no need, putting __init__.py in the folder allows normal import

config = ConfigParser()
config.read('.env')

# Database connection parameters

DB_HOST = config['DB_STAGING_CONN']['host']
DB_PASSWORD = config['DB_STAGING_CONN']['password']
DB_PORT = config['DB_STAGING_CONN']['port']
DB_USER = config['DB_STAGING_CONN']['user']
DB_DATABASE = config['DB_STAGING_CONN']['database']
DB_SCHEMA = config['DB_STAGING_CONN']['schema']

# Create Table Parameters

STORAGE_TRANS = config['DB_TABLES']['STORAGE_TRANS']
CUSTOMERS = config['DB_TABLES']['CUSTOMERS']
DATES = config['DB_TABLES']['DATES']
ACTIONS = config['DB_TABLES']['ACTIONS']
STORAGES = config['DB_TABLES']['STORAGES']


def database_connector():
    connection = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, password=DB_PASSWORD, user=DB_USER, database=DB_DATABASE)
    print('Connection established')
    return connection


def createSchema():
    con = database_connector()
    cursor = con.cursor()
    cursor.execute(Staging.schema.format(DB_SCHEMA))
    con.commit()
    cursor.close()
    con.close()
    print('Schema created')


def createTransactionFact():
    conn = database_connector()
    cursor = conn.cursor()
    cursor.execute(Staging.fact_table_storage_trans.format(
        DB_SCHEMA, STORAGE_TRANS))
    conn.commit()
    cursor.close()
    conn.close()
    print('Fact table created')


def customersDims():
    connection = database_connector()
    cursor = connection.cursor()
    cursor.execute(Staging.customers.format(DB_SCHEMA, CUSTOMERS))
    connection.commit()
    cursor.close()
    connection.close()
    print('Customers table created')


def datesDims():
    connect = database_connector()
    cursor = connect.cursor()
    cursor.execute(Staging.dates.format(DB_SCHEMA, DATES))
    connect.commit()
    cursor.close()
    connect.close()
    print(f"{DATES} table created")  # print dates table created.


def actionsDim():
    connection = database_connector()
    cursor = connection.cursor()
    cursor.execute(Staging.actions.format(DB_SCHEMA, ACTIONS))
    connection.commit()
    cursor.close()
    connection.close()
    print('Actions table created')


def storagesDims():
    connection = database_connector()
    cursor = connection.cursor()
    cursor.execute(Staging.storages.format(DB_SCHEMA, STORAGES))
    connection.commit()
    cursor.close()
    connection.close()
    print('Storages table created')


def createAllTables():
    createTransactionFact()
    customersDims()
    datesDims()
    actionsDim()
    storagesDims()


# createAllTables()

# so import error importing my csv into pgadmin, now attempting loading my dataframe into
# postgress using sqlalchemy - first step pip install sqlalchemy-more on documentation.txt


# communication between sqlalchemy conn and postgrees DB using the driver psycopg2

# engine = create_engine(dialect+driver://username:password@host:port/database_name)

# call my psycopg2 connection

# I have loaded all tables into the database, using sql alchemy create-engine syntax, check public_create.py and public_load.py


# Insert into my schema.tables by selecting data from public tables(imported csv files)
def insertIntoCustomers():
    conn = database_connector()
    cursor = conn.cursor()
    cursor.execute(Insert.customers.format(DB_SCHEMA, CUSTOMERS))
    conn.commit()
    cursor.close()
    conn.close()
    print('Inserted into schema.customers table')


# insertIntoCustomers()

def insertIntoStorages():
    connection = database_connector()
    cursor = connection.cursor()
    cursor.execute(Insert.storages.format(DB_SCHEMA, STORAGES))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Inserted into {STORAGES} table")


# insertIntoStorages()

def insertIntoDates():
    conn = database_connector()
    cursor = conn.cursor()
    cursor.execute(Insert.dates.format(DB_SCHEMA, DATES))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted into {DATES} table")


# insertIntoDates()

def insertIntoActions():
    connection = database_connector()
    cursor = connection.cursor()
    cursor.execute(Insert.actions.format(DB_SCHEMA, ACTIONS))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Inserted into {ACTIONS} table")


# insertIntoActions()

def insertIntoStorageTransactionsFact():
    conn = database_connector()
    cursor = conn.cursor()
    cursor.execute(Insert.transactions.format(DB_SCHEMA, STORAGE_TRANS))
    conn.commit()
    cursor.close()
    conn.close()
    print('Inserted into Facts table')


def runallInserts():
    insertIntoCustomers()
    insertIntoStorages()
    insertIntoDates()
    insertIntoActions()
    insertIntoStorageTransactionsFact


runallInserts()
