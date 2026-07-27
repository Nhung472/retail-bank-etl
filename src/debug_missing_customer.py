from database import get_connection

con = get_connection()

df = con.execute("""
SELECT
    customer_id,
    effective_from,
    effective_to,
    is_current
FROM DIM_CUSTOMER
WHERE customer_id IN (
    6,9,21,22,39,47,60,67,71,82
)
ORDER BY customer_id;
""").fetchdf()

print(df)

con.close()