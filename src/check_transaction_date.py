from database import get_connection

con = get_connection()

print("=== NULL transaction_date ===")

print(
    con.execute("""
        SELECT COUNT(*)
        FROM STG_TRANSACTION
        WHERE transaction_date IS NULL
    """).fetchdf()
)

print("\n=== Sample rows ===")

print(
    con.execute("""
        SELECT
            transaction_id,
            customer_id,
            transaction_date
        FROM STG_TRANSACTION
        WHERE transaction_date IS NULL
        LIMIT 20
    """).fetchdf()
)

con.close()