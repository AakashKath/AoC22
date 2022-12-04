with open('input', 'r') as file:
    x = file.readlines()
    count = 0
    print(len(x))
    for i in x:
        c = i.split('\n')[0]
        p1, p2 = c.split(',')
        r11, r12 = [int(_) for _ in p1.split('-')]
        r21, r22 = [int(_) for _ in p2.split('-')]
        if set(range(r11, r12+1)).intersection(range(r21, r22+1)):
            count += 1
    print(count)

