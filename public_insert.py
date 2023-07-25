# Actually just import the csv file into the pgadmin using the import/export file path and the created table
# ensure you specify the column to import if not importing all columns, all columns must match the created table

# KeyErrorERROR:  could not open file "/Users/adeleke/Documents/Rhino_Storage/Datasets/address.csv" for reading: Permission denied
# HINT:  COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy.
# SQL state: 42501

# use sql alchemy and connect tp postgress to insert csv files into postgres table
# Syntax:

# from sqlalchemy import create_engine

# engine = create_engine(dialect+driver://username:password@host:port/database_name)

# Parameters:
# postgres +
# dialect – Name of the DBMS. The dialect is the system SQLAlchemy uses to communicate with various types of DBAPIs and databases like PostgreSQL, MySQL, MS SQL, etc.
# driver – Name of the DB API that moves information between SQLAlchemy and the database.
# Username – Name of the admin
# Password – Password of the admin
# host – Name of the host in which the database is hosted
# port – port number through which the database can be accessed
# database_name– Name of the database
# Note: It is extremely unsafe to explicitly mention your password in the code. In order to avoid this, we can hash our password with urllib library as shown below

# check bookmarked scq tutorials brave browser for more

# first pip install !pip install psycopg2-binary SQLAlchemy

# What kind of database are we communicating with? (PostgreSQL)
# What python DBAPI driver are we using? (psycopg2)
# How do we locate the database? (localhost:5432)

# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")
