#!/bin/sh

if [ -h .git/hooks/pre-commit ]; then
    echo "symlink exists, g2g"
else
    cd .git/hooks/
    echo "creating sym link"
    ln -s ../../pre-commit pre-commit
fi