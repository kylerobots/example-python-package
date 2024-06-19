# Example Python Package #

A collection of modern (mostly) best practices implemented in a simple package template. This is designed to allow easy
reference for future projects.

The library itself is just a simple math library with addition, subtraction, multiplication, and division. But it comes
with a number of features.

## Table of Contents ##

1. [Included Features](#included-features)
    - [Poetry](#poetry)
    - [Pyenv Python Versions](#pyenv-python-versions)
    - [Release Drafts](#release-drafts)
2. [Acknowledgements](#acknowledgements)

## Included Features ##

These are the included features. This README is not an exhaustive list of all features. It merely points out which are
in use with some light explanation and often a link to the relevant documentation. Please refer to that documentation
for implementation details.

### Poetry ###

This package uses [Poetry](https://python-poetry.org/) to do all the package management, including dependencies and
installation. The `pyproject.toml` file contains the necessary information. The environment can be set up locally with
`poetry install` and run with `poetry run <command>`.

### Pyenv Python Versions ###

There is a `.python-version` file that specifies which versions of Python [pyenv](https://github.com/pyenv/pyenv) can
support. Just install `pyenv` per instructions, install the recommended build dependencies, then the desired Python
versions. This will allow you to have multiple different Python versions at once.

### Release Drafts ###

There is a GitHub workflow that automatically drafts release notes based on pull requests. It uses an Action called
[release-drafter](https://github.com/release-drafter/release-drafter). This action is configured to group info based on
tag type (e.g. `build`, `documentation`, etc.) and can automatically determine the next version use the same tags.

## Acknowledgements ##

This guide was partly inspired by
[Claudio Jolowicz's series of blog posts](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
