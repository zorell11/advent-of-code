with open('input.txt', 'r') as f:
    data = f.read().splitlines()

rack = {}

for line in data:
    device, outputs = line.split(':')
    outputs = outputs.split()
    rack[device] = outputs

def solve(actual):
    if actual == 'out':
        return 1
    sol = 0

    for n in rack[actual]:
        sol = sol + solve(n)
    return sol

print(solve('you'))
