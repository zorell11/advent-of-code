with open('input.txt', 'r') as f:
    data = f.read().splitlines()

actual = 50
counter = 0

for line in data:
    direction = line[0]
    number = int(line[1:])
    
    for _ in range(number):
        if direction == 'L':
            actual = (actual - 1 + 100)%100
        else:
            actual = (actual + 1)%100
        if actual == 0:
            counter += 1
print(counter)