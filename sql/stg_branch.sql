CREATE OR REPLACE TABLE STG_BRANCH AS

SELECT DISTINCT

    branch_id,
    branch_name,
    region

FROM RAW_BRANCH;