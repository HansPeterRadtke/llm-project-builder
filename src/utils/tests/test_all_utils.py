import sys
from pathlib import Path

# Add src/utils to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from open_router.tests.test_open_router import test_open_router_fake_output
from make_code.tests.test_make_code import test_make_code
from parser.tests.test_parser import (
  test_extract_python_single_block,
  test_extract_python_multiple_blocks,
  test_extract_python_no_block,
  test_extract_python_malformed,
)

def test_utils_open_router(monkeypatch):
  test_open_router_fake_output(monkeypatch)

def test_utils_make_code(monkeypatch):
  test_make_code(monkeypatch)

def test_utils_parser():
  test_extract_python_single_block()
  test_extract_python_multiple_blocks()
  test_extract_python_no_block()
  test_extract_python_malformed()

print("[DEBUG] All utils tests executed from integration test.")