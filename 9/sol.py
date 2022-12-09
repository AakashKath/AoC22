def update_position(direction, tracker, hp, tp):
    if direction == 'R':
        hp[1] += 1
    if direction == 'L':
        hp[1] -= 1
    if direction == 'U':
        hp[0] += 1
    if direction == 'D':
        hp[0] -= 1
    if abs(hp[0]-tp[0]) <= 1 and abs(hp[1]-tp[1]) <= 1:
        return
    if hp[0] == tp[0]:
        tp[1] += 1 if hp[1] > tp[1] else -1
    elif hp[1] == tp[1]:
        tp[0] += 1 if hp[0] > tp[0] else -1
    else:
        tp[0] += 1 if hp[0] > tp[0] else -1
        tp[1] += 1 if hp[1] > tp[1] else -1
    tracker.add(tuple(tp))

with open('input', 'r') as file:
    x = file.readlines()
    tp = [0, 0]
    hp = [0, 0]
    tracker = set()
    tracker.add(tuple(tp))
    for i in x:
        direction, steps = i.split('\n')[0].split(' ')
        for j in range(int(steps)):
            update_position(direction, tracker, hp, tp)
    print(len(tracker))

