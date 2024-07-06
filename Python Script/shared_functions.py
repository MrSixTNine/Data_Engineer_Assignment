import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

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
    engine = create_engine(CONNECTION_URL)
    try:
        # Insert the DataFrame into the specified table within the specified schema
        df.to_sql(table_name, engine, if_exists='append', index=False, schema=schema_name)
        print(f"Data successfully inserted into {schema_name}.{table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        engine.dispose()
