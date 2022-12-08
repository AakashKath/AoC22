with open('input', 'r') as file:
    x = file.readlines()
    tree = list()
    for i in x:
        local = list()
        line = i.split('\n')[0]
        for j in line:
            local.append(int(j))
        tree.append(local)
    rows = len(tree)
    cols = len(tree[0])
    visible = 0
    for i in range(rows):
        for j in range(cols):
            if i in [0, rows-1] or j in [0, cols-1]:
                visible += 1
            elif tree[i][j] > min(max(tree[i][:j]), max(tree[i][j+1:]),
                                  max(list(zip(*tree))[j][i+1:]),
                                  max(list(zip(*tree))[j][:i])):
                visible += 1
    print(visible)

