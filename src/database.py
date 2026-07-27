from pathlib import Path
import duckdb

# Đường dẫn tới thư mục gốc của project
ROOT_DIR = Path(__file__).resolve().parent.parent

# File database DuckDB
DB_PATH = ROOT_DIR / "retail_bank.duckdb"

# Thư mục chứa file CSV
RAW_DATA_PATH = ROOT_DIR / "data" / "raw"

# Thư mục export kết quả
OUTPUT_PATH = ROOT_DIR / "data" / "output"


def get_connection():
    """
    Tạo và trả về kết nối tới DuckDB.
    Nếu retail_bank.duckdb chưa tồn tại thì DuckDB sẽ tự tạo.
    """
    return duckdb.connect(str(DB_PATH))