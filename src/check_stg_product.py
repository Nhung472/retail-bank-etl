from database import get_connection


con = get_connection()


df = con.execute("""
DESCRIBE STG_PRODUCT
""").fetchdf()


print(df)


con.close()