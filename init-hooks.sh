#!/bin/sh

if [ -h .git/hooks/pre-commit ]; then
    echo "symlink exists, g2g"
else
    echo "creating sym link"
    ln -s pre-commit .git/hooks/pre-commit
fi