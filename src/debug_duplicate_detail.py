from database import get_connection


con = get_connection()


df = con.execute("""
SELECT

    t.transaction_id,

    t.customer_id,
    t.product_id,
    t.branch_id,
    t.rm_id,

    c.customer_key,
    c.effective_from,
    c.effective_to,

    p.product_key

FROM STG_TRANSACTION t


LEFT JOIN DIM_CUSTOMER c
ON t.customer_id = c.customer_id
AND t.transaction_date 
    BETWEEN c.effective_from AND c.effective_to


LEFT JOIN DIM_PRODUCT p
ON t.product_id = p.product_id


WHERE t.transaction_id IN (
    5030,
    3154,
    3212
)

ORDER BY t.transaction_id

""").fetchdf()


print(df)


con.close()