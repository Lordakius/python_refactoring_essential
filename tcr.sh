#!/bin/bash

if [ -z ${1+x} ]; then msg="It works!"; else msg="$1"; fi

git add .
python -m unittest discover && git commit -m "$msg" || git reset --hard
git push
