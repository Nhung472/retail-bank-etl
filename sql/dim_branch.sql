CREATE OR REPLACE TABLE DIM_BRANCH AS

SELECT

    ROW_NUMBER() OVER(
        ORDER BY branch_id
    ) AS branch_key,

    branch_id,

    branch_name,

    region

FROM STG_BRANCH;