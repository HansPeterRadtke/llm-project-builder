LLM Project Builder

Generates full project scaffolding and code from a prompt — powered by LLMs.

LLM Project Builder creates complete Python projects from high-level descriptions, generating modules, folder structures, and even configurations.

---

🛠️ Installation

    pip install llm-project-builder

---

🚀 Example usage

    from llm_project_builder import generate_project

    project_description = """
    A REST API using FastAPI and SQLite for managing tasks.
    """

    generate_project(prompt=project_description)

---

🧪 Testing

Run included tests to validate functionality:

    python3 -m llm_project_builder.tests

---

🗂️ Project structure

- llm_project_builder/ — main package
  - core.py — main logic (placeholder)
  - __main__.py — CLI entry point (placeholder)
  - tests/ — test suite

---

More coming soon. Contribute or report issues at: https://github.com/HansPeterRadtke/llm-project-builder