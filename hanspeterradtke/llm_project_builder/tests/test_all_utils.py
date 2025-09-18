import sys
from pathlib import Path

# Ensure imports work from project root (llm_project_builder)
root = Path(__file__).resolve().parents[1]  # project root
src = root / "src"

sys.path.insert(0, str(src))  # gives access to make_code and utils

from utils.open_router.tests.test_open_router import (
  test_open_router_invalid_key,
  test_open_router_valid_placeholder,
)
from utils.parser.tests.test_parser import (
  test_extract_python_single_block,
  test_extract_python_multiple_blocks,
  test_extract_python_no_block,
  test_extract_python_malformed,
)
from make_code.test.test_make_code import test_make_code

def test_utils_open_router():
  test_open_router_invalid_key()
  test_open_router_valid_placeholder()

def test_utils_make_code():
  test_make_code()

def test_utils_parser():
  test_extract_python_single_block()
  test_extract_python_multiple_blocks()
  test_extract_python_no_block()
  test_extract_python_malformed()

if __name__ == "__main__":
  print("[DEBUG] Running integration tests...")
  test_utils_open_router()
  test_utils_make_code()
  test_utils_parser()
  print("[DEBUG] All utils tests executed successfully.")