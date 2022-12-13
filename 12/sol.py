def is_valid(i, j, mat, visited, old_ord):
    if (i>=0 and j>=0) and (i<len(mat) and j<len(mat[0])) \
       and visited[i][j] == 0:
        new_ord = ord('a') if mat[i][j] == 'S' else ord(mat[i][j])
        if new_ord - old_ord >= -1:
            return True
    return False

def shortest_path(mat, e_pos):
    queue = list()
    queue.append(e_pos)
    visited = [[0 for _ in range(len(mat[0]))] for i in range(len(mat))]
    visited[e_pos[0]][e_pos[1]] = 1
    while queue:
        curr = queue.pop(0)
        i = curr[0]
        j = curr[1]
        depth = curr[2]
        if mat[i][j] in ['S', 'a']:
            return depth
        old_ord = ord('z') if mat[i][j] == 'E' else ord(mat[i][j])
        if is_valid(i-1, j, mat, visited, old_ord):
            queue.append([i-1, j, depth+1])
            visited[i-1][j] = 1
        if is_valid(i+1, j, mat, visited, old_ord):
            queue.append([i+1, j, depth+1])
            visited[i+1][j] = 1
        if is_valid(i, j-1, mat, visited, old_ord):
            queue.append([i, j-1, depth+1])
            visited[i][j-1] = 1
        if is_valid(i, j+1, mat, visited, old_ord):
            queue.append([i, j+1, depth+1])
            visited[i][j+1] = 1
    return -1

with open('input', 'r') as file:
    x = file.readlines()
    mat = list()
    e_pos = [0, 0]
    i_counter = 0
    for i in x:
        st = i.split('\n')[0]
        temp = list()
        j_counter = 0
        for ch in st:
            if ch == 'E':
                e_pos = [i_counter, j_counter, 0]
            temp.append(ch)
            j_counter += 1
        i_counter += 1
        mat.append(temp)
    print(shortest_path(mat, e_pos))

