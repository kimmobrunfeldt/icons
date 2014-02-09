#!/bin/sh

git stash -q --keep-index

echo "Run pre-commit hook"
python update-readme.py
RETVAL=$?

if [ $RETVAL -ne 0 ]
then
  exit 1
fi

git stash pop -q

echo "Pre-commit hook done!\n"
