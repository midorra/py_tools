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
    
    hdfs_ig_file = "/user/datacenter/zhangpeng/related_search/word_entropy/base_ig/" + sum_or_avg_flag + "_word_ig_" + date_version + "/*"
    local_ig_file = "../data/word_ig/word_" + sum_or_avg_flag + "_ig_" + date_version
    local_ig_sorted_file = "../data/word_ig/sorted_word_" + sum_or_avg_flag + "_ig_" + date_version

    ### "delate local file"
    os.system("rm -f " + local_ig_file)
    os.system("rm -f " + local_ig_sorted_file)

    ### download word ig
    print "\nProgress: download word ig"
    t1 = datetime.datetime.now()
    os.system("/home/appops/hadoop-current/bin/hadoop fs -getmerge " + hdfs_ig_file + " " + local_ig_file)
    t2 = datetime.datetime.now()
    print "timecost = " + str(t2 -t1)

    ### sort word ig
    print "\nProgress: sort word ig"
    t1 = datetime.datetime.now()
    with open(local_ig_sorted_file, "w") as orst:
        with open(local_ig_file, "r") as ofile:
            wdict = dict()
            for line in ofile:
                msgs = line.strip().split("\t")
                if len(msgs) != 2 or msgs[0].strip() == "":
                    continue
                try:
                    wdict[msgs[0]] = float(msgs[1])
                except Exception as e:
                    print e
                    continue
            sorted_lst = sorted(wdict.items(), lambda x,y : cmp(x[1], y[1]), reverse = True)
            for i in sorted_lst:
                orst.write(i[0] + "\t" + str(i[1]) + "\n")
    t2 = datetime.datetime.now()
    print "timecost = " + str(t2 - t1)
    
