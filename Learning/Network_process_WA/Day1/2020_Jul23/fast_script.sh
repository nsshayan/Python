#!/bin/sh

while true
do
    printf "shell script($$): $I"
    I=$((I + 1))
    sleep 1
done

