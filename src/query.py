from database import get_connection

con = get_connection()

df = con.execute("""
SELECT
    t.customer_id,
    t.transaction_date,
    c.effective_from,
    c.effective_to
FROM STG_TRANSACTION t
LEFT JOIN DIM_CUSTOMER c
ON t.customer_id = c.customer_id
AND t.transaction_date BETWEEN c.effective_from AND c.effective_to
WHERE t.customer_id = 22
ORDER BY t.transaction_date;
""").fetchdf()

print(df)

con.close()