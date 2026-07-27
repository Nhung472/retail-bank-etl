from database import get_connection


con = get_connection()


df = con.execute("""
SELECT *
FROM DIM_PRODUCT
LIMIT 10
""").fetchdf()


print(df)


con.close()