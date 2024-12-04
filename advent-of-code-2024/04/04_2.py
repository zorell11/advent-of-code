with open('input.txt', 'r') as f:
    raw_data = f.read()

solution = 0
data = []
for line in raw_data.splitlines():
    data.append(line)

for row in range(1, len(data)-1):
    for column in range(1, len(data[0])-1):
        check = 0

        if data[row][column] == 'A':
            if data[row-1][column-1] == 'M' and data[row+1][column+1] =='S':
                check +=1
            if data[row-1][column-1] == 'S' and data[row+1][column+1] =='M':
                check +=1
            if data[row-1][column+1] == 'M' and data[row+1][column-1] =='S':
                check +=1
            if data[row-1][column+1] == 'S' and data[row+1][column-1] =='M':
                check +=1
            
        if check == 2:
            solution +=1

print(solution)