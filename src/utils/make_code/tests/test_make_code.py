import os
import sys
from pathlib import Path

# Ensure src is in Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'src'))

from utils.make_code.__main__ import make_code

def test_make_code(monkeypatch):
  monkeypatch.setenv("LLM_TEST_MODE", "true")

  base = Path(__file__).resolve().parents[4]
  makecode_dir = base / 'src' / 'utils' / 'make_code'
  openrouter_dir = base / 'src' / 'utils' / 'open_router'

  prompt_path = makecode_dir / 'prompt.txt'
  output_path = openrouter_dir / 'output.txt'

  prompt_path.write_text("Write a Hello World script in Python.")
  if output_path.exists():
    output_path.unlink()

  make_code()

  assert output_path.exists(), "Output file not created"
  content = output_path.read_text()
  assert "Hello world" in content or "print(" in content, "Expected content not found"
  print("[DEBUG] Test MakeCode test-mode response passed successfully!")