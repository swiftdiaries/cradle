# `cradle`

![Lint](https://github.com/swiftdiaries/cradle/workflows/Lint/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

cradle is a tool to test ML models.

**Installation**:

```console
$ pip install cradle-app
```

## `cradle-app`

cradle is tool to test ML models in production.

**Usage**:

```console
$ cradle-app [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `init`: init cradle app
* `launch`: Launch gradio instance

## `cradle-app init`

init cradle app

**Usage**:

```console
$ cradle-app init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `cradle-app launch`

Launch gradio instance

**Usage**:

```console
$ cradle-app launch [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
