# coding: utf-8

SPLIT_STR = ','

def read_by_key(filepath, SPLIT_STR):
    data_dict = dict()
    swp_data_dict = dict()
    o_exception_data = open('./data/exception_data', 'w')
    with open(filepath, 'r') as ofile:
        for line in ofile:
            if None == line or '' == line.strip() or len(line.strip().split(SPLIT_STR)) != 2:
                o_exception_data.write(line)
                continue
            name, score = line.strip().split(SPLIT_STR)
            try:
                data_dict[name] = int(score)
                swp_data_dict[int(score)] = name
            except:
                o_exception_data.write(line)
                continue
    o_exception_data.close()
    return data_dict, swp_data_dict

def sort_by_key(swp_data_dict, outpath):
    with open(outpath, 'w') as oout:
        sorted_list = sorted(swp_data_dict.items(), lambda x, y: cmp(x[0], y[0]), reverse = True)
        for tuplex in sorted_list:
            oout.write(str(tuplex[0]) + '\t' + tuplex[1] + '\n')
    print 'sort by key value is over'

def sort_by_value(data_dict, outpath):
    with open(outpath, 'w') as oout:
        sorted_list = sorted(data_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse = True)
        for tuplex in sorted_list:
            oout.write(tuplex[0] + '\t' + str(tuplex[1]) + '\n')
    print 'sort by value process is over'

if __name__ == '__main__':
    
    filepath = './data/score'
    data_dict, swp_data_dict = read_by_key(filepath, SPLIT_STR)
    
    outpath_for_key_sort = './data/key_sort_rst'
    outpath_for_value_sort = './data/value_sort_rst'

    sort_by_key(swp_data_dict, outpath_for_key_sort)
    sort_by_value(data_dict, outpath_for_value_sort)

