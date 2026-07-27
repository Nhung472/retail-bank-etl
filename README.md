# retail-bank-etl

tạo folder:  retail-bank-etl
cấu trúc folder: 
retail-bank-etl
│
├── data
│   ├── raw
│   └── output
│
├── docs
│
├── src
│
├── sql
│
├── gx
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

Bước 2. Tạo Virtual Environment
python -m venv .venv
.venv\Scripts\activate

Bước 3. Cài package
pip install duckdb pandas great_expectations pyarrow
pip freeze > requirements.txt

Bước 4. Tạo file .gitignore
Bước 5. Tạo database DuckDB
Bước 6. Tạo thư mục src
tạo src/database.py
Bước 7. Load CSV
Tạo src/load_raw.py
Bước 8. Chạy thử
=> python src/load_raw.py
Bước 9. Kiểm tra dữ liệu
src/explore.py
=> python src/explore.py
Bước 10. Thiết kế Star Schema
docs/star_schema.md
Bước 11. Xác định Surrogate Key
Không dùng customer_id làm Primary Key.
Mà sẽ dùng customer_key

Load thử data
=> Bước 8. Chạy chương trình
Kiểm tra data type, ...
=> python src/explore.py
Kiểm tra số dòng
=> python src/check_row_count.py

PHẦN 2 - STAGING + DATA CLEANING + DIMENSION
sql/
│
├── stg_branch.sql
├── stg_customer.sql
├── stg_product.sql
├── stg_rm.sql
├── stg_transaction.sql
└── reject_transaction.sql

Bước 9. Loại bỏ dữ liệu lỗi khỏi STG
sql/clean_transaction.sql
Sau bước này:
RAW_TRANSACTION
        │
        ▼
STG_TRANSACTION
        │
        ├──► REJECT_TRANSACTION
        │
        ▼
Clean STG_TRANSACTION

Build staging
=> python src/build_staging.py

Kiểm tra
=> python src/check_staging.py