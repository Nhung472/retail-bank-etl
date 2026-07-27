from database import get_connection

tables = [
    "STG_BRANCH",
    "STG_PRODUCT",
    "STG_RM",
    "STG_CUSTOMER",
    "STG_TRANSACTION",
    "REJECT_TRANSACTIONS"
]

con = get_connection()

for table in tables:

    cnt = con.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table:<25}{cnt}")

con.close()