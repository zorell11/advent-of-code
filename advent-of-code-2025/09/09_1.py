with open('input.txt', 'r') as f:
    data = f.read().splitlines()

print(data)

data = [ tuple(map(int, line.split(','))) for line in data ]

print(data)

largest_area = 0

for koor1,row in enumerate(data[:-1]):
    for koor2,column in enumerate(data[koor1+1:]):
        #print(row[0], row[1])
        #print(column[0], column[1])
        x = abs(row[0] - column[0]) +1 
        y = abs(row[1] - column[1]) +1
        area = x * y
        largest_area = max(largest_area, area)
print(largest_area)