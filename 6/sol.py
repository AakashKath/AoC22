def countDis(x, limit):
    spark = ''
    count = 0
    for i in x:
        spark += i
        count += 1
        if len(spark) < limit:
            continue
        if len(spark) > limit:
            spark = spark[1:]
        if len(set(spark)) == limit:
            return count

with open('input', 'r') as file:
    x = file.read()
    print(countDis(x, 4))
    print(countDis(x, 14))

