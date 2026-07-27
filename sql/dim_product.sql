CREATE OR REPLACE TABLE DIM_PRODUCT AS

SELECT

    ROW_NUMBER() OVER (
        ORDER BY product_id
    ) AS product_key,

    product_id,

    product_name,

    product_category


FROM STG_PRODUCT;