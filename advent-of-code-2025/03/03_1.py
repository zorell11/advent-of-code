with open('input.txt', 'r') as f:
    data = f.read().splitlines()

total_joltage = []
for line in data:
    maximum = max(line)
    last = len(line)-1
    joltage1_index = line.index(maximum)
    if joltage1_index == last:
        joltage2 = maximum
        joltage1 = max(line[:-1])
        total_joltage.append(int(joltage1+joltage2))
    else:
        joltage2 = max(line[joltage1_index+1:])
        total_joltage.append(int(maximum+joltage2))

print(sum(total_joltage))