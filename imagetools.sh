#!/bin/bash
export PIPENV_IGNORE_VIRTUALENVS=1

IMAGETOOLS_PATH=$(greadlink -f "$0")
IMAGETOOLS_DIR=$(dirname "$IMAGETOOLS_PATH")

cd "$IMAGETOOLS_DIR" || exit 1

PYTHON_INTERPRETER=$(pipenv --py)
"$PYTHON_INTERPRETER" imagetools.py "$@"
