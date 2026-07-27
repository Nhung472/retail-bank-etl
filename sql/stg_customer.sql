CREATE OR REPLACE TABLE STG_CUSTOMER AS

SELECT DISTINCT

    customer_id,

    customer_name,

    dob,

    phone,

    segment,

    branch_id,

    rm_id,

    record_effective_date,

    source_update_date

FROM RAW_CUSTOMER;