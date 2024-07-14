# The starting place for your projects that require torch and acceleration

based on this repo https://github.com/lucaspar/poetry-torch

# If you want to do a new think with torch

- copy these files
- rename  `name         = "YOUR_NAME_HERE"` in pyproject.toml
- git init your new repo

- run
$ poetry install && poetry run python check-cuda.py

to make sure it all its all good
