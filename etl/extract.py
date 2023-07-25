from configparser import ConfigParser
import pandas as pd

config = ConfigParser()

config.read('.env')

base_url = config['DATASOURCE']['base_s3_url']
customers_file = config['FILES']['customers']
transaction1_file = config['FILES']['transaction_1']
transaction2_file = config['FILES']['transaction_2']
storage_data_file = config['FILES']['storage_data']
address_file = config['FILES']['address']

customers_df = pd.read_json(f"{base_url}/{customers_file}")
trans1_df = pd.read_csv(f"{base_url}/{transaction1_file}")
trans2_df = pd.read_csv(f"{base_url}/{transaction2_file}")
storage_data_df = pd.read_json(f"{base_url}/{storage_data_file}")
address_df = pd.read_csv(f"{base_url}/{address_file}")

customers_df.to_csv('Datasets/customers.csv')
trans1_df.to_csv('Datasets/transaction1.csv')
trans2_df.to_csv('Datasets/transaction2.csv')
storage_data_df.to_csv('Datasets/storages.csv')
address_df.to_csv('Datasets/address.csv')
