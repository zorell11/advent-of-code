with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def check(line):
    res, res1, res2 = [], [], []
    for i in range(0,len(line)-1):
        res.append(line[i] - line[i+1])
    for i in res:
        if 1 <= i <= 3:
            res1.append(1)
        else:
            res1.append(0)
        
    if all(res1):
        return True

    for i in res:
        if -1 >= i >= -3:
            res2.append(1)
        else:
            res2.append(0)
    if all(res2):
        return True
    return False
        
sol = 0
for line in data:
    line = list(map(int, line.split()))

    if check(line):
        sol += 1
    else:
        for index in range(len(line)):
            new_line = line[:index]+line[index+1:]
            if check(new_line):
                sol +=1 
                break

print(sol)