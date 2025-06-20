import os
import re
import sys
from pathlib import Path

def make_code():
  print("[DEBUG] Starting full process", flush=True)

  SCRIPT_DIR      = Path(__file__).resolve().parent
  BASE_DIR        = SCRIPT_DIR.parent.parent
  OPEN_ROUTER_DIR = BASE_DIR / 'utils' / 'open_router'
  GEN_DIR         = BASE_DIR / 'generated'
  PROMPT_FILE     = SCRIPT_DIR / 'prompt.txt'
  ERROR_TAG       = '<ERROR_FILES>'
  FILE_TAG        = '<FILE_LIST>'

  print("[DEBUG] Starting make_prompt()", flush=True)
  try:
    instruction = PROMPT_FILE.read_text()
  except Exception as e:
    print(f"[ERROR] Cannot read {PROMPT_FILE.name}: {e}", flush=True)
    sys.exit(1)

  file_paths  = []
  error_paths = []

  if FILE_TAG in instruction:
    match = re.search(f"{FILE_TAG}(.*?){FILE_TAG}", instruction, re.DOTALL)
    if match:
      file_paths  = match.group(1).strip().splitlines()
      instruction = instruction.replace(match.group(0), '')

  if ERROR_TAG in instruction:
    match = re.search(f"{ERROR_TAG}(.*?){ERROR_TAG}", instruction, re.DOTALL)
    if match:
      error_paths = match.group(1).strip().splitlines()
      instruction = instruction.replace(match.group(0), '')

  prompt = instruction.strip()

  for file in file_paths:
    path = Path(file)
    if not path.exists():
      print(f"[ERROR] File not found: {file}", flush=True)
      sys.exit(1)
    prompt += f"\nStartFile: {file}\n<python>\n{path.read_text()}\n</python>\nEndFile"

  if error_paths:
    prompt += "\nThose errors occurred:\n"
    for file in error_paths:
      path = Path(file)
      if not path.exists():
        print(f"[ERROR] Error file not found: {file}", flush=True)
        sys.exit(1)
      prompt += f"\n{path.read_text()}"

  try:
    (OPEN_ROUTER_DIR / 'prompt.txt').write_text(prompt)
  except Exception as e:
    print(f"[ERROR] Cannot write prompt.txt in open_router: {e}", flush=True)
    sys.exit(1)

  print("[DEBUG] Prompt written to OpenRouter", flush=True)
  os.system(f"python3 {OPEN_ROUTER_DIR}/__main__.py")

if __name__ == '__main__':
  make_code()