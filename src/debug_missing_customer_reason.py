from database import get_connection

con = get_connection()

df = con.execute("""
SELECT
    t.transaction_id,
    t.customer_id,
    t.transaction_date,
    (
        SELECT MIN(record_effective_date)
        FROM STG_CUSTOMER c
        WHERE c.customer_id = t.customer_id
    ) AS first_effective_date
FROM STG_TRANSACTION t
LEFT JOIN DIM_CUSTOMER d
ON t.customer_id = d.customer_id
AND t.transaction_date BETWEEN d.effective_from AND d.effective_to
WHERE d.customer_key IS NULL
ORDER BY t.customer_id, t.transaction_date;
""").fetchdf()

print(df)

con.close()