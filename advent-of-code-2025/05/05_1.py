with open('input.txt', 'r') as f:
    data = f.read().splitlines()

ids = []
ranges =[]
flag = True
for line in data:
        if line == '':
            flag = False
            continue
        if flag:
            ranges.append(tuple(map(int,line.split('-'))))
        else:
            ids.append(int(line))

counter = 0
for ingredient_id in ids:
    for r in ranges:
        if ingredient_id in range(r[0],r[1]+1):
            counter += 1
            break
    
print(counter)