#!/bin/bash

DIR=`dirname "$(readlink -f "$0")"`
output="/user/s1673820/assignment2/task1"

hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask1' \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D num.key.fields.for.partition=1 \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.map.output.key.field.separator=" " \
    -D mapreduce.partition.keypartitioner.options=-k1 \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
    -input /data/assignments/ex2/part1/large \
    -output $output \
    -mapper mapper.py \
    -file $DIR/mapper.py \
    -reducer reducer.py \
    -file $DIR/reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat /user/s1673820/assignment2/task1/* | head -n 20 > $DIR/output.out
