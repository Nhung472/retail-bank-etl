from database import get_connection

tables = [

    "DIM_BRANCH",

    "DIM_PRODUCT",

    "DIM_RM",

    "DIM_CUSTOMER"

]

con = get_connection()

for table in tables:

    cnt = con.execute(

        f"SELECT COUNT(*) FROM {table}"

    ).fetchone()[0]

    print(f"{table:<20}{cnt}")

con.close()