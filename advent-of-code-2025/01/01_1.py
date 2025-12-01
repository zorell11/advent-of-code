with open('input.txt', 'r') as f:
    data = f.read().splitlines()

actual = 50
counter = 0

for line in data:
    direction = line[0]
    number = int(line[1:])
    if direction == 'L':
        actual = (actual - number)%100 
    else:
        actual = (actual + number)%100 
    if actual == 0:
        counter += 1
print(counter)