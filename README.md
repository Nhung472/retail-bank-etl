# Retail Banking ETL Pipeline - Data Mart

## 1. Tổng quan dự án
Project xây dựng một **Data Mart cho ngân hàng bán lẻ** nhằm phục vụ bài toán phân tích:
> **Hiệu quả kinh doanh sản phẩm bán lẻ theo Chi nhánh và Relationship Manager (RM)**
Hệ thống mô phỏng một pipeline dữ liệu trong môi trường ngân hàng, bắt đầu từ dữ liệu nguồn (RAW), qua các bước làm sạch, xử lý lịch sử dữ liệu, xây dựng Data Warehouse Model và kiểm tra chất lượng dữ liệu.

---

## 2. Mục tiêu dự án
Các mục tiêu chính:

* Thiết kế mô hình dữ liệu dạng **Star Schema**
* Xây dựng pipeline ETL từ RAW → STAGING → DATA MART
* Xử lý dữ liệu lỗi trong quá trình ingestion
* Xây dựng Dimension và Fact table
* Áp dụng **SCD Type 2** cho dữ liệu khách hàng
* Kiểm tra Data Quality bằng **Great Expectations**
* Export Data Mart phục vụ báo cáo BI / Analytics

---

# 3. Dataset
Dữ liệu đầu vào gồm 5 bảng RAW mô phỏng hệ thống ngân hàng:

| Bảng             | Mô tả                          |
| ---------------- | ------------------------------ |
| RAW_TRANSACTIONS | Thông tin giao dịch khách hàng |
| RAW_CUSTOMER     | Thông tin khách hàng           |
| RAW_PRODUCT      | Danh mục sản phẩm              |
| RAW_BRANCH       | Thông tin chi nhánh            |
| RAW_RM           | Relationship Manager           |

---

# 4. Công nghệ sử dụng
| Công nghệ          | Mục đích                |
| ------------------ | ----------------------- |
| Python             | Xây dựng ETL Pipeline   |
| SQL                | Data Transformation     |
| DuckDB             | Analytical Database     |
| Pandas             | Data Processing         |
| Great Expectations | Data Quality Validation |
| Draw.io            | Data Modeling           |

---

# 5. Kiến trúc Pipeline
Luồng xử lý dữ liệu:

```
                CSV Source Files

                      |
                      v

                 RAW Layer

 RAW_CUSTOMER
 RAW_PRODUCT
 RAW_BRANCH
 RAW_RM
 RAW_TRANSACTION

                      |
                      v


              STAGING Layer

 - Data Cleaning
 - Data Standardization
 - Reject Handling

                      |
                      v

              DATA MART Layer

        DIM_CUSTOMER (SCD Type 2)

        DIM_PRODUCT

        DIM_BRANCH

        DIM_RM

                      |
                      v

              FACT_TRANSACTION

                      |
                      v

              Data Quality Check

            Great Expectations

```

---

# 6. Data Modeling - Star Schema

Mục tiêu của Data Mart:

> Phân tích doanh thu sản phẩm theo chi nhánh và RM.

Mô hình dữ liệu:

```
                  DIM_PRODUCT

                       |

                       |

DIM_CUSTOMER ---- FACT_TRANSACTION ---- DIM_BRANCH

                       |

                       |

                    DIM_RM

```

---

# 7. Thiết kế bảng dữ liệu

## 7.1 FACT_TRANSACTION

### Grain

Mỗi dòng dữ liệu đại diện cho:

> Một giao dịch phát sinh trong hệ thống.

Schema:

| Column           | Description       |
| ---------------- | ----------------- |
| transaction_key  | Surrogate Key     |
| transaction_id   | Business Key      |
| customer_key     | FK DIM_CUSTOMER   |
| product_key      | FK DIM_PRODUCT    |
| branch_key       | FK DIM_BRANCH     |
| rm_key           | FK DIM_RM         |
| transaction_date | Ngày giao dịch    |
| transaction_type | Loại giao dịch    |
| channel          | Kênh giao dịch    |
| amount_vnd       | Giá trị giao dịch |

Primary Key:

```
transaction_key
```

Trong đó:

* `transaction_key`: khóa thay thế trong Data Mart
* `transaction_id`: mã giao dịch từ hệ thống nguồn để trace dữ liệu

---

## 7.2 DIM_PRODUCT

Lưu thông tin sản phẩm ngân hàng.

Ví dụ:

| product_key | product_id | product_category |
| ----------- | ---------- | ---------------- |
| 1           | 101        | Tiết kiệm        |
| 3           | 103        | Vay              |

---

## 7.3 DIM_BRANCH

Lưu thông tin chi nhánh.

| branch_key | branch_id | branch_name  |
| ---------- | --------- | ------------ |
| 1          | 1         | CN Hoàn Kiếm |

---

## 7.4 DIM_RM

Lưu thông tin Relationship Manager.

| rm_key | rm_id | rm_name      |
| ------ | ----- | ------------ |
| 1      | 10    | Nguyễn Văn A |

---

# 8. DIM_CUSTOMER - SCD Type 2

## 8.1 Vấn đề

Thông tin khách hàng có thể thay đổi theo thời gian:

Ví dụ:

* Khách hàng chuyển chi nhánh
* Thay đổi RM phụ trách
* Thay đổi segment

Không update đè dữ liệu cũ.

Thay vào đó lưu lại lịch sử.

---

## 8.2 Thiết kế bảng

| Column         | Ý nghĩa               |
| -------------- | --------------------- |
| customer_key   | Surrogate Key         |
| customer_id    | Business Key          |
| customer_name  | Tên khách hàng        |
| dob            | Ngày sinh             |
| phone          | Số điện thoại         |
| segment        | Phân khúc             |
| branch_id      | Chi nhánh             |
| rm_id          | RM                    |
| effective_from | Ngày bắt đầu hiệu lực |
| effective_to   | Ngày kết thúc         |
| is_current     | Record hiện tại       |

---

# 9. Quy trình ETL

# Step 1: Data Exploration

Kiểm tra dữ liệu nguồn:

* Schema
* Data type
* Missing value
* Duplicate
* Data anomaly

Command:

```bash
python src/explore.py
```

---

# Step 2: STAGING Layer

STAGING thực hiện:

* Chuẩn hóa dữ liệu
* Kiểm tra dữ liệu đầu vào
* Loại bỏ dữ liệu lỗi
* Chuẩn bị dữ liệu cho Dimension và Fact

Các bảng:

```
STG_CUSTOMER

STG_PRODUCT

STG_BRANCH

STG_RM

STG_TRANSACTION

```

---

# 10. Xử lý dữ liệu lỗi Transaction

Trong dữ liệu nguồn phát hiện các giao dịch:

```
transaction_date IS NULL
```

Các record này không được đưa vào Data Mart.

Được tách sang bảng:

```
REJECT_TRANSACTION
```

Ví dụ:

| transaction_id | reject_reason            |
| -------------- | ------------------------ |
| 5065           | Missing transaction_date |

Các transaction hợp lệ:

```
STG_TRANSACTION
```

---

# 11. Xây dựng Dimension

Pipeline:

```
STG_PRODUCT

       |

       v

DIM_PRODUCT


```

Tương tự:

```
STG_BRANCH  -> DIM_BRANCH

STG_RM      -> DIM_RM

STG_CUSTOMER -> DIM_CUSTOMER

```

---

# 12. Xử lý SCD Type 2 - DIM_CUSTOMER

## 12.1 Logic xử lý

Khi customer mới:

```
Insert record mới
```

Khi customer không thay đổi:

```
Giữ nguyên dữ liệu
```

Khi customer thay đổi:

```
1. Close record cũ

2. Insert record mới

```

---

## 12.2 Ví dụ

Trước khi thay đổi:

| customer_id | branch | segment |
| ----------- | ------ | ------- |
| 22          | 1      | Mass    |

Khách hàng chuyển sang chi nhánh khác:

| customer_id | branch | segment  |
| ----------- | ------ | -------- |
| 22          | 5      | Priority |

---

## Bước 1: Đóng bản ghi cũ

```sql
UPDATE DIM_CUSTOMER

SET

effective_to = '2025-07-17',

is_current = FALSE

WHERE customer_id = 22;

```

Kết quả:

| customer_id | branch | effective_to | current |
| ----------- | ------ | ------------ | ------- |
| 22          | 1      | 2025-07-17   | False   |

---

## Bước 2: Insert bản ghi mới

```sql
INSERT INTO DIM_CUSTOMER
(
customer_id,
branch_id,
segment,
effective_from,
effective_to,
is_current
)

VALUES
(
22,
5,
'Priority',
'2025-07-18',
'9999-12-31',
TRUE
);

```

Kết quả:

| customer_id | branch | effective_from | effective_to | current |
| ----------- | ------ | -------------- | ------------ | ------- |
| 22          | 1      | 2024-01-01     | 2025-07-17   | False   |
| 22          | 5      | 2025-07-18     | 9999-12-31   | True    |

---

# 13. Build FACT_TRANSACTION

FACT được tạo bằng cách join:

```
STG_TRANSACTION


        +

DIM_CUSTOMER

DIM_PRODUCT

DIM_BRANCH

DIM_RM


        |

        v


FACT_TRANSACTION

```

---

## Join DIM_CUSTOMER theo thời gian

Không join đơn giản:

```sql
customer_id = customer_id
```

Vì một customer có nhiều version.

Sử dụng:

```sql
ON t.customer_id = c.customer_id

AND t.transaction_date

BETWEEN

c.effective_from

AND

c.effective_to

```

Ví dụ:

Customer history:

| effective_from | effective_to | branch |
| -------------- | ------------ | ------ |
| 2024-01-01     | 2025-07-17   | CN1    |
| 2025-07-18     | 9999-12-31   | CN5    |

Transaction:

| transaction_date | branch |
| ---------------- | ------ |
| 2025-07-02       | CN1    |
| 2025-07-31       | CN5    |

---

# 14. Data Quality Validation

Framework sử dụng:

```
Great Expectations
```

Các rule:

## 1. Transaction date không NULL

Expectation:

```
expect_column_values_to_not_be_null
```

---

## 2. Transaction ID không duplicate

```
expect_column_values_to_be_unique
```

---

## 3. Amount hợp lệ

Rule:

```
amount_vnd >= 0
```

---

## 4. Foreign Key Customer

```
customer_key IS NOT NULL
```

---

## 5. Foreign Key Product

```
product_key IS NOT NULL
```

---

# 15. Export Data Mart Output

Sau khi hoàn thành ETL và Data Quality:

Dữ liệu được export ra:

```
data/output

│
├── dim_customer.csv

├── dim_product.csv

├── dim_branch.csv

├── dim_rm.csv

└── fact_transaction.csv

```

Các file này có thể sử dụng cho:

* Power BI
* Tableau
* Reporting System
* Analytics

---

# 16. Project Structure

```
retail-bank-etl

│

├── data

│   ├── raw

│   └── output


├── sql


├── src

│   ├── database.py

│   ├── explore.py

│   ├── build_staging.py

│   ├── build_dimension.py

│   ├── build_fact.py

│   ├── run_gx_validation.py


├── gx


├── retail_bank.duckdb


├── requirements.txt


└── README.md

```

---

# 17. Cách chạy Project

## Install dependencies

```bash
pip install -r requirements.txt

```

---

## Build Staging

```bash
python src/build_staging.py

```

---

## Build Dimension

```bash
python src/build_dimension.py

```

---

## Build Fact

```bash
python src/build_fact.py

```

---

## Data Quality Check

```bash
python src/run_gx_validation.py

```

Output:

```
PASS - transaction_date not null

PASS - transaction_id unique

PASS - amount valid


```

---

# 18. Kết quả đạt được

Project hoàn thành:

✅ Xây dựng Data Mart theo Star Schema
✅ Hoàn thiện ETL Pipeline bằng Python + SQL
✅ Data Cleaning và Reject Handling
✅ Xử lý lịch sử khách hàng bằng SCD Type 2
✅ Mapping Fact - Dimension theo thời gian
✅ Data Quality Framework bằng Great Expectations
✅ Export dữ liệu phục vụ báo cáo BI
