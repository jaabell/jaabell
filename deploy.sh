#!/bin/sh

make publish
cd ../jaabell.github.io
cp -R ../blog2/output/* .
git add . 
git commit
git push 


