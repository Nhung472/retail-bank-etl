from database import get_connection

con = get_connection()

print("REJECT_TRANSACTION")

print(
    con.execute("""
    SELECT
        reject_reason,
        COUNT(*) AS total
    FROM REJECT_TRANSACTION
    GROUP BY reject_reason
    ORDER BY total DESC;
    """).fetchdf()
)

print("\nFACT_TRANSACTION")

print(
    con.execute("""
    SELECT COUNT(*) AS total_rows
    FROM FACT_TRANSACTION;
    """).fetchdf()
)

con.close()