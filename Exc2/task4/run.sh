#!/bin/bash

DIR=`dirname "$(readlink -f "$0")"`
output="/user/s1673820/assignment2/task4"
temp="/user/s1673820/assignment2/temp4"

hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi
hdfs dfs -test -d $temp
if (($?==0));then
    hdfs dfs -rm -r $temp
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask4-1' \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D num.key.fields.for.partition=1 \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1 \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
    -input /data/assignments/ex2/part2/stackLarge.txt \
    -output $output \
    -mapper mapper1.py \
    -file $DIR/mapper1.py \
    -reducer reducer1.py \
    -file $DIR/reducer1.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask4-2' \
    -input $output \
    -output $temp \
    -mapper mapper2.py \
    -file $DIR/mapper2.py \
    -reducer reducer2.py \
    -file $DIR/reducer2.py \
    -combiner combiner2.py \
    -file $DIR/combiner2.py \


hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask3-3' \
    -D mapreduce.job.reduces=1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options=-k1nr \
    -input $temp \
    -output $output \
    -mapper mapper3.py \
    -file $DIR/mapper3.py \
    -reducer reducer3.py \
    -file $DIR/reducer3.py \

hdfs dfs -test -d $temp
if (($?==0));then
    hdfs dfs -rm -r $temp
fi

hdfs dfs -cat /user/s1673820/assignment2/task4/* | head -n 20 > $DIR/output.out
