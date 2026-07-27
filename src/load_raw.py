from database import get_connection, RAW_DATA_PATH

# Kết nối tới DuckDB
con = get_connection()

# Danh sách các file CSV
tables = {
    "RAW_BRANCH": "RAW_BRANCH.csv",
    "RAW_CUSTOMER": "RAW_CUSTOMER.csv",
    "RAW_PRODUCT": "RAW_PRODUCT.csv",
    "RAW_RM": "RAW_RM.csv",
    "RAW_TRANSACTIONS": "RAW_TRANSACTIONS.csv",
}

for table_name, file_name in tables.items():

    file_path = RAW_DATA_PATH / file_name

    print(f"Loading {file_name}...")

    con.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_csv_auto('{file_path.as_posix()}', HEADER=TRUE);
    """)

    count = con.execute(f"""
        SELECT COUNT(*)
        FROM {table_name}
    """).fetchone()[0]

    print(f"Loaded {count} rows into {table_name}")

con.close()

print("All RAW tables loaded successfully.")