with open('input.txt', 'r') as f:
    data = f.read().splitlines()

grid_x = 101
grid_y = 103
maximum = (-1, 0)
stats = []

for sec in range(grid_x * grid_y):
    q1 = q2 = q3 = q4 = 0 
    for line in data:
        position, velocity = line.split()
        position_x, position_y = tuple(map(int, position.strip('p=').split(',')))
        velocity_x, velocity_y = tuple(map(int, velocity.strip('v=').split(',')))
        
        position_x += sec*velocity_x 
        position_y += sec*velocity_y
        position_x %= grid_x
        position_y %= grid_y
        
        # if sec == 8053:
        #     stats.append((position_x, position_y))

        if position_x < grid_x//2 and position_y < grid_y//2:
            q1 += 1
        elif position_x > grid_x//2 and position_y < grid_y//2:
            q2 += 1
        elif position_x < grid_x//2 and position_y > grid_y//2:
            q3 += 1
        elif position_x > grid_x//2 and position_y > grid_y//2:
            q4 += 1
    max_q = max(q1, q2, q3, q4)

    if  max_q > maximum[1]:
        maximum = (sec, max_q)

print(maximum[0])

#print grid with christmas tree
# grid = [[" " for _ in range(grid_y)] for _ in range(grid_x)]
# for stat in stats:
#     grid[stat[0]][stat[1]] = '#'
# for line in grid:
#     print("".join(line))