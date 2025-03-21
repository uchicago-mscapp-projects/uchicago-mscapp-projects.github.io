#!/usr/bin/env python3
import os
import sys
import json


def new_person(slug, name=None):
    dir_path = f"content/authors/{slug}"
    file_path = f"{dir_path}/_index.md"

    os.makedirs(dir_path, exist_ok=True)

    if not name:
        name = " ".join(word.capitalize() for word in name.split("-"))

    content = f"""---
title: "{name}"
---
"""

    with open(file_path, "w") as f:
        f.write(content)

    # make json
    json_path = f"data/authors/{slug}.json"

    with open(json_path, "w") as f:
        json.dump(
            {
                "name": name,
                "bio": "",
                "social": [
                    # {"linkedin": "https://linkedin.com/in/"},
                    # {"github": "https://github.com/"},
                ],
            },
            f,
        )


if __name__ == "__main__":
    name = sys.argv[1]
    new_person(name)
