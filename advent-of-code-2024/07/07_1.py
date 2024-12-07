from itertools import product

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

CHARS = ['+', '*']
solution = 0

for line in data:
    line_sum, numbers = line.split(':')
    line_sum = int(line_sum)
    numbers = list(map(int, numbers.split()))
    combinations = list(product(CHARS, repeat=len(numbers)-1))
    
    for combination in combinations:
        count_sum = numbers[0]
        inp = list(zip(numbers[1:], combination))
        for number, comb in inp:
            count_sum = eval(f'{count_sum}{comb}{number}')
            if count_sum == line_sum:
                solution += line_sum
                break
        else:
            continue
        break

print(solution)