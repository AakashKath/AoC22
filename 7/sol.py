import pandas as pd

def append_size(directory_tree):
    total_size = 0
    for k, v in directory_tree.items():
        if isinstance(v, dict):
            total_size += append_size(v)
        else:
            total_size += int(v)
    directory_tree.update({'total_size': total_size})
    return total_size

def calculate_total_size(directory_tree, size_array):
    final_size = 0
    if directory_tree['total_size'] <= 100000:
        final_size += directory_tree['total_size']
        size_array.append(directory_tree['total_size'])
    for k, v in directory_tree.items():
        if isinstance(v, dict):
            final_size += calculate_total_size(v, size_array)
    return final_size

with open('input', 'r') as file:
    x = file.readlines()
    directory_tree = {"/": {}}
    directory_queue = list()
    i = 0
    while i < len(x):
        if x[i][0] == '$':
            command = x[i].split('\n')[0][2:]
            if command.startswith('cd'):
                if command.endswith('..'):
                    directory_queue.pop()
                else:
                    directory_queue.append(command[3:])
                i += 1
            if command.startswith('ls'):
                i += 1
                temp_dict = directory_tree
                for j in directory_queue:
                    temp_dict = temp_dict[j]
                while i < len(x) and x[i][0] != '$':
                    if x[i].startswith('dir'):
                        temp_dict.update({x[i][4:].split('\n')[0]: {}})
                    else:
                        size, file_name = x[i].split('\n')[0].split(' ')
                        temp_dict.update({file_name: size})
                    i += 1
        else:
            i += 1
    append_size(directory_tree)
    size_array = list()
    print(calculate_total_size(directory_tree, size_array))
    print(directory_tree)
    size_array.sort()
    to_be_freed = 30000000 - 70000000 + max(size_array)
    print(max(size_array))
    for i in size_array:
        if i >= to_be_freed:
            print(i)
            break

