with open('input.txt', 'r') as f:
    data = f.read().split(',')

invalid = []

for line in data:
    start, stop = line.split('-')
    for test_number in range(int(start), int(stop)+1):
        if len(str(test_number))//2 == 0:
            continue
        else:
            half = len(str(test_number))//2
            if str(test_number)[:half] == str(test_number)[half:]:
                invalid.append(test_number)

print(sum(invalid))