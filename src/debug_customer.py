from database import get_connection

con = get_connection()

df = con.execute("""
SELECT DISTINCT
    t.customer_id
FROM STG_TRANSACTION t
LEFT JOIN DIM_CUSTOMER c
    ON t.customer_id = c.customer_id
    AND t.transaction_date BETWEEN c.effective_from AND c.effective_to
WHERE c.customer_key IS NULL
ORDER BY t.customer_id;
""").fetchdf()

print(df)

con.close()