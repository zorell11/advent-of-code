with open('input.txt', 'r') as f:
    data = f.read()

sol = 0
for i,sign in enumerate(data):
    if data[i:i+4] == 'mul(':
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