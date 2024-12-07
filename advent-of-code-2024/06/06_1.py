with open('input.txt', 'r') as f:
    data = f.read().splitlines()

rotate = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def get_direction(rotation):
    if rotation == '^':
        r,c = -1, 0
    elif rotation == '>':
        r,c = 0, 1
    elif rotation == 'v':
        r,c = 1, 0
    elif rotation == '<':
        r,c = 0, -1
    return r,c

for r in range(len(data)): 
    for c in range(len(data[0])):
        if data[r][c] in '^>v<':
            start = r,c
            break
    else:
        continue
    break

visited = {start}
direction = data[start[0]][start[1]]
r, c = get_direction(direction)
actual = start
while True:
    if (0 > actual[0]+r) or  (actual[0]+r > (len(data)-1)) or (0 > actual[1]+c) or  (actual[1]+c > (len(data[0])-1)):
        break
    elif data[actual[0]+r][actual[1]+c] == '#':
        direction = rotate[direction]
        r, c = get_direction(direction)
    
    visited.add((actual[0]+r,actual[1]+c))
    actual = actual[0]+r, actual[1]+c
        
print(len(visited))