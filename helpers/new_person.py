#!/usr/bin/env python3
import os
import sys
import json

name = sys.argv[1]

dir_path = f"content/authors/{name}"
file_path = f"{dir_path}/_index.md"

os.makedirs(dir_path, exist_ok=True)

title = " ".join(word.capitalize() for word in name.split("-"))

content = f"""---
title: "{title}"
---
"""

with open(file_path, "w") as f:
    f.write(content)


# make json
json_path = f"data/authors/{name}.json"

with open(json_path, "w") as f:
    json.dump(
        {
            "name": title,
            "bio": "",
            "social": [
                # {"linkedin": "https://linkedin.com/in/"},
                # {"github": "https://github.com/"},
            ],
        },
        f,
    )
