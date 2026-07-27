from database import get_connection

con = get_connection()

tables = [
    "RAW_BRANCH",
    "RAW_CUSTOMER",
    "RAW_PRODUCT",
    "RAW_RM",
    "RAW_TRANSACTIONS",
]

for table in tables:

    count = con.execute(f"""
        SELECT COUNT(*)
        FROM {table}
    """).fetchone()[0]

    print(f"{table:<20} {count}")

con.close()