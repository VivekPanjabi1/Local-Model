"""Entrypoint for the Local LLM Lab experiments."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    print("Local LLM Lab ready! 🧪")
    print(f"Project root: {project_root}")
    print("Next steps: configure requirements.txt, add training scripts, run experiments.")


if __name__ == "__main__":
    main()
