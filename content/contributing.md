---
title: "Contributing to This Site"
date: "2024-11-30"
---

## Contributions

This site is for showcasing *original* work done in CAPP or CAPP-adjacent courses.

<em>In general, you may only post work that it is acceptable to post publicly on GitHub (i.e. original projects, not assigned coursework where everyone solves the same problem). Check with the instructor of the course if you are in doubt.</em>

You can contribute by submitting a pull request to this repository on GitHub.

{{<github repo="uchicago-mscapp-projects/uchicago-mscapp-projects.github.io" >}}

## How to Contribute

1) [Create a fork](https://github.com/uchicago-mscapp-projects/uchicago-mscapp-projects.github.io/fork) of the repository on GitHub.
2) Check out your fork, and make any edits.
    - See [modifying content](#modifying-content) below to determine which files to change, you will be editing Markdown and some [TOML](https://toml.io/en/), which you'll find quite easy!
    - Optionally, see [running locally](#running-locally) to verify your changes.
3) [Submit a pull request](https://github.com/uchicago-mscapp-projects/uchicago-mscapp-projects.github.io/pulls) with your changes.
4) Once your PR is merged, your changes will be live!

## Modifying Content

Most of the time, editing or adding a page will involve creating a `.md` file in the appropriate place.

These files consist of TOML metadata (the top section between `---` markers) and Markdown.

The markdown beneath the TOML will appear on the page in question rendered as HTML.

To include a GitHub repo link like the one on this page, use this special syntax

```html
{{</* github repo="username/reponame" */>}}
```

### Project Page

To edit the page `/projects/SLUG/`, modify the file `content/projects/SLUG`:

**TOML Metadata:**

- `title`: display title of project
- `authors`: list of authors, should correspond to /authors/USERNAME/
- `courses`: list of course IDs, should correspond to /courses/CODE/
- `date`: used for sorting
- `tags`: arbitrary metadata

### Project Image

A file named `feature.png` or `feature.jpg` will be used as the "cover image."  Modify this as desired.

Note: A helper script in `helpers/mosaic.py` generates the mosaic image on the front page.

### Author Page

To edit the page `/authors/USERNAME/`, modify the file `content/authors/USERNAME/_index.md`:

**TOML Metadata:**

- `title`: display name in author listings

### Additional Author Metadata

There is additional author metadata which appears on project pages.

To modify it edit the file `data/authors/USERNAME.json`:

- `name`: Will appear on article pages.
- `linkedin`: LinkedIn URL. Remove entry from `social` to exclude
- `github`: GitHub URL. Remove entry from `social` to exclude

### Course Info

To edit the page `/courses/CODE`, modify the file `content/courses/CODE/_index.md`:

- `title`: Course Name

## Running locally

1. You will need to download and install Hugo, the static site generator tool used to build this site. See <https://gohugo.io/installation/>
2. Check out your fork of the repository using Git.
3. Within the `uchicago-mscapp-projects.github.io` directory, run `git submodule update --init --recursive` to initialize the theme.
4. `hugo serve` will start a server that will load the site on <http://localhost:1313>.
