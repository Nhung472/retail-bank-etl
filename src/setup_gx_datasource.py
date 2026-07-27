import great_expectations as gx
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

context = gx.get_context(
    mode="file",
    project_root_dir=str(ROOT_DIR / "gx")
)


# Tạo datasource
datasource = context.data_sources.add_pandas(
    name="pandas_datasource"
)


print("Datasource created:")
print(datasource.name)