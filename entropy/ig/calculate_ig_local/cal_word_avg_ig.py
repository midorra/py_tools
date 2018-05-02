# coding: utf-8

import sys
import math

reload(sys)
sys.setdefaultencoding("utf-8")

def init():
    stop_word_set = set()
    return stop_word_set

if __name__ == "__main__":

    stop_word_set = init()
    
    #seg_file = "../data/seg_file/seg_file_small"
    #seg_file = "../data/seg_file/seg_w2v_2018"
    seg_file = "../data/seg_file/seg_w2v_2018_head_50w"
    
    orst_avg_ig = open("../data/word_ig/word_avg_ig_50w", "w")
    orst_sum_ig = open("../data/word_ig/word_sum_ig_50w", "w")

    with open(seg_file, "r") as ofile:

        ig_dict = dict()
        line_cnt = 0

        print "Progress: calculate word IG-Score"
        for line in ofile:
            line_cnt += 1
            if line_cnt % 1000 == 0:
                print "process ===> " + str(line_cnt / 1000) + " k  ///  ig_dict size = " + str(len(ig_dict))

            words = line.strip().split(" ")
            w_dict = dict()
            tf_sum = 0

            ### init w_dict
            #print "init w_dict"
            for w in words:
                if w in stop_word_set:
                    continue
                if w not in w_dict.keys():
                    node = dict()
                    node["word"] = w
                    node["tf"] = 1
                    w_dict[w] = node
                else:
                    w_dict[w]["tf"] += 1
                tf_sum += 1

            ### calculate standard IE-Score
            #print "calculate standard IE-Score"
            standard_entropy = 0
            for w in w_dict:
                w_prob = 1.0 * w_dict[w]["tf"] / tf_sum
                standard_entropy += (-1.0) * w_prob * math.log(w_prob)

            ### calcualte word IG-Score
            #print "calculate word IG-Score"
            for w in w_dict:
                w_entropy = 0
                w_tf_sum = tf_sum - w_dict[w]["tf"]
                for x in w_dict:
                    if x == w:
                        continue
                    x_prob = 1.0 * w_dict[x]["tf"] / w_tf_sum
                    w_entropy += (-1.0) * x_prob * math.log(x_prob)
                w_ig = w_entropy - standard_entropy
                
                ### add to ig_dict
                if w not in ig_dict:
                    tmp = dict()
                    tmp["ig_sum"] = w_ig
                    tmp["ig_cnt"] = 1
                    ig_dict[w] = tmp
                else:
                    ig_dict[w]["ig_sum"] += w_ig
                    ig_dict[w]["ig_cnt"] += 1
         
        ### calculate word average IG-Score
        print "Progress: calculate average IG-Score"
        avg_ig_dict = dict()
        sum_ig_dict = dict()
        for w in ig_dict:
            avg_ig_dict[w] = ig_dict[w]["ig_sum"] / ig_dict[w]["ig_cnt"]
            sum_ig_dict[w] = ig_dict[w]["ig_sum"]

        ### check word average IG-Score
        print "Progress: sorted and write word average IG-Score"
        sorted_lst = sorted(avg_ig_dict.items(), lambda x,y : cmp(x[1], y[1]), reverse = True)
        for i in sorted_lst:
            orst_avg_ig.write(i[0] + "\t" + str(i[1]) + "\n")

        ### check word sum IG-Score
        print "Progress: sprted and write word sum IG-Score"
        sorted_lst = sorted(sum_ig_dict.items(), lambda x,y : cmp(x[1], y[1]), reverse = True)
        for i in sorted_lst:
            orst_sum_ig.write(i[0] + "\t" + str(i[1]) + "\n")
    
    orst_avg_ig.close() 
    orst_sum_ig.close()
    
