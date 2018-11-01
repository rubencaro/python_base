# Python base project

This project aims to be a base for quickly starting a new Python application. It just contains the basic dependencies and tools for you to build on top of.

## Setup

Following [this](https://gist.github.com/rubencaro/888fb8e4f0811e79fa22b5ac39610c9e).

So you should clone it, then `cd` into its folder, run `asdf install` to get the right Python version. Then `python -m venv env` to create a new environment and `source env/bin/activate` to activate it. Then run `pip install -r requirements.txt` to install all dependencies.

## Development

Just run `./watch.sh` to run tests and coverage analysis while you make changes to the code.

### Testing

Testing is done using [pytest](https://docs.pytest.org/en/latest/index.html). You can see any params passed to it in the `watch.sh` script.

Tests lay inside the `test` folder. Just follow `pytest` best practices and everything will flow.

### Coverage

Coverage analysis is done with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html). Some options are configured through the `watch.sh` script, and some are in `.cov.conf` file.

In particular the option `fail_under = 100.0` states that testing will be considered failed if coverage goes under 100%. You may edit this requirement at your own risk.

### Rerun script

You can configure (or modify) the rerun script as you wish. It's just part of our code now. It is called from `watch.sh`, and the code is in `rerun.sh`.

Interesting parts may be the `exclude` regular expression for files to be excluded from monitoring, and the `--verbose` option to see more details about the monitoring process itself.