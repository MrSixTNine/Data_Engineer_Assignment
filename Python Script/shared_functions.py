from sqlalchemy import create_engine


def insert_into_postgres(df, table_name, schema_name, engine):
    try:
        # Insert the DataFrame into the specified table within the specified schema
        df.to_sql(name=table_name, con=engine, schema=schema_name, if_exists='append', index=False)
        print(f"Data successfully inserted into {schema_name}.{table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        engine.dispose()
