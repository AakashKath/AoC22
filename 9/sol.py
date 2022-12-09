def update_direction(direction, hp):
    if direction == 'R':
        hp[1] += 1
    if direction == 'L':
        hp[1] -= 1
    if direction == 'U':
        hp[0] += 1
    if direction == 'D':
        hp[0] -= 1

def update_position(tracker, hp, tp, to_be_tracked):
    if abs(hp[0]-tp[0]) <= 1 and abs(hp[1]-tp[1]) <= 1:
        return
    if hp[0] == tp[0]:
        tp[1] += 1 if hp[1] > tp[1] else -1
    elif hp[1] == tp[1]:
        tp[0] += 1 if hp[0] > tp[0] else -1
    else:
        tp[0] += 1 if hp[0] > tp[0] else -1
        tp[1] += 1 if hp[1] > tp[1] else -1
    if to_be_tracked:
        tracker.add(tuple(tp))

with open('input', 'r') as file:
    x = file.readlines()
    position = [[0, 0] for _ in range(2)]
    tracker = set()
    tracker.add((0, 0))
    for i in x:
        direction, steps = i.split('\n')[0].split(' ')
        for j in range(int(steps)):
            for k in range(len(position)-1):
                if k == 0:
                    update_direction(direction, position[k])
                update_position(tracker, position[k], position[k+1],
                               True if k == len(position)-2 else False)
    print(len(tracker))

