def operate(operator1, operator2, operation):
    if operation == '+':
        return operator1 + operator2
    if operation == '-':
        return operator1 - operator2
    if operation == '*':
        return operator1 * operator2
    if operation == '/':
        return operator1 / operator2

def compute_yell(yell, monkey, find_humn):
    if find_humn and monkey == 'humn':
        return float('inf')
    ans = yell.get(monkey)
    if isinstance(ans, int):
        return ans
    return operate(compute_yell(yell, ans[0], find_humn), compute_yell(yell, ans[2], find_humn), ans[1])

def part1(yell):
    return compute_yell(yell, 'root', False)

def part2(yell):
    ans = yell.pop('root')
    ans0 = compute_yell(yell, ans[0], True)
    ans2 = compute_yell(yell, ans[2], True)
    if ans0 == float('inf'):
        yell.update({ans[2]: ans2})
    else:
        yell.update({ans[0]: ans0})
    key_to_update = ''
    for key, value in yell.items():
        if isinstance(value, list) and 'humn' in value:
            key_to_update = key
            break
    v1, op, v2 = yell.pop(key_to_update)
    second_key = v1 if v2 == 'humn' else v1
    if op == '+':
        yell.update({'humn': [key_to_update, '-', second_key]})
    elif op == '*':
        yell.update({'humn': [key_to_update, '/', second_key]})
    elif op == '-':
        if v1 == 'humn':
            yell.update({'humn': [key_to_update, '+', second_key]})
        else:
            yell.update({'humn': [second_key, '-', key_to_update]})
    elif op == '/':
        if v1 == 'humn':
            yell.update({'humn': [key_to_update, '*', second_key]})
        else:
            yell.update({'humn': [second_key, '/', key_to_update]})
    return compute_yell(yell, 'humn', False)

with open('input', 'r') as file:
    x = file.readlines()
    yell = {}
    for i in x:
        key, value = i.split('\n')[0].split(': ')
        if len(value.split(' ')) == 1:
            yell.update({key: int(value)})
        else:
            yell.update({key: value.split(' ')})
    #print(part1(yell))
    print(part2(yell))

