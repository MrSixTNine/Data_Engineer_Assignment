import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
import pandas as pd

def insert_into_postgres(df, table_name, schema_name):
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
    # Create a SQLAlchemy engine
    engine = create_engine(CONNECTION_URL)
    try:
        # Insert the DataFrame into the specified table within the specified schema
        df.to_sql(table_name, engine, if_exists='append', index=False, schema=schema_name)
        print(f"Data successfully inserted into {schema_name}.{table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        engine.dispose()

def get_from_postgres(query):
    # Load environment variables from config.env file
    dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    # Database connection details
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DATABASE = os.getenv('DATABASE')

    # Construct the connection string
    conn_string = f"dbname='{DATABASE}' user='{USER}' host='{HOST}' password='{PASSWORD}' port='{PORT}'"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(conn_string)

    # Create a cursor object using the connection
    cursor = conn.cursor()

    try:
        # Execute the SQL query
        cursor.execute(query)
        
        # Fetch all rows from the cursor into a list of tuples
        rows = cursor.fetchall()

        # Get the column names from the cursor description
        columns = [desc[0] for desc in cursor.description]

        # Create a pandas DataFrame from the fetched rows and columns
        df = pd.DataFrame(rows, columns=columns)

        return df

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
