with open('input.txt', 'r') as f:
    data = f.read().splitlines()

solution = 0
group_value = ''
for colummn_index in range(len(data[0])):
    if data[-1][colummn_index].strip():
        operator = data[-1][colummn_index]
    
    value = ''
    for row_index in range(len(data)-1):
        value += data[row_index][colummn_index]

    if value.strip():
        group_value += value.strip() + operator 
    else:
        solution += eval(group_value[:-1])
        group_value = ''
else:
    solution += eval(group_value[:-1])

print(solution)