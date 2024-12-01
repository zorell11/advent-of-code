with open('input', 'r') as f:
    data = f.read().splitlines()
sol = 0
col1, col2 = [], []
for line in data:
    col = line.split()
    col1.append(int(col[0]))
    col2.append(int(col[1]))


for col1_num in col1:
    sol += col1_num * col2.count(col1_num)     

print(sol)