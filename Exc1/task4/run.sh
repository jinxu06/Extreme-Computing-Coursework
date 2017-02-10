#!/bin/bash

output="/user/s1673820/assignment1/task4"
my_home="/afs/inf.ed.ac.uk/user/s16/s1673820"
hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name="JinXTask4" \
    -D mapreduce.job.reduces=10 \
    -input /user/s1673820/assignment1/task2/* \
    -output /user/s1673820/assignment1/task4 \
    -mapper mapper.py \
    -file $my_home/Assignment/Exc1/task4/mapper.py \
    -reducer reducer.py \
    -file $my_home/Assignment/Exc1/task4/reducer.py

hdfs dfs -cat /user/s1673820/assignment1/task4/* | head -n 20 > $my_home/Assignment/Exc1/task4/output.out
