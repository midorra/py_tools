#!/bin/bash

/usr/bin/kinit -kt /home/appops/keytab/datacenter.keytab datacenter/dev@HADOOP.HZ.NETEASE.COM  && /usr/bin/kinit -R

hadoop=/home/appops/hadoop-current/bin/hadoop
spark=/home/appops/hadoop-current/bin/spark-submit

$hadoop fs -rm -r /user/datacenter/zhangpeng/related_search/word_entropy/base_ig/avg_word_ig_20180410

$hadoop jar /home/appops/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.5.2.jar \
    -D mapred.map.tasks=400 \
    -D mapred.reduce.tasks=400 \
    -D mapred.job.priority=VERY_HIGH \
    -D mapreduce.job.queuename=root.data_analysis.default \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -file "mapper.py" \
    -file "reducer.py" \
    -output /user/datacenter/zhangpeng/related_search/word_entropy/base_ig/avg_word_ig_20180410 \
    -input /user/datacenter/zhangpeng/warehouse/core_data/article_seg_for_w2v/seg_w2v_2018 \
    -input /user/datacenter/zhangpeng/warehouse/core_data/article_seg_for_w2v/seg_w2v_2017 \
    -input /user/datacenter/zhangpeng/warehouse/core_data/article_seg_for_w2v/seg_w2v_2016 \
    -input /user/datacenter/zhangpeng/warehouse/core_data/article_seg_for_w2v/seg_w2v_2015 
