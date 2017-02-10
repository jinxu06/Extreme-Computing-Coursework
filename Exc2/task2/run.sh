#!/bin/bash

DIR=`dirname "$(readlink -f "$0")"`
output="/user/s1673820/assignment2/task2"
hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask2' \
    -D mapreduce.job.reduces=1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options=-k1nr \
    -input /data/assignments/ex2/part2/stackSmall.txt \
    -output /user/s1673820/assignment2/task2 \
    -mapper mapper.py \
    -file $DIR/mapper.py \
    -reducer reducer.py \
    -file $DIR/reducer.py \

hdfs dfs -cat /user/s1673820/assignment2/task2/* | head -n 20 > $DIR/output.out
