"""Fridge Roast entry: one line roasting a smart fridge.

Writes the roast to entry.txt in the output directory so the
sealed gate (UTF-8, 1-200 characters) can read it.
"""

import os
from pathlib import Path

ROAST = (
    "My smart fridge installed a firmware update overnight "
    "and now the ice maker wants a subscription."
)


def output_dir() -> Path:
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path("/output")


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, len(text)
    (target_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
