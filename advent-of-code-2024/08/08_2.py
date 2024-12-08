from collections import defaultdict
import math

with open('input.txt') as f:
    data = f.read().splitlines()

antennas = defaultdict(list)
antinodes = set()
diag_len = int(math.sqrt(len(data)**2 + len(data)**2)+1)

for row in range(len(data)):
    for column in range(len(data[0])):
        if data[row][column] != '.':
            antennas[data[row][column]].append((row, column))

def get_antinode(value_x,value_y):
    antinodes_f = set()
    for i in range(1,diag_len):
        xy = []
        for j in range(2):
            if value_x[j] > value_y[j]:
                x = value_x[j] + i*abs(value_x[j]-value_y[j])
            else:
                x = value_x[j] - i*abs(value_x[j]-value_y[j])
            if x <0 or x>len(data[0])-1:
                break 
            xy.append(x)  
        if len(xy) == 2: 
            antinodes_f.add((xy[0],xy[1]))
    if antinodes_f:
        return antinodes_f
    return False

for antenna in antennas.values():
    for i,value_x in enumerate(antenna[:-1]):
        for value_y in antenna[i+1:]:
            for _ in range(2):
                antinode = get_antinode(value_x, value_y)
                antinodes.add((value_x))
                antinodes.add((value_y))
                if antinode:
                    antinodes = antinodes | antinode
                value_x, value_y = value_y, value_x

print(len(antinodes))