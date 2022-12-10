def draw_screen(screen):
    for i in range(len(screen)):
        print(''.join(screen[i]))

def update_screen(screen, sprite, cycle):
    if cycle%40 in sprite:
        screen[cycle//40][cycle%40] = '#'

with open('input', 'r') as file:
    x = file.readlines()
    cycle = 0
    _sum = 1
    result = 0
    sprite = [-1, 0, 1]
    screen = [['.' for _ in range(40)] for __ in range(6)]
    for i in x:
        command = i.split('\n')[0]
        if command.startswith('noop'):
            update_screen(screen, sprite, cycle)
            cycle += 1
            continue
        for j in range(2):
            update_screen(screen, sprite, cycle)
            cycle += 1
            #if cycle in [20, 60, 100, 140, 180, 220]:
            #    result += (_sum * cycle)
        number = int(command.split(' ')[1])
        _sum += number
        sprite = [_sum-1, _sum, _sum+1]
    draw_screen(screen)
    #print(result)

