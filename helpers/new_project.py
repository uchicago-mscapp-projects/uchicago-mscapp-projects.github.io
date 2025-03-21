import tomllib
import pathlib
from new_person import new_person


def new_project(slug, name, members, date, course, repo, youtube):
    template = f"""---
date: "{date}"
tags: []
title: "{name}"
authors: {repr(members)}
courses: ["{course}"]
---

{{{{< github repo="{repo}" >}}}}

{{{{< youtube {youtube} >}}}}

"""

    pathlib.Path(f"content/projects/{slug}").mkdir(exist_ok=True, parents=True)
    with open(f"content/projects/{slug}/index.md", "w") as f:
        f.write(template)


def load_projects_and_create():
    """
    Load projects from a TOML file and create each one.
    """
    try:
        project_data = tomllib.load(open("projects.toml", "rb"))
    except Exception as e:
        print(f"Error loading TOML file: {e}")
        return

    # Extract projects list from the TOML data
    projects = project_data.get("projects", [])
    if not projects:
        print("No projects found in the TOML file.")
        return

    # Process each project
    for project in projects:
        # Extract required fields with default values where appropriate
        slug = project.get("slug", "")
        name = project.get("name", "")
        members = project.get("members", [])
        date = project.get("date")
        course = project.get("course", "")
        repo = project.get("repo", "")
        youtube = project.get("youtube", "")

        # Call the new_project function
        new_project(slug, name, members, date, course, repo, youtube)
        for member in members:
            mslug = member.lower().replace(" ", "-")
            new_person(mslug, member)


if __name__ == "__main__":
    load_projects_and_create()
