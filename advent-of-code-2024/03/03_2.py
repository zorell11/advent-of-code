with open('input.txt', 'r') as f:
    data = f.read()

sol = 0
flag = 1
i = -1

while len(data) > i:
    i+=1
    if data[i:i+4] == 'do()' and data[i+3:i+8] != 'n\'t()':
        flag = 1

    if data[i:i+7] == 'don\'t()':
        flag = 0    

    if data[i:i+4] == 'mul(' and flag:
        index = i + 4
        if data[index:index+3].isdecimal():
            mul1 = int(data[index:index+3])
            index += 3
        elif data[index:index+2].isdecimal():
            mul1 = int(data[index:index+2])
            index += 2
        elif data[index:index+1].isdecimal():
            mul1 = int(data[index])
            index += 1
        else: continue

        if data[index] == ',':
            index +=1 
        else: continue

        if data[index:index+3].isdecimal():
            mul2 = int(data[index:index+3])
            index += 3
        elif data[index:index+2].isdecimal():
            mul2 = int(data[index:index+2])
            index += 2
        elif data[index:index+1].isdecimal():
            mul2 = int(data[index])
            index += 1

        if data[index] == ')':
            sol += (mul1 * mul2)
        
print(sol)