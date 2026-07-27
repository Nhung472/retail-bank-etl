CREATE OR REPLACE TABLE STG_TRANSACTION AS

SELECT

    transaction_id,

    customer_id,

    product_id,

    branch_id,

    rm_id,

    transaction_date,

    transaction_type,

    channel,

    amount_vnd

FROM RAW_TRANSACTIONS;