#!/usr/bin/env python
# coding: utf-8

import sys
import math

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    
    current_word = ""
    current_ig_cnt = 0
    current_ig_sum = 0

    word = ig_str = ig = None
    for line in sys.stdin:
        if len(line.strip().split("\t")) != 2:
            continue
        word, ig_str = line.strip().split("\t")
        try:
            ig = float(ig_str)
        except Exception as e:
            continue
        if word != current_word:
            if current_word.strip() != "":
                #print current_word + "\t" + str(current_ig_sum) ### sum_ig
                print current_word + "\t" + str(1.0 * current_ig_sum / current_ig_cnt) ### avg_ig
            current_word = word
            current_ig_cnt = 1
            current_ig_sum = ig
        else:
            current_ig_cnt += 1
            current_ig_sum += ig

    if word == current_word:
        #print current_word + "\t" + str(current_ig_sum) ### sum_ig
        print current_word + "\t" + str(1.0 * current_ig_sum / current_ig_cnt) ### avg_ig
        
