with open('input.txt', 'r') as f:
    raw_data = f.read()

XMAS = 'XMAS'
solution = 0

data = []
for line in raw_data.splitlines():
    data.append(line)

for row in range(len(data)):
    for column in range(len(data[0])):
        if data[row][column:column+4] == XMAS:
            solution += 1

        if data[row][::-1][column:column+4] == XMAS:
            solution +=1

        word_down = ''
        for i in range(4):
            if row > len(data)-4:
                break
            word_down += data[row+i][column]
        if word_down == XMAS:
            solution += 1

        word_up = ''
        for i in range(4):
            if row < 3:
                continue
            word_up += data[row-i][column]
        if word_up == XMAS:
            solution += 1

        word_right_down = ''
        for i in range(4):
            if row > len(data)-4 or column >len(data[0])-4:
                break
            word_right_down += data[row+i][column+i]  
        if word_right_down == XMAS:
            solution += 1      
        
        word_left_down = ''
        for i in range(4):
            if row > len(data)-4 or column < 3:
                break
            word_left_down += data[row+i][column-i] 

        if word_left_down == XMAS:
            solution += 1  

        word_right_up = ''
        for i in range(4):
            if row < 3 or column > len(data[column])-4:
                continue
            word_right_up += data[row-i][column+i]
        if word_right_up == XMAS:
            solution += 1

        word_left_up = ''
        for i in range(4):
            if row < 3 or column < 3:
                continue
            word_left_up += data[row-i][column-i]
        if word_left_up == XMAS:
            solution += 1

print(solution)