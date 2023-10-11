#!/bin/bash

SCRIPTPATH=$(dirname `realpath "$0"`)

if [[ "$1" = "-p" || "$1" = "--pull" ]]; then
    echo "pulling latest changes..."
    cd "$SCRIPTPATH"
    git pull origin master
    echo "DONE"
    exit 0;
fi

read -p "enter commit description: " commitDescription

git add "$SCRIPTPATH"

git commit -m "$commitDescription"

git push origin master
