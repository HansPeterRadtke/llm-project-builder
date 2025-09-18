from hanspeterradtke.utils.parser import extract_python


def make_code(prompt: str, options: dict):
  print("[DEBUG] make_code started")
  try:
    print("[DEBUG] calling extract_python with fixed code")
    result = extract_python("""
```python
def foo():
  return 42
```
""")
    print("[DEBUG] extract_python returned:", result)
    return result
  except Exception as e:
    print("[ERROR] exception in make_code:", repr(e))
    raise


if __name__ == "__main__":
  print("[DEBUG] __main__ entrypoint started")
  try:
    output = make_code("test prompt", {})
    print("[DEBUG] make_code output:", output)
  except Exception as e:
    print("[ERROR] exception in __main__:", repr(e))