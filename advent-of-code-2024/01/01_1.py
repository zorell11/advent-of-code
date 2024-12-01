with open('input', 'r') as f:
    data = f.read().splitlines()
sol = 0
col1, col2 = [], []
for line in data:
    col = line.split()
    col1.append(int(col[0]))
    col2.append(int(col[1]))

col1.sort()
col2.sort()

for index in range(len(col1)):
    sol += abs(col1[index] - col2[index])       

print(sol)