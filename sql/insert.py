# First I want to load my address.csv, transactions.csv, storages.csv and customers.csv into the public  schema, but I'll also create a table for it in the public schema

# or can also extract each columns of the table as pandas df and then convert to json, then load that straight..I am goimg to attempt both steps


# Note that:  The INSERT INTO SELECT statement copies data from one table and inserts it into another table. here from public.tables to schema.tables
# Note: The existing records in the target table are unaffected.

# Insert into tables using insert select
class Staging:
    customers = """
    INSERT INTO {}.{} (customer_id, first_name, last_name, email, gender, address_id,
    city, postal_code, state, country)
    SELECT 
        customers.id, 
        customers.first_name, 
        customers.last_name, 
        customers.email, 
        customers.gender, 
        customers.address_id, 
        address.city, 
        address.postal_code, 
        address.state,
        address.country
        
    from public.customers
    left join public.address 
    ON customers.address_id = address.id
    """
    storages = """
    INSERT INTO {}.{}(id, room_number, street_address, state, country,
    opens_at, closes_at, charge_per_space)
    SELECT
    storages.id,
    storages.room_number,
    storages.street_address,
    storages.state,
    storages.country,
    storages.opens_at :: integer,
    storages.closes_at :: integer,
    SUBSTRING(storages.charge_per_space, 2) :: REAL AS charge_per_space
    from public.storages

    """
# :: this is CAST symbol in postgres sql used to covert to another datatypes in sql
# substring extract character from a string. substring(string to extract from, starting position, no of characters to extract)
# note: substring starts at position 1
# we are attempting to remove the $sign from the column values
    dates = """
    INSERT INTO {}.{}(id, date, year, month, day, quarter)
    SELECT
    transactions.id,
    transactions.date,
    transactions.year,
    transactions.month,
    transactions.day,
    CASE WHEN transactions.month <= 3 THEN 1
        WHEN transactions.month > 3 AND transactions.month <= 6 THEN 2
        WHEN transactions.month > 6 AND transactions.month <= 9 THEN 3
        WHEN transactions.month > 9 THEN 4
    END as quarter
    from public.transactions

   
    """
    transactions = """
    INSERT INTO {}.{}(transaction_id, customer_id, storage_id, date_id, space_qty,
    action_id, charge_per_space, total_amount)
    SELECT
    transactions.id as transaction_id,
    transactions.customer as customer_id,
    transactions.storage_center as storage_id,
    dates.id  as date_id,
    transactions.space_qty :: integer space_qty,
    actions.id as action_id,
    storages.charge_per_space as charge_per_space,
    (storages.charge_per_space * space_qty) as total_amount
    from public.transactions
    left join adeleke_amoda.actions
    on actions.name = transactions.action
    left join adeleke_amoda.dates
    on transactions.date = dates.date
    left join adeleke_amoda.storages 
    on storages.id = transactions.storage_center

    """
    actions = """
    INSERT INTO {}.{}(name)
    SELECT DISTINCT action
    from public.transactions
    """
