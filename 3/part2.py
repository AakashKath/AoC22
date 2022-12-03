with open('input', 'r') as file:
    x = file.readlines()
    total = 0
    for i in range(len(x)//3):
        i1 = x[3*i].split('\n')[0]
        i2 = x[3*i+1].split('\n')[0]
        i3 = x[3*i+2].split('\n')[0]
        common = ''.join(set(i1) & set(i2) & set(i3))
        if ord(common) > 96:
            total += ord(common)-96
        else:
            total += ord(common)-38
    print(total)

