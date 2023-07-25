# create tables into db.public schema
# Not stating the schema will create in the public folder

class Staging_public:
    address = """
    create table if not exists address(
    id INTEGER,
    city VARCHAR(200),
    postal_code BIGINT,
    country VARCHAR(100),
    country_code VARCHAR(50),
    state VARCHAR(100)
    
    );
    """

    customers = """
    CREATE TABLE IF NOT EXISTS customers(
    id INT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    gender VARCHAR(50),
    website TEXT,
    address_id INTEGER
    
    );
    """

    storages = """
    CREATE TABLE IF NOT EXISTS storages(
    id INTEGER,
    room_number INTEGER,
    street_address TEXT,
    state TEXT,
    country TEXT,
    opens_at INTEGER,
    closes_at INTEGER,
    charge_per_space DECIMAL(18, 2) 

    );
    """
# fact table

    transactions = """
    CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER,
    customer INTEGER,
    storage_center INTEGER,
    space_qty INTEGER,
    action TEXT,
    date INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week INTEGER 
    );
    """
