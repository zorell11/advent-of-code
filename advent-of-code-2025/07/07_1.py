with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = [ list(line) for line in data]
start_index = data[0].index('S')
print(start_index)
data[1][start_index] = '|'

splitters = []


def print_graph():
    for line in data:
        print(line)

data = data[1:]
for index_row, row in enumerate(data):
    for index_column, sign in enumerate(row):
        if index_row+1 > len(data)-1:
            break 
        if sign == '|' and data[index_row+1][index_column] == '.':
            data[index_row+1][index_column] = '|'
        elif sign == '|' and data[index_row+1][index_column] == '^':
            data[index_row+1][index_column-1] = '|'
            data[index_row+1][index_column+1] = '|'
            splitters.append((index_row+1, index_column))
    # print_graph()
    # print(splitters)
    # input()
print(len(splitters))