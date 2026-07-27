CREATE OR REPLACE TABLE STG_RM AS

SELECT DISTINCT

    rm_id,
    rm_name,
    branch_id,
    rm_type

FROM RAW_RM;