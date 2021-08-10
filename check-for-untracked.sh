#!/bin/bash

UNTRACKED=$(git status --porcelain=v1 | grep '??')
echo 'TEST'
echo $UNTRACKED
if [[ "$UNTRACKED" == "" ]]
then
  exit 0
else
  exit 1
fi

