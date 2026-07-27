from database import get_connection

con = get_connection()

tables = [
    "RAW_TRANSACTIONS",
    "STG_TRANSACTION",
    "FACT_TRANSACTION"
]

print("-" * 40)
print(f"{'Table':<25} {'Rows':>10}")
print("-" * 40)

for table in tables:
    count = con.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table:<25} {count:>10}")

con.close()