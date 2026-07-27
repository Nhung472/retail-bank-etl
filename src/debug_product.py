from database import get_connection

con = get_connection()

df = con.execute("""
SELECT DISTINCT
    t.product_id
FROM STG_TRANSACTION t
LEFT JOIN DIM_PRODUCT p
    ON t.product_id = p.product_id
WHERE p.product_key IS NULL
ORDER BY t.product_id;
""").fetchdf()

print(df)

con.close()