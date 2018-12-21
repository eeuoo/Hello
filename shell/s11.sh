#!/bin/bash

NEWFILE="dir_info.csv"
 
if [ $# -eq 0 ]; then
    echo "Input the filename, please.."
    exit 0
fi

PRE_IFS=$IFS
IFS=

for i in `./$1`;
do
     
   echo $i >> $NEWFILE

done

IFS=$PRE_IFS 
