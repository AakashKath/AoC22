with open("input", "r") as file:
    x = file.readlines()
    li = list()
    su = 0
    for i in x:
        if(i == "\n"):
            li.append(su)
            su = 0
            continue
        su += int(i.split("\n")[0])
    print(max(li))
    top3 = sorted(li, reverse=True)[:3]
    print(sum(top3))

