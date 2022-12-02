with open('input', 'r') as file:
    x = file.readlines()
    total = 0
    for i in x:
        move = i.split('\n')[0]
        op_mv = move.split(' ')[0]
        m_mv = move.split(' ')[1]
        if move in ['A Y', 'B Z', 'C X']:
            total += 6
        elif move in ['A X', 'B Y', 'C Z']:
            total += 3
        if m_mv == 'X':
            total += 1
        if m_mv == 'Y':
            total += 2
        if m_mv == 'Z':
            total += 3
    print(total)

