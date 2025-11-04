from pathlib import Path

years = sorted([y for y in Path("src").iterdir() if y.is_dir()], reverse=True)

with open("docs/index.md", "w", encoding="utf-8") as f:
    items = "\n".join([f"- [{y.stem}]({y.stem}.md)" for y in years])
    text = f"""
# Advent of Code

Solutions to [Advent of Code](https://adventofcode.com/)

{items}
"""
    f.write(text.strip())

for y in years:
    days = {}
    for d in list(y.glob("*.py")):
        name = d.stem.split("_")[0]
        if name not in days:
            days[name] = [d]
        else:
            days[name].append(d)

    text = f"""
# Advent of Code {y.stem}

"""
    for d in sorted(days):
        parts = [
            f"""
    === "{p.stem.split('_')[-1].capitalize().replace("Part","Part ")}"

        ```py linenums="1"
        --8<-- "{str(p.as_posix())}"
        ```
"""
            for p in sorted(days[d])
        ]

        text += f"""
??? success "{d.capitalize().replace("Day","Day ")}"
{''.join(parts)}
""".lstrip()

    with open(f"docs/{y.stem}.md", "w", encoding="utf-8") as f:
        f.write(text.strip())
