import great_expectations as gx
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

GX_DIR = ROOT_DIR / "gx"


context = gx.get_context(
    mode="file",
    project_root_dir=str(GX_DIR)
)


print("GX initialized")
print(context)