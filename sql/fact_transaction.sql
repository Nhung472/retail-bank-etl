CREATE OR REPLACE TABLE FACT_TRANSACTION AS
SELECT
    ROW_NUMBER() OVER (ORDER BY t.transaction_id) AS transaction_key,
    t.transaction_id,
    c.customer_key,
    p.product_key,
    b.branch_key,
    r.rm_key,
    t.transaction_date,
    t.transaction_type,
    t.channel,
    t.amount_vnd
FROM STG_TRANSACTION t
LEFT JOIN DIM_CUSTOMER c
ON t.customer_id = c.customer_id
AND t.transaction_date BETWEEN c.effective_from AND c.effective_to
LEFT JOIN DIM_PRODUCT p
ON t.product_id = p.product_id
LEFT JOIN DIM_BRANCH b
ON t.branch_id = b.branch_id
LEFT JOIN DIM_RM r
ON t.rm_id = r.rm_id
WHERE
    t.transaction_date IS NOT NULL
    AND t.customer_id IS NOT NULL
    AND t.product_id IS NOT NULL
    AND t.amount_vnd > 0;