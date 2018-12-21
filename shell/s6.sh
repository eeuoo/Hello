#!/bin/sh

if [ $# -lt 2 ]; then
    echo "Input 2 files, please.."
    exit 0
fi

DATE=`date +%Y%m%d --date=yesterday`
FN="${DATE}.log"
#echo "mv $1 $FN"

cat $1 > $FN

cat $2 >> $FN



