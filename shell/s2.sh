#!/bin/bash

for i in `ls *.txt`
do
    echo " -------------------- $i"
    cat $i
    echo "==================================="
done

