from functools import cache

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = [ list(line) for line in data]
start_index = data[0].index('S')
data[1][start_index] = '|'
data = data[1:]

@cache
def solve(r,c):
    if r > len(data)-1:
        return 1
    if data[r][c] == '.':
        return solve(r+1, c)
    elif data[r][c] == '^':
        return solve(r+1, c-1) + solve(r+1, c+1)

sol = solve(1,start_index)