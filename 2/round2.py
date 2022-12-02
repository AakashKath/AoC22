with open('input', 'r') as file:
    x = file.readlines()
    total = 0
    for i in x:
        move = i.split('\n')[0]
        op_mv = move.split(' ')[0]
        m_mv = move.split(' ')[1]
        if move in ['A Y', 'B X', 'C Z']:
            total += 1
        elif move in ['A Z', 'B Y', 'C X']:
            total += 2
        elif move in ['A X', 'B Z', 'C Y']:
            total += 3
        if m_mv == 'Y':
            total += 3
        if m_mv == 'Z':
            total += 6
    print(total)

