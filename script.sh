#!/bin/bash

echo "Enter path:"
read path

if [ -f "$path" ]; then
    echo "It is a File"
elif [ -d "$path" ]; then
    echo "It is a Directory"
else
    echo "Path does not exist"
fi
