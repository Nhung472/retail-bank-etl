                    DIM_BRANCH
                 branch_key (PK)
                 branch_id
                 branch_name
                 region
                      |
                      |
DIM_PRODUCT ----------|---------- FACT_TRANSACTION -------- DIM_RM
 product_key (PK)     |           transaction_key (PK)      rm_key (PK)
 product_id           |           customer_key (FK)         rm_id
 product_name         |           product_key (FK)          rm_name
 product_category     |           branch_key (FK)           rm_type
                      |           rm_key (FK)
                      |           transaction_id
                      |           transaction_date
                      |           transaction_type
                      |           channel
                      |           amount_vnd
                      |
                DIM_CUSTOMER
             customer_key (PK)
             customer_id
             customer_name
             dob
             phone
             segment
             branch_id
             rm_id
             effective_from
             effective_to
             is_current