---
title: "Contributing to this Site"
date: "2024-11-30"
---

You are welcome to list any work done in a CAPP course by submitting a pull request to this repository on GitHub.

## Steps

1) Create a fork of the repository on GitHub.
2) Check out your fork, and make any edits.
2b) Optionally, run the project locally to verify your changes.
3) Submit a pull request with your changes.
4) Once your PR is merged, your changes will be live.

## Content

Most of the time, editing or adding a page will involve creating a `.md` file in the appropriate place.

These files consist of TOML metadata (the top section between `---` markers) and Markdown.

### Project Page

To edit the page `/projects/SLUG/`, modify the file `content/projects/SLUG`:

**Metadata:**
- title: display title of project
- authors: list of authors, should correspond to /authors/USERNAME/
- courses: list of course IDs, should correspond to /courses/CODE/
- date: used for sorting
- tags: arbitrary metadata

**Markdown**:

Feel free to include a short description of the project.

To include a GitHub Repo:

```html
{\{< github repo="username/reponame" >}}
```

### Author Page

To edit the page `/authors/USERNAME/`, modify the file `content/authors/USERNAME/_index.md`:

- 'title': display name in author listings
- Markdown beneath the header will be rendered on your author page.

### Author Metadata

Metadata which appears on project pages.

Modify the file `data/authors/USERNAME.json`:

- name: Will appear on article pages.
- linkedin: LinkedIn URL, remove entry from social to exclude
- github: GitHub URL, remove entry from social to exclude

### Course Info

To edit the page `/courses/CODE`, modify the file `content/courses/CODE/_index.md`:

- title: Course Name
