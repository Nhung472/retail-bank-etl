CREATE OR REPLACE TABLE STG_PRODUCT AS

SELECT DISTINCT

    product_id,
    product_name,
    product_category

FROM RAW_PRODUCT;