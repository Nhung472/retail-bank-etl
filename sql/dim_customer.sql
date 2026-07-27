CREATE OR REPLACE TABLE DIM_CUSTOMER AS

SELECT

    ROW_NUMBER() OVER(
        ORDER BY customer_id
    ) AS customer_key,

    customer_id,

    customer_name,

    dob,

    phone,

    segment,

    branch_id,

    rm_id,

    record_effective_date AS effective_from,

    DATE '9999-12-31' AS effective_to,

    TRUE AS is_current


FROM STG_CUSTOMER;