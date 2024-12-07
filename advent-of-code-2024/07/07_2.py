from itertools import product

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

CHARS = [' + ', ' * ', ' || ']
solution = 0

def evaluate_string(expression):
    exp = expression.split()
    result = int(exp[0])

    for i in range(1, len(exp), 2):
        operator = exp[i]
        number = int(exp[i+1])

        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        elif operator == '||':
            result = int(str(result)+str(number))
    return result

for i,line in enumerate(data):
    line_sum, numbers = line.split(':')
    line_sum = int(line_sum)
    numbers = numbers.split()
    combinations = list(product(CHARS, repeat=len(numbers)-1))

    expression = ''
    for combination in combinations:
        expression = ''
        expression += numbers[0]
        for i in range(len(combination)):
            expression += combination[i] + numbers[i+1]

        if evaluate_string(expression) == line_sum:
            solution += line_sum
            break

print(solution)