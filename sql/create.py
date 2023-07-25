class Staging:
    schema = """
    create schema if not exists {};
    """
    fact_table_storage_trans = """
    create table if not exists {}.{}(
    id INTEGER NOT NULL,
    transaction_id INTEGER,
    customer_id INTEGER,
    storage_id INT,
    date_id integer,
    space_qty_id INTEGER,
    action_id INTEGER,
    space_qty INTEGER,
    charge_per_space REAL,
    total_amount REAL

    );
    
    """
    # dims either pickup, reserve or drop off
    actions = """
    CREATE TABLE IF NOT EXISTS {}.{}(
    action_id INTEGER,
    name TEXT
    );

    """
    # joined column from address date joined on address id
    customers = """
    CREATE TABLE if not exists {}.{}(
    id SERIAL,
    customer_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    gender TEXT NOT NULL,
    address_id INT NOT NULL,
    city TEXT NOT NULL,
    postal_code INTEGER NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL
    

    );
    """

    storages = """
    CREATE TABLE IF NOT EXISTS {}.{}(
    id SERIAL,
    room_number INTEGER NOT NULL,
    street_address TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL,
    opens_at INTEGER NOT NULL,
    closes_at INTEGER NOT NULL,
    charge_per_space REAL NOT NULL

    );
    """

    dates = """
    CREATE TABLE IF NOT EXISTS {}.{} (
    id SERIAL,
    date INTEGER NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
    
    );
    
    """
# postgres allows for generated as identity or serial instead of identity
# and serial don't go with INTEGER...JUST id serial (maybe primary key if needed or the constraint)
