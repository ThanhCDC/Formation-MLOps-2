import ast
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"


def test_to_csv_called_with_index_false():
    for path in PACKAGE_ROOT.rglob("*.py"):
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "to_csv":
                kwargs = {kw.arg: kw.value for kw in node.keywords}
                index = kwargs.get("index")
                assert isinstance(index, ast.Constant) and index.value is False, f"{path}:{node.lineno}"
