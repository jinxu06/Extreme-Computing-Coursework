#!/bin/bash

output="/user/s1673820/assignment1/task1"
my_home="/afs/inf.ed.ac.uk/user/s16/s1673820"
hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask1' \
    -D mapreduce.job.reduces=0 \
    -files $my_home/Assignment/Exc1/task1/mapper.py \
    -input /data/assignments/ex1/webLarge.txt \
    -output /user/s1673820/assignment1/task1 \
    -mapper mapper.py \

hdfs dfs -cat /user/s1673820/assignment1/task1/* | head -n 20 > $my_home/Assignment/Exc1/task1/output.out
