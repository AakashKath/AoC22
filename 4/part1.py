with open('input', 'r') as file:
    x = file.readlines()
    count = 0
    for i in x:
        c = i.split('\n')[0]
        p1, p2 = c.split(',')
        r11, r12 = [int(_) for _ in p1.split('-')]
        r21, r22 = [int(_) for _ in p2.split('-')]
        if (r11 <= r21 and r12 >= r22) or (r21 <= r11 and r22 >= r12):
            count += 1
    print(count)

