from database import get_connection

con = get_connection()

df = con.execute("""
SELECT
    t.transaction_id,
    t.customer_id,
    t.transaction_date,
    c.record_effective_date
FROM STG_TRANSACTION t

LEFT JOIN DIM_CUSTOMER d
ON t.customer_id = d.customer_id
AND t.transaction_date BETWEEN d.effective_from AND d.effective_to

LEFT JOIN (
    SELECT
        customer_id,
        MIN(record_effective_date) AS record_effective_date
    FROM STG_CUSTOMER
    GROUP BY customer_id
) c
ON t.customer_id = c.customer_id

WHERE d.customer_key IS NULL

ORDER BY t.customer_id,
         t.transaction_date;
""").fetchdf()

print(df)

con.close()