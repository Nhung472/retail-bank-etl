from database import get_connection


con = get_connection()


df = con.execute("""
SELECT
    transaction_id,
    COUNT(*) AS cnt
FROM FACT_TRANSACTION
GROUP BY transaction_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC
""").fetchdf()


print(df)


con.close()