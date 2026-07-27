-- ===============================
-- Reject duplicate transaction
-- ===============================

CREATE OR REPLACE TABLE REJECT_TRANSACTION AS

WITH duplicate_check AS (

    SELECT
        *,
        COUNT(*) OVER(
            PARTITION BY transaction_id
        ) AS cnt

    FROM RAW_TRANSACTIONS

)

SELECT

    transaction_id,
    customer_id,
    product_id,
    branch_id,
    rm_id,
    transaction_date,
    transaction_type,
    channel,
    amount_vnd,

    'Duplicate transaction_id' AS reject_reason

FROM duplicate_check

WHERE cnt > 1;



-- ===============================
-- Clean staging transaction
-- ===============================


CREATE OR REPLACE TABLE STG_TRANSACTION AS


WITH ranked AS (

    SELECT

        *,

        ROW_NUMBER() OVER(
            PARTITION BY transaction_id
            ORDER BY transaction_date DESC NULLS LAST
        ) AS rn


    FROM RAW_TRANSACTIONS

)

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

FROM ranked

WHERE rn = 1;