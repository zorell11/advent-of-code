with open('input.txt', 'r') as f:
    data = f.read().splitlines()

total_joltage = []
for line in data:
    joltage_length = 12 - 1
    actual_joltage =''
    counter = 0
    while len(actual_joltage) < 12:
        counter +=1
        if joltage_length == len(line):
            actual_joltage += line
            break
        length_line = len(line)
        if joltage_length == 0:
            joltage = max(line[:])
        else:
            joltage = max(line[:-joltage_length])
        actual_joltage += joltage
        index = line.index(joltage)
        line = line[index+1:]
        joltage_length -=1
    total_joltage.append(int(actual_joltage))

print(sum(total_joltage))