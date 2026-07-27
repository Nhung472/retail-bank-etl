CREATE OR REPLACE TABLE DIM_RM AS

SELECT

    ROW_NUMBER() OVER(
        ORDER BY rm_id
    ) AS rm_key,

    rm_id,

    rm_name,

    branch_id,

    rm_type

FROM STG_RM;