#!/bin/bash

output="/user/s1673820/assignment1/task2"
my_home="/afs/inf.ed.ac.uk/user/s16/s1673820"
hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name="JinXTask2" \
    -D mapreduce.job.reduces=10 \
    -input /user/s1673820/assignment1/task1/* \
    -output /user/s1673820/assignment1/task2 \
    -mapper mapper.py \
    -file $my_home/Assignment/Exc1/task2/mapper.py \
    -reducer reducer.py \
    -file $my_home/Assignment/Exc1/task2/reducer.py

hdfs dfs -cat /user/s1673820/assignment1/task2/* | head -n 20 > $my_home/Assignment/Exc1/task2/output.out
