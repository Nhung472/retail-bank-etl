from database import get_connection


con = get_connection()


df = con.execute("""
SELECT *
FROM FACT_TRANSACTION
LIMIT 10
""").fetchdf()


print(df)


con.close()