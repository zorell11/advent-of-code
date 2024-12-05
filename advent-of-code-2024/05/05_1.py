with open('input.txt') as f:
    data = f.read()


solution =0 
raw_rules, raw_update = data.split('\n\n')

rules = {}

for i in raw_rules.splitlines():
    x, y = i.split('|')
    if x not in rules:
        rules[x] = []
    rules[x].append(y)
    
update = []
for line in raw_update.splitlines():
    update.append(line.split(','))

flag = 0
for line in update:
    for i in range(0, len(line)-1):
        for j in range(i+1,len(line)):
            rule = rules.get(line[i], [])
            if line[j] not in rule:
                flag=1
                break
        if flag:
            flag = 0
            break
    
    else:
        middle = len(line) // 2
        solution += int(line[middle])

print(solution)