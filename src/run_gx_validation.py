from database import get_connection

import great_expectations as gx
from pathlib import Path


# ==========================
# Load DuckDB data
# ==========================

con = get_connection()

df = con.execute("""
    SELECT *
    FROM FACT_TRANSACTION
""").fetchdf()

con.close()


print("FACT_TRANSACTION rows:", len(df))


# ==========================
# GX Context
# ==========================

ROOT_DIR = Path(__file__).resolve().parent.parent

context = gx.get_context(
    mode="file",
    project_root_dir=str(ROOT_DIR / "gx")
)


# ==========================
# Datasource
# ==========================

datasource = context.data_sources.get(
    "pandas_datasource"
)


# ==========================
# Data Asset
# ==========================

try:
    asset = datasource.get_asset(
        "fact_transaction"
    )

except:

    asset = datasource.add_dataframe_asset(
        name="fact_transaction"
    )


# ==========================
# Batch
# ==========================

try:
    batch_definition = asset.get_batch_definition(
        "fact_transaction_batch"
    )

except:

    batch_definition = asset.add_batch_definition_whole_dataframe(
        "fact_transaction_batch"
    )


batch = batch_definition.get_batch(
    batch_parameters={
        "dataframe": df
    }
)


print("Batch created")

# ==========================
# Create / Load Expectation Suite
# ==========================

try:
    suite = context.suites.get(
        "fact_transaction_quality"
    )

    # clear expectation cũ
    suite.expectations = []

except:

    suite = gx.ExpectationSuite(
        name="fact_transaction_quality"
    )

    context.suites.add(
        suite
    )


# ==========================
# Expectations
# ==========================

from great_expectations.expectations import *


expectations = [

    ExpectColumnValuesToNotBeNull(
        column="transaction_date"
    ),


    ExpectColumnValuesToBeUnique(
        column="transaction_id"
    ),


    ExpectColumnValuesToBeBetween(
        column="amount_vnd",
        min_value=0
    ),


    ExpectColumnValuesToNotBeNull(
        column="customer_key"
    ),


    ExpectColumnValuesToNotBeNull(
        column="product_key"
    )

]


for e in expectations:
    suite.add_expectation(e)



# ==========================
# Validate
# ==========================

result = batch.validate(
    suite
)


print("\n========================")
print("DATA QUALITY RESULT")
print("========================")


for r in result.results:

    status = "PASS" if r.success else "FAIL"

    print(
        status,
        "-",
        r.expectation_config.type
    )


print("========================")