#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
from utils.parser import extract_python

SCRIPT_DIR     = Path(__file__).resolve().parent
UTILS_DIR      = SCRIPT_DIR.parent / "utils"
OPEN_ROUTER    = UTILS_DIR / "open_router" / "__main__.py"
PARSER_OUTPUT  = UTILS_DIR / "open_router" / "output.txt"
PROMPT_FILE    = UTILS_DIR / "open_router" / "prompt.txt"


def write_prompt(prompt: str):
  print("[DEBUG] write_prompt started")
  try:
    PROMPT_FILE.write_text(prompt, encoding="utf-8")
    print(f"[DEBUG] Prompt written to {PROMPT_FILE}")
  except Exception as e:
    print(f"[ERROR] Failed to write prompt: {e}")
    raise
  print("[DEBUG] write_prompt finished")


def run_open_router():
  print("[DEBUG] run_open_router started")
  try:
    subprocess.run([sys.executable, str(OPEN_ROUTER)], check=True)
    print("[DEBUG] OpenRouter run completed")
  except subprocess.CalledProcessError as e:
    print(f"[ERROR] OpenRouter process failed: {e}")
    raise
  except Exception as e:
    print(f"[ERROR] Unexpected error running OpenRouter: {e}")
    raise
  print("[DEBUG] run_open_router finished")


def parse_output():
  print("[DEBUG] parse_output started")
  try:
    if not PARSER_OUTPUT.exists():
      raise FileNotFoundError(f"Missing output file: {PARSER_OUTPUT}")
    content = PARSER_OUTPUT.read_text(encoding="utf-8")
    blocks  = extract_python(content)
    print(f"[DEBUG] Extracted {len(blocks)} Python code blocks")
    return blocks
  except Exception as e:
    print(f"[ERROR] Failed to parse output: {e}")
    return []
  finally:
    print("[DEBUG] parse_output finished")


def make_code(prompt: str):
  print("[DEBUG] make_code started")
  try:
    write_prompt(prompt)
    run_open_router()
    code_blocks = parse_output()
    result      = {"status": "ok", "code": code_blocks}
    print(f"[DEBUG] make_code result: {result}")
    return result
  except Exception as e:
    print(f"[ERROR] make_code failed: {e}")
    return {"status": "error", "error": str(e)}
  finally:
    print("[DEBUG] make_code finished")


if __name__ == "__main__":
  demo_prompt = "Write a Python program that prints Hello World"
  make_code(demo_prompt)