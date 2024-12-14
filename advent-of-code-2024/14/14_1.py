with open('input.txt', 'r') as f:
    data = f.read().splitlines()

SECONDS = 100
# grid_x = 11 
# grid_y = 7
grid_x = 101
grid_y = 103
q1 = q2 = q3 = q4 = 0

for line in data:
    position, velocity = line.split()
    position_x, position_y = tuple(map(int, position.strip('p=').split(',')))
    velocity_x, velocity_y = tuple(map(int, velocity.strip('v=').split(',')))

    for _ in range(SECONDS):
        position_x += velocity_x 
        position_y += velocity_y
    position_x %= grid_x
    position_y %= grid_y

    if position_x < grid_x//2 and position_y < grid_y//2:
        q1 += 1
    elif position_x > grid_x//2 and position_y < grid_y//2:
        q2 += 1
    elif position_x < grid_x//2 and position_y > grid_y//2:
        q3 += 1
    elif position_x > grid_x//2 and position_y > grid_y//2:
        q4 += 1

print(q1*q2*q3*q4)