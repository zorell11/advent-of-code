with open('input.txt', 'r') as f:
    data = f.read().split(',')

invalid = []

for line in data:
    start, stop = line.split('-')
    for test_number in range(int(start), int(stop)+1):
        length = len(str(test_number))
        if length == 1:
            continue

        if length%2 != 0 and length%3 == 0:
            if str(test_number)[:3]*3 == str(test_number):
                invalid.append(test_number)
                continue

        if length%2 != 0 or length == 2:
            if len(set(str(test_number))) == 1:
                invalid.append(test_number)
        else:
            half = length//2
            counter_half = half
            for i in range(2,half+1):
                if str(test_number)[:i]*counter_half == str(test_number):
                    invalid.append(test_number)
                    break
                counter_half -=1

print(sum(invalid))