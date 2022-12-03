with open('input', 'r') as file:
    x = file.readlines()
    total = 0
    for i in x:
        item = i.split('\n')[0]
        r1 = item[:len(item)//2]
        r2 = item[len(item)//2:]
        common = ''.join(set(r1).intersection(r2))
        if ord(common) > 96:
            total += ord(common)-96
        else:
            total += ord(common)-38
    print(total)

