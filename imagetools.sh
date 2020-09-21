#!/bin/bash

export PIPENV_IGNORE_VIRTUALENVS=1
python_interpreter=$(pipenv --py)
"$python_interpreter" imagetools.py "$@"