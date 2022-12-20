def move_ele(ls, e, i):
    new_position = (i + e[1]) % (len(ls)-1)
    ls.remove(e)
    ls.insert(new_position, e)

with open('input', 'r') as file:
    x = file.read()
    dupl = [(i, int(e)*811589153) for i, e in enumerate(x.split('\n')) if e]
    dupl_len = len(dupl)
    for k in range(10):
        for i in range(dupl_len):
            for index, ele in enumerate(dupl):
                if ele[0] == i:
                    move_ele(dupl, ele, index)
                    break
    zero = 0
    for index, ele in enumerate(dupl):
        if ele[1] == 0:
            zero = index
            break
    su = 0
    for i in [1000, 2000, 3000]:
        su += dupl[(zero+i) % dupl_len][1]
    print(su)
