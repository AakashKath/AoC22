with open('input', 'r') as file:
    x = file.readlines()
    ls = list()
    for i in range(9):
        local = list()
        for j in range(7, -1, -1):
            local.append(x[j][4*i+1])
        ls.append(local)
    ls = [list(filter(None, [j.replace(' ', '') for j in i])) for i in ls]
    for i in x[10:]:
        _, count, _, fro, _, to = i.split('\n')[0].split(' ')
        for j in range(int(count)):
            if ls[int(fro)-1]:
                ls[int(to)-1].append(ls[int(fro)-1].pop())
    for i in ls:
        print(i.pop())

