with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

data = [ list(map(int, list(line))) for line in raw_data]

max_row = len(data[1])
max_col = len(data)

trailheads = {}
stack = []
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == 0:
            trailheads[(row, col)] = []
            stack.append((row, col))

for t_row, t_col in trailheads:
    stack = [(t_row, t_col)]
    while stack:
        row, col = stack.pop(-1)
        for r,c in [(0,1), (1,0), (0,-1), (-1,0)]:
            x,y = row+r, col+c
            if max_col > y > -1 and max_row > x >-1:
                if data[x][y] == data[row][col] +1 and data[x][y]!=9:
                    stack.append((x,y))
                elif data[x][y] == data[row][col] +1 and data[x][y]==9:
                    trailheads[(t_row, t_col)].append((x,y))

sol = 0
for i in trailheads:
    sol += len(trailheads[i])

print(sol)