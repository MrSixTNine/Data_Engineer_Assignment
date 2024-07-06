from sqlalchemy import create_engine


def insert_into_postgres(df, table_name, schema_name, engine):
    try:
        # Insert the DataFrame into the specified table within the specified schema
        df.to_sql(table_name, engine, if_exists='append', index=False, schema=schema_name)
        print(f"Data successfully inserted into {schema_name}.{table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        engine.dispose()
