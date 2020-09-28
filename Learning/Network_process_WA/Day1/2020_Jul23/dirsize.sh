#!/bin/bash
if [[ -z "$1" ]]
then
    dir="."
else
    dir="$1"
fi

expr $(ls -lRa ${dir}   | \
       grep -v '^d'     | \
       sed 's/ \+/ /g'  | \
       cut -f5 -d' '    | \
       egrep '^[0-9]+$' | \
       xargs            | \
       sed 's/ / + /g')

