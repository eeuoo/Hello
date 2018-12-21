#!/bin/bash

PRE_IFS=$IFS
IFS="
"
TOTAL_SIZE=0

for i in `ls -al /bin`; do

    F=`echo $i | awk '{print $9}'`       
    S=`echo $i | awk '{print $5}'`

    if [ "$F" == "." ] || [ "$F" == ".." ] || [ "$F" == "" ]; then
        continue
    fi

    echo "$F $S"
    
    TOTAL_SIZE=`expr $TOTAL_SIZE + $S` 

done

echo $TOTAL_SIZE

IFS=$PRE_IFS

