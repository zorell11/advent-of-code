with open('input.txt', 'r') as f:
    data = f.read().splitlines()

ranges =[]

for line in data:
    if line == '':
        break    
    ranges.append(list(map(int,line.split('-'))))

ranges = sorted(ranges)
final_range = [ranges[0]]

for r in ranges[1:]:
    if r[0]>final_range[-1][1]:
        final_range.append(r)
    elif r[0] == final_range[-1][0] and r[1]< final_range[-1][1]:
        continue
    elif r[0] >= final_range[-1][0] and r[1] > final_range[-1][1]:
        new_item = [final_range[-1][0], r[1]]
        final_range.pop()
        final_range.append(new_item)

fresh_ingredients = 0
for item in final_range:
    fresh_ingredients += item[1] - item[0] +1
print(fresh_ingredients)