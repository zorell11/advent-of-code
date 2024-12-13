with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

sol = 0

def count_values():
    denominator = (x1 * y2 - y1 * x2)
    a = (z1 * y2 - z2 * x2) / denominator
    b = (x1 * z2 - y1 * z1) / denominator
    if a == int(a) and b == int(b) and 100 >= int(a) > 0 and 100 >= int(b) > 0:
        return int(a),int(b)
    return False

def get_values(line, delimeter):
    value = line.split(':')[1].split(',')
    x = int(value[0].split(delimeter)[1])
    y = int(value[1].split(delimeter)[1])
    return x,y 

for line in data:
    line = line.split('\n')
    for line1 in line:
        if line1.startswith('Button A'):
            x1, y1 = get_values(line1, '+')
        if line1.startswith('Button B'):
            x2, y2 = get_values(line1, '+')
        if line1.startswith('Prize'):
            z1, z2 = get_values(line1, '=')
    vals = count_values()
    if vals:
        sol += 3*vals[0] + 1*vals[1]

print(sol)        