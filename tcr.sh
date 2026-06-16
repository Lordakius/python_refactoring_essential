#!/bin/bash

git add .
python -m unittest discover && git commit -m "It works!" || git reset --hard
