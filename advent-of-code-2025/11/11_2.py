from functools import cache

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

rack = {}
visited = tuple()

for line in data:
    device, outputs = line.split(':')
    outputs = outputs.split()
    rack[device] = outputs

@cache
def solve(actual, visited):
    if actual == 'out':  
        if 'fft' in visited and 'dac' in visited:
            visited = tuple()
            return 1
        return 0
    sol = 0

    for n in rack[actual]:
        if n == 'fft' or n == 'dac':
            visited = visited + (n,)
        sol = sol + solve(n, visited)
        if n == 'fft' or n == 'dac':
            visited = visited[:-1]
    return sol

print(solve('svr',visited))