with open('input.txt', 'r') as f:
    data = f.read().splitlines()

print(data)

sol = 0
for line in data:
    line = list(map(int, line.split()))

    if line[0] > line[1]:
        check = 0
        for i in range(0,len(line)-1):
            if line[i] > line[i+1] and 1<=(line[i]-line[i+1]) and (line[i]-line[i+1])<=3:
                continue
            else: break
        else:
            sol += 1
    elif line[1] > line[0]:
        for i in range(0,len(line)-1):
            if line[i] < line[i+1] and 1<=(line[i+1]-line[i]) and (line[i+1]-line[i])<=3:
                continue
            else: break
        else:
            sol += 1
print(sol)