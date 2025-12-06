with open('input.txt', 'r') as f:
    data = f.read().splitlines()

worksheets = []
operators = data[-1].strip().split()
for line in data[:-1]:
    worksheets.append(list(map(int, line.strip().split())))

length = len(worksheets)
solution = []
for index in range(len(worksheets[0])):
    word = ''
    for i in range(length):
        x = str(worksheets[i][index])
        word = word + x + operators[index]
    solution.append(eval(word[:-1]))
print(sum(solution))