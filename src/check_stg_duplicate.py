from database import get_connection


con = get_connection()


df = con.execute("""
SELECT
    transaction_id,
    COUNT(*) cnt
FROM STG_TRANSACTION
GROUP BY transaction_id
HAVING COUNT(*) > 1
""").fetchdf()


print(df)


con.close()