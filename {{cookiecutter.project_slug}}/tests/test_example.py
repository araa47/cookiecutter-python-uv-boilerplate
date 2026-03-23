import importlib
import sys
from pathlib import Path


def test_main(capsys):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    app = importlib.import_module("app")
    app.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
