print("TEST_SCRIPT_START")
import os

def test_make_code():
  print("[DEBUG] test_make_code started")

  # Enable test mode
  os.environ["LLM_TEST_MODE"] = "true"

  from hanspeterradtke.llm_project_builder import make_code

  prompt  = "Write a Python program that prints Hello Test"
  result  = make_code(prompt)

  assert result is not None, "make_code() returned None"
  assert result.get("status") == "ok", "make_code() did not return status=ok"
  code_blocks = result.get("code", [])
  assert isinstance(code_blocks, list), "code_blocks is not a list"
  assert len(code_blocks) > 0, "no code blocks extracted"
  assert "print(\"Hello" in code_blocks[0], "expected print statement missing"

  print("[DEBUG] test_make_code passed, result:", result)

  # Clean up
  del os.environ["LLM_TEST_MODE"]
  print("[DEBUG] test_make_code finished")