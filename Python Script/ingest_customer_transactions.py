import json
import pandas as pd
import os
import psycopg2
from shared_functions import *
import sys
from pathlib import Path
from dotenv import load_dotenv

table_name = 'customer_transactions'
schema_name = 'pre_prd'

# Load environment variables from config.env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Database connection details
DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DBAPI = os.getenv('DBAPI')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

# Create the connection URL
CONNECTION_URL = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Get the current directory (where this script is located)
current_dir = Path(sys.path[0])

# Construct the relative path to the JSON file
file_name = 'customer_transactions[2].json'
file_path = os.path.join(current_dir, '..', 'Sources', file_name)

# Read JSON file to datafram
with open(file_path, 'r') as file:
    data = json.load(file)
df = pd.DataFrame(data)

# Convert data type
df['transaction_id'] = df['transaction_id'].astype(str)
df['customer_id'] = df['customer_id'].astype(str)
df['product_id'] = df['product_id'].astype(str)
df['quantity'] = df['quantity'].astype(int)
df['price'] = df['price'].astype(float)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Clean transaction data
df.drop_duplicates(subset='transaction_id', keep="first", inplace=True)

print(df)


