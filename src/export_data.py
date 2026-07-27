from pathlib import Path
from database import get_connection


ROOT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = ROOT_DIR / "data" / "output"


OUTPUT_DIR.mkdir(
    exist_ok=True
)


con = get_connection()


tables = [

    "DIM_CUSTOMER",
    "DIM_PRODUCT",
    "DIM_BRANCH",
    "DIM_RM",
    "FACT_TRANSACTION"

]


for table in tables:

    print(f"Exporting {table}...")


    df = con.execute(
        f"""
        SELECT *
        FROM {table}
        """
    ).fetchdf()


    output_file = OUTPUT_DIR / f"{table.lower()}.csv"


    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )


    print(
        f"Saved: {output_file}"
    )


con.close()


print("\nExport completed!")