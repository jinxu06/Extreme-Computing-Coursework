#!/bin/bash

DIR=`dirname "$(readlink -f "$0")"`
input="/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt"
output="/user/s1673820/assignment2/task6"

hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi

hdfs dfs -mkdir $output
cat $input | $DIR/reservior_sampling.py 100 > $DIR/full-output.out
hdfs dfs -copyFromLocal $DIR/full-output.out $output 
cat $DIR/full-output.out | head -n 20 > $DIR/output.out
rm $DIR/full-output.out
