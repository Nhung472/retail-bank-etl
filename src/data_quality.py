from database import get_connection
import great_expectations as gx

con = get_connection()

# Đọc FACT_TRANSACTION vào DataFrame
df = con.execute("""
SELECT *
FROM FACT_TRANSACTION
""").fetchdf()

con.close()

# Chuyển DataFrame thành GX Dataset
gx_df = gx.from_pandas(df)

print("=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

# 1. transaction_id unique
r1 = gx_df.expect_column_values_to_be_unique("transaction_id")
print("Unique transaction_id :", r1.success)

# 2. amount > 0
r2 = gx_df.expect_column_values_to_be_between(
    "amount_vnd",
    min_value=1
)
print("Amount > 0 :", r2.success)

# 3. transaction_date not null
r3 = gx_df.expect_column_values_to_not_be_null(
    "transaction_date"
)
print("Transaction date not null :", r3.success)

# 4. customer_key not null
r4 = gx_df.expect_column_values_to_not_be_null(
    "customer_key"
)
print("Customer FK :", r4.success)

# 5. product_key not null
r5 = gx_df.expect_column_values_to_not_be_null(
    "product_key"
)
print("Product FK :", r5.success)

print("=" * 60)