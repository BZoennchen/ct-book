# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

An interactive German-language textbook titled *Computational Thinking*, built with [Jupyter Book](https://jupyterbook.org). It is published to GitHub Pages at `https://BZoennchen.github.io/ct-book`. The book is authored by Benedikt Zönnchen at Hochschule München and licensed CC BY-SA 4.0.

## Build & deploy commands

```sh
# Build the book (output goes to _build/html/)
jupyter-book build .

# Clean build (force full rebuild)
rm -R _build && jupyter-book build .

# Deploy to GitHub Pages only
ghp-import -n -p -f _build/html

# Full pipeline: clean build → commit → push → deploy
./build.sh
```

> `build.sh` also runs `git add ./* && git commit && git push origin master` — do not run it unless intending to commit and publish.

## Environment setup

Use the conda environment or pip:

```sh
# Conda
conda env create -f environment.yaml
conda activate ct-book

# pip (alternative)
pip install -r doc-requirements.txt
```

Key packages: `jupyter-book`, `sphinx-exercise`, `sphinx-inline-tabs`, `roboworld`, `jupyterquiz`, `ghp-import`, `docutils==0.17.1`, `mdit-py-plugins~=0.3.1`.

## Content format (MyST Markdown)

All content lives in `chapters/` as `.md` files using **MyST Markdown** with jupytext frontmatter. Every content file starts with:

```yaml
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```

Common MyST constructs used throughout:

- **Code cells**: `` ```{code-cell} python3 ``
- **Admonitions**: `` ```{admonition} Title `` with `:class: remark`, `:class: exercise`, etc.
- **Cross-references**: label a section with `(sec-my-label)=` above a heading, then reference with `[text](sec-my-label)` or `{ref}`
- **Citations**: `{cite}` role referencing `references.bib`
- **Math**: inline `$...$` and block `$$...$$` (dollarmath extension), also `:::` colon fences
- **Exercises**: via `sphinx-exercise` (`` ```{exercise} ``, `` ```{solution} ``)
- **Tabs**: via `sphinx-inline-tabs`

Notebook execution is set to `auto` in `_config.yml` with a 200-second timeout.

## Book structure

```
_config.yml       # Jupyter Book configuration (language: de, extensions, launch buttons)
_toc.yml          # Table of contents — source of truth for chapter order
intro.md          # Book landing page
references.bib    # BibTeX bibliography
_static/          # Custom CSS
figs/             # Figures and images
chapters/
  01-x/           # Einleitung (Introduction)
  02-x/           # Theorie (Theory: math, information, languages, programming)
  03-x/           # Python (environment, types, functions, OOP, CPython internals)
  04/             # CT in Aktion (applied projects: roboworld, images, memory, etc.)
  misc/           # Appendix (bibliography page)
```

Chapter numbering in `_toc.yml` is separate from directory names. Sections within a chapter are individual files listed under `sections:` in the TOC.

## Key configuration details

- Language is **German** throughout (`sphinx: language: de`)
- `only_build_toc_files: true` — files not listed in `_toc.yml` are excluded from the build
- `exclude_patterns` in `_config.yml` controls what Jupyter Book ignores
- Heading anchors are auto-generated up to depth 3 (`myst_heading_anchors: 3`)
- JupyterHub launch button points to `https://datahub.cs.hm.edu/`
