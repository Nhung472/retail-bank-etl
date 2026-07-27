from pathlib import Path
from database import get_connection

ROOT_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = ROOT_DIR / "sql"

con = get_connection()

# Build REJECT_TRANSACTION
print("Running reject_transaction.sql...")
sql = (SQL_DIR / "reject_transaction.sql").read_text(encoding="utf-8")
con.execute(sql)
print("REJECT_TRANSACTION created successfully.")

# Build FACT_TRANSACTION
print("Running fact_transaction.sql...")
sql = (SQL_DIR / "fact_transaction.sql").read_text(encoding="utf-8")
con.execute(sql)
print("FACT_TRANSACTION created successfully.")

con.close()