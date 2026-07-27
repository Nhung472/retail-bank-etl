import duckdb

con=duckdb.connect("retail_bank.duckdb")

con.execute("""

CREATE OR REPLACE TABLE DIM_PRODUCT AS

SELECT

row_number() over() product_key,

product_id,

product_name,

product_type

FROM RAW_PRODUCT

""")