#!/bin/bash

./rerun.sh \
  --clear \
  --exclude '__pycache__|\.pytest_cache|.*\.pyc' \
  pytest --cov-config=.cov.conf --cov=. --no-cov-on-fail
