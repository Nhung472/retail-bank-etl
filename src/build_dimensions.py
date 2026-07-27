from pathlib import Path

from database import get_connection

ROOT = Path(__file__).resolve().parent.parent

SQL_DIR = ROOT / "sql"

sql_files = [

    "dim_branch.sql",

    "dim_product.sql",

    "dim_rm.sql",

    "dim_customer.sql"

]

con = get_connection()

for file in sql_files:

    print(f"Running {file}")

    sql = (SQL_DIR / file).read_text(encoding="utf-8")

    con.execute(sql)

print("\nDimensions created successfully.")

con.close()