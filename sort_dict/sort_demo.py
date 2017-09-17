# coding: utf-8

SPLIT_STR = ','

def read_by_key(filepath, SPLIT_STR):
    data_dict = dict()
    o_exception_data = open('exception_data', 'w')
    with open(filepath, 'r') as ofile:
        for line in ofile:
            if None == line or '' == line.strip() or len(line.strip().split(SPLIT_STR)) != 2:
                o_exception_data.write(line)
                continue
            name, score = line.strip().split(SPLIT_STR)
            try:
                data_dict[name] = int(score)
            except:
                o_exception_data.write(line)
                continue
    o_exception_data.close()
    return data_dict

def sort_by_key:
    
def sort_by_value:


if __name__ == '__main__':
    
    filepath = './data/score'
    data_dict = read_by_key(filepath, SPLIT_STR)

    sort_by_key(data_dict)
    sort_by_value(data_dict)
