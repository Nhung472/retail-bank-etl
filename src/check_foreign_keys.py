from database import get_connection

con = get_connection()

queries = {
    "customer_key": """
        SELECT COUNT(*)
        FROM FACT_TRANSACTION
        WHERE customer_key IS NULL
    """,

    "product_key": """
        SELECT COUNT(*)
        FROM FACT_TRANSACTION
        WHERE product_key IS NULL
    """,

    "branch_key": """
        SELECT COUNT(*)
        FROM FACT_TRANSACTION
        WHERE branch_key IS NULL
    """,

    "rm_key": """
        SELECT COUNT(*)
        FROM FACT_TRANSACTION
        WHERE rm_key IS NULL
    """
}

print("-" * 40)

for name, sql in queries.items():

    cnt = con.execute(sql).fetchone()[0]

    print(f"{name:<20}: {cnt}")

con.close()