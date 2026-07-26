"""Scan kid answers for # OUTPUT blocks missing print()."""

from __future__ import annotations

import re

from python_review_kid_answers import KID_ANSWERS

STEP_PRE = re.compile(r'<div class="step-pre">(.*?)</div>', re.S)

bad: list[str] = []
for qid, html in KID_ANSWERS.items():
    for block in STEP_PRE.findall(html):
        if "# OUTPUT" in block and "print(" not in block:
            bad.append(qid)

print("bad:", sorted(set(bad)) or "none")
print("Q1.8 has print(by_blood_type):", "print(by_blood_type" in KID_ANSWERS["Q1.8"])
print("Q1.8 has db.by_blood_type:", "db.by_blood_type" in KID_ANSWERS["Q1.8"])
