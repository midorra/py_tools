#!/usr/bin/env python
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

    for line in sys.stdin:
        words = line.strip().split(" ")
        w_dict = dict()
        tf_sum = 0

        ### init w_dict
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
        standard_entropy = 0
        for w in w_dict:
            w_prob = 1.0 * w_dict[w]["tf"] / tf_sum
            standard_entropy += (-1.0) * w_prob * math.log(w_prob)

        ### calculate word IG-Score
        for w in w_dict:
            w_entropy = 0
            w_tf_sum = tf_sum - w_dict[w]["tf"]
            for x in w_dict:
                if x == w:
                    continue
                x_prob = 1.0 * w_dict[x]["tf"] / w_tf_sum
                w_entropy += (-1.0) * x_prob * math.log(x_prob)
            w_ig = w_entropy - standard_entropy
            print w + "\t" + str(w_ig)
    
