import re
with open('input.txt', 'r') as f:
    data = f.read()

##### part1
pattern = r"mul\(\d{1,3},\d{1,3}\)"
found_patterns = re.findall(pattern, data)
solution1 = 0
for pattern in found_patterns:
    x, y = map(int, pattern.rstrip(')').lstrip('mul(').split(','))
    solution1 += x*y
print(solution1)

##### part 2
flag = 1
pattern = r"don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)"
found_patterns = re.findall(pattern, data)
solution2 = 0
for pattern in found_patterns:
    if pattern == 'do()':
        flag = 1
    elif pattern == 'don\'t()':
        flag = 0
    elif pattern.startswith('mul(') and flag:
        x, y = map(int, pattern.rstrip(')').lstrip('mul(').split(','))
        solution2 += x*y

print(solution2)