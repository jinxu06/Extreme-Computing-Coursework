#!/bin/bash

DIR=`dirname "$(readlink -f "$0")"`
output="/user/s1673820/assignment2/task3"
temp="/user/s1673820/assignment2/temp3"

hdfs dfs -test -d $output
if (($?==0));then
    hdfs dfs -rm -r $output
fi
hdfs dfs -test -d $temp
if (($?==0));then
    hdfs dfs -rm -r $temp
fi

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask3-1' \
    -input /data/assignments/ex2/part2/stackLarge.txt \
    -output $temp \
    -mapper mapper1.py \
    -file $DIR/mapper1.py \
    -reducer reducer1.py \
    -file $DIR/reducer1.py \
    -combiner combiner1.py \
    -file $DIR/combiner1.py \

# The second map reduce is really just compare all the one line results from last reducers
# But it seems that we are asked to do so using mapreduce......(according to piazza)
# I did not use pre-defined Identity Map in the second mapreduce, reason is explained in mapper2.py

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -D mapred.job.name='JinXTask3-2' \
    -D mapreduce.job.reduces=1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options=-k1nr \
    -input $temp \
    -output $output \
    -mapper mapper2.py \
    -file $DIR/mapper2.py \
    -reducer reducer2.py \
    -file $DIR/reducer2.py \

hdfs dfs -test -d $temp
if (($?==0));then
    hdfs dfs -rm -r $temp
fi

hdfs dfs -cat /user/s1673820/assignment2/task3/* | head -n 20 > $DIR/output.out
