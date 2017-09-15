# coding: utf-8

import esm

if __name__ == "__main__":
    
    word_index = esm.Index()
    o_rst = open('./data/search_rst', 'w')
    with open('./data/search_words', 'r') as o_words:
        for line in o_words:
            if None != line and line.strip() != '':
                word_index.enter(line.strip())
    word_index.fix()
    with open('./data/search_file', 'r') as o_file:
        for line in o_file:
            if None == line or line.strip() == '':
                continue
            search_rst_list = word_index.query(line.strip())
            for sr in search_rst_list:
                print sr[1]
                o_rst.write(sr[1] + '\n')
    o_rst.close()
    print 'process finished'

