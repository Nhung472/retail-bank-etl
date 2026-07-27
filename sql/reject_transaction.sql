CREATE OR REPLACE TABLE REJECT_TRANSACTION AS

SELECT
    *,
    CASE
        WHEN transaction_date IS NULL THEN 'Missing transaction_date'
        WHEN customer_id IS NULL THEN 'Missing customer_id'
        WHEN product_id IS NULL THEN 'Missing product_id'
        WHEN amount_vnd <= 0 THEN 'Invalid amount'
    END AS reject_reason
FROM STG_TRANSACTION
WHERE
    transaction_date IS NULL
    OR customer_id IS NULL
    OR product_id IS NULL
    OR amount_vnd <= 0;