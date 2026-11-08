"""Checks the language files: same keys as en_us.json and the same %s / %1$s / %% placeholders in every text."""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN = re.compile(r"%(?:\d+\$)?[sd%]")


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


source = load("en_us.json")
errors = []
for name in sorted(os.listdir(HERE)):
    if not name.endswith(".json") or name == "en_us.json":
        continue
    if name == "reading_overrides.json":
        # Japanese reading corrections: word -> reading, only has to be valid JSON with text values
        try:
            for key, value in load(name).items():
                if not isinstance(value, str):
                    errors.append(f"{name}: the reading of {key} must be text")
        except ValueError as e:
            errors.append(f"{name}: not valid JSON ({e})")
        continue
    try:
        data = load(name)
    except ValueError as e:
        errors.append(f"{name}: not valid JSON ({e})")
        continue
    for key in source:
        if key not in data:
            errors.append(f"{name}: missing key {key}")
    for key in data:
        if key not in source:
            errors.append(f"{name}: unknown key {key}")
    for key, text in data.items():
        if key in source and isinstance(text, str):
            if collections.Counter(TOKEN.findall(text)) != collections.Counter(TOKEN.findall(source[key])):
                errors.append(f"{name}: placeholders of {key} differ from en_us.json (keep %s, %1$s, %% exactly as in the English text)")
for e in errors:
    print(e)
print("OK" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
