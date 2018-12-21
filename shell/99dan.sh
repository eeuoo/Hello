#!/bin/sh

for i in {2..9};

do

echo "--- $i단---" 

    for j in {1..9};

    do 
        DDD=$(( $i * $j ))
        printf "${i} X ${j} = %d\n" $DDD 
                
    done


done



