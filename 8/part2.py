def count_scene(tr, left, right, up, down):
    scene = 1
    left.reverse()
    up.reverse()
    for mat in [left, right, up, down]:
        count = 0
        for i in range(len(mat)):
            count += 1
            if mat[i]>=tr:
                break
        scene = count*scene if count !=0 else scene
    return scene

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
    max_scene = 0
    for i in range(rows):
        for j in range(cols):
            max_scene = max(max_scene, count_scene(tree[i][j], tree[i][:j],
                                                   tree[i][j+1:],
                                                   list(list(zip(*tree))[j][:i]),
                                                   list(list(zip(*tree))[j][i+1:])))
    print(max_scene)

