"""Notes From a Passive-Aggressive Fridge -- writes the entry line
(68 chars, one line) to /output/entry.txt. Pure stdlib; deterministic
from any working directory."""

import os

LINE = "I kept your leftovers cold for nine days. You thanked the microwave."

# Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, one line,
# not only whitespace. Fail loudly instead of writing an invalid entry.
if not (1 <= len(LINE) <= 200) or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-200 char single-line gate")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
