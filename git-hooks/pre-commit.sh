#!/bin/sh

git stash -q --keep-index

python update-readme.py
RETVAL=$?

if [ $RETVAL -ne 0 ]
then
  exit 1
fi

git stash pop -q
