#!/bin/sh

make publish
cd ../jaabell.github.io
cp -R ../blog/output/* .
git add . 
git commit
git push 


