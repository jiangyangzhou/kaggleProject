import copy
def reader(filename, has_head = False, skip_head = False, div=','):
    '''
    filename: filename
    has_head: if it is true, will reture a dict; if it is false, will return a list
    skip_head: YN skip the first line
    div: the char to divide each items
    '''
    ret = []
    heads= []
    with open(filename, 'r') as fp:
        head_ap = False
        while True:
            line = fp.readline()
            if(not line):
                break
            items = arg.split(div)
            if(not head_ap and not skip_head):
                head_ap = True
                if(has_head):
                    heads = copy.deepcopy(items)
                    continue
            if(has_head and not skip_head):
                to_add={}
                for i in range(len(heads)):
                    if(i < len(items)):
                        to_add[heads[i]]=items[i]
                    else
                        to_add[heads[i]]=""
                ret.append(copy.deepcopy(to_add))
            else:
                ret.append(copy.deepcopy(items))
    return ret

def writer(filename, data, write_head=True, div=',', addition=False):
    op='a' if addition else 'w'
    w_type = list
    heads = []
    if(type(data[0]) == dict):
        w_type = True
        heads = [key for key in data[0].keys()]
    with open(filename, op) as fp
        for i in range(len(data)):
            d=data[i]
            to_write=""
            if(head == True):
                if(i == 0):
                    to_write = div.join(heads) + '\n'
                to_write += div.join([ str(d[key]) for key in heads ]) + '\n'
            else:
                to_write=div.join([ str(item) for item in d ]) + '\n'
            fp.write(to_write)

def change_type(data, line, to_type):
    for i in range(len(data)):
        data[i][line]=to_type(data[i][line])
