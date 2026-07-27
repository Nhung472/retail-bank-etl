from pathlib import Path
import pandas as pd


OUTPUT = Path("data/output")


files = [
    "dim_customer.csv",
    "dim_product.csv",
    "dim_branch.csv",
    "dim_rm.csv",
    "fact_transaction.csv"
]


for file in files:

    path = OUTPUT / file

    print("="*50)
    print(file)

    df = pd.read_csv(path)

    print("Rows:", len(df))

    print(df.head())

    print()