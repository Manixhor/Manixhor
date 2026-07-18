#!/usr/bin/env python3
import json
import os
import re


HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, ".."))
README_PATH = os.path.join(ROOT, "README.md")
DATA_PATH = os.path.join(ROOT, "data", "contributions.json")


with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

cache_key = re.sub(r"[^0-9A-Za-z]", "", data["generated_at"])

with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

updated = re.sub(
    r'(\./contrib-heatmap\.svg)(?:\?v=[0-9A-Za-z_.-]+)?',
    rf"\1?v={cache_key}",
    readme,
)

if updated != readme:
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

print(f"heatmap cache key: {cache_key}")
