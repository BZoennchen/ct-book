#!/bin/sh
rm _build -r -f
jupyter-book build .
git add ./*
git commit -m "update book content"
git push origin master
ghp-import -n -p -f _build/html