CREATE OR REPLACE TABLE REJECT_TRANSACTIONS AS

SELECT *,

CASE

    WHEN transaction_id IS NULL THEN 'Missing transaction_id'

    WHEN customer_id IS NULL THEN 'Missing customer_id'

    WHEN product_id IS NULL THEN 'Missing product_id'

    WHEN branch_id IS NULL THEN 'Missing branch_id'

    WHEN rm_id IS NULL THEN 'Missing rm_id'

    WHEN amount_vnd IS NULL THEN 'Missing amount'

    WHEN amount_vnd < 0 THEN 'Negative amount'

END AS reject_reason

FROM STG_TRANSACTION

WHERE

transaction_id IS NULL

OR customer_id IS NULL

OR product_id IS NULL

OR branch_id IS NULL

OR rm_id IS NULL

OR amount_vnd IS NULL

OR amount_vnd<0;