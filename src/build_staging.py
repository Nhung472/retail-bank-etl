from pathlib import Path
from database import get_connection

ROOT_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = ROOT_DIR / "sql"

sql_files = [
    "stg_branch.sql",
    "stg_product.sql",
    "stg_rm.sql",
    "stg_customer.sql",
    "stg_transaction.sql",
    "reject_transactions.sql",
    "clean_transaction.sql"
]

con = get_connection()

for file in sql_files:
    print(f"Running {file}...")

    sql = (SQL_DIR / file).read_text(encoding="utf-8")

    con.execute(sql)

print("\nStaging completed!")

con.close()