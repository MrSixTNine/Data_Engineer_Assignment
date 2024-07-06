import pandas as pd
import  os
import sys
from sqlalchemy import create_engine
from pathlib import Path

# Get the current directory (where this script is located)
current_dir = Path(sys.path[0])
print(current_dir)

# Construct the relative path to the JSON file
file_name = 'product_catalog[1].csv'
file_path = os.path.join(current_dir, '..', 'Sources', file_name)

df = pd.read_csv(file_path)

# Convert 'price' to numeric, invalid parsing will be set as NaN
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Filter out rows where 'price' is less than 0 or NaN
df = df[(df['price'] >= 0) & (df['price'].notna())]

# Function to generate product name based on product_id
def generate_product_name(row):
    if pd.isna(row['product_name']):
        product_num = row['product_id'][1:]  # Extract numeric part of product_id
        product_num_int = int(product_num)
        return f"Product {product_num_int}"
    return row['product_name']

# Apply function to 'product_name' column
df['product_name'] = df.apply(generate_product_name, axis=1)

# Create an engine instance
engine = create_engine('postgresql://master_tk:120344@localhost:5432/postgres')

# Insert data into PostgreSQL database
try:
    df.to_sql('customer_transactions', engine, if_exists='append', index=False, schema='pre_prd')
    print("Data successfully inserted into PostgreSQL database.")
except Exception as e:
    print("Error:", e)