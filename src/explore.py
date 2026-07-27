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

    print("=" * 80)
    print(table)
    print("=" * 80)

    print("\nSchema")

    print(
        con.execute(f"""
            DESCRIBE {table}
        """).fetchdf()
    )

    print("\nSample Data")

    print(
        con.execute(f"""
            SELECT *
            FROM {table}
            LIMIT 5
        """).fetchdf()
    )

    print("\n")

con.close()