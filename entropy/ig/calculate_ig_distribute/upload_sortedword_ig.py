# !/usr/bin/env python
# coding: utf-8 

import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    
    date_version = "20180410"
    sum_or_avg_flag = "sum"
    #sum_or_avg_flag = "avg"
    
    hdfs_sorted_ig_path = "/user/datacenter/zhangpeng/related_search/word_entropy/base_ig"
    hdfs_sorted_ig_file = hdfs_sorted_ig_path + "/sorted_word_" + sum_or_avg_flag + "_ig_" + date_version
    local_ig_sorted_file = "../data/word_ig/sorted_word_" + sum_or_avg_flag + "_ig_" + date_version

    ### "upload sorted word ig"
    print "\nProgress: upload sorted word ig"
    t1 = datetime.datetime.now()
    os.system("/home/appops/hadoop-current/bin/hadoop fs -rm " + hdfs_sorted_ig_file)
    os.system("/home/appops/hadoop-current/bin/hadoop fs -put " + local_ig_sorted_file + " " + hdfs_sorted_ig_path)
    t2 = datetime.datetime.now()
    print "timecost = " + str(t2 - t1)
    
