with open('input.txt') as f:
    data1 = f.read().splitlines()

data = []
for i in data1: 
    data.append(list(i))

final_solution = 0
removed = []

while True:
    solution = 0
    for row in range(len(data)):
        for column in range(len(data[0])):

            if data[row][column] != '@':
                continue 
            counter = 0
            # 1 hore
            if (row-1) >= 0:
                if data[row-1][column] == '@':
                    counter += 1
    
            #2 hore vpravo
            if (row-1) >= 0 and (column + 1) < (len(data[0])):
                if data[row-1][column+1] == '@':
                    counter += 1

            # 3 vpravo
            if (column + 1) < (len(data[0])):
                if data[row][column+1] == '@':
                    counter += 1
            
            # 4 vpravo dole
            if (row +1) < (len(data)) and (column + 1) < (len(data[0])):
                if data[row+1][column+1] == '@':
                    counter += 1
            
            # 5 dole
            if (row +1) < (len(data)):
                if data[row+1][column] == '@':
                    counter += 1
            
            # 6 dole vlavo
            if (row +1) < (len(data)) and (column-1) >= 0:
                if data[row +1][column-1] == '@':
                    counter += 1
            
            # 7 vlavo
            if (column-1) >= 0:
                if data[row][column-1] == '@':
                    counter += 1

            # 8 hore vlavo
            if (row-1) >= 0 and (column-1)>=0:
                if data[row-1][column-1] == '@':
                    counter += 1

            if counter < 4:
                solution += 1
                removed.append((row, column))
            counter = 0
    
    for r,c in removed:
        data[r][c] = 'X'
    removed = []

    # print picture/graph
    # for line in data:
    #     for sign in line:
    #         print(sign, end=' ')
    #     print()

    final_solution += solution
    if solution == 0:
        break

print(f'solution: {final_solution}')