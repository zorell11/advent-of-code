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

def sort_line(seq_line):
    while True:
        is_sorted = True
        for i in range(len(seq_line)-1):
            rule = rules.get(seq_line[i],[])
            if seq_line[i+1] not in rule:
                is_sorted = False
                seq_line[i], seq_line[i+1] = seq_line[i+1], seq_line[i]

        if is_sorted:
            return seq_line

flag = 0
for line in update:
    for i in range(0, len(line)-1):
        for j in range(i+1,len(line)):
            if line[j] not in rules[line[i]]:
                flag=1
                break
        if flag:
            sorted_line = sort_line(line)
            middle = len(sorted_line) // 2
            solution += int(sorted_line[middle])
            flag = 0
            break

print(solution)