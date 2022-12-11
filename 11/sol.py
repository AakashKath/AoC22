from math import prod

def execute_operation(operation, item):
    if operation[1] == '*':
        if operation[2] == 'old':
            return item*item
        return item*int(operation[2])
    return item+int(operation[2])

def execute_round(item_list, operation, condition, true_move, false_move,
                  inspect_count, cap,  monkey_no):
    for item in item_list[monkey_no]:
        item = execute_operation(operation[monkey_no], item)
        #item = item//3
        item = item%cap
        if item%condition[monkey_no] == 0:
            item_list[true_move[monkey_no]].append(item)
        else:
            item_list[false_move[monkey_no]].append(item)
        inspect_count[monkey_no] += 1
    item_list[monkey_no] = []
    return item_list, inspect_count

with open('input', 'r') as file:
    x = file.readlines()
    item_list = list()
    operation = list()
    condition = list()
    true_move = list()
    false_move = list()
    inspect_count = list()
    for i in range(8):
        item_list.append([int(_) for _ in x[7*i+1].split('\n')[0].split(':')[1].split(',')])
        operation.append(x[7*i+2].split('\n')[0].split(' ')[-3:])
        condition.append(int(x[7*i+3].split('\n')[0].split(' ')[-1]))
        true_move.append(int(x[7*i+4].split('\n')[0].split(' ')[-1]))
        false_move.append(int(x[7*i+5].split('\n')[0].split(' ')[-1]))
        inspect_count.append(0)

    cap = prod(condition)

    for i in range(10000):
        for j in range(8):
            item_list, inspect_count = execute_round(item_list, operation,
                                                     condition, true_move,
                                                     false_move, inspect_count,
                                                     cap, j)
    i1, i2 = sorted(inspect_count, reverse=True)[:2]
    print(i1*i2)

