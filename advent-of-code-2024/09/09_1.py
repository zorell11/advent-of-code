with open('input.txt', 'r') as f:
    data = f.read().strip()

checksum = 0
blocks = []
i = 0
for index,value in enumerate(data):
    if index%2 == 0:
        blocks.extend(int(value) * [i])
        i+=1
    else:
        blocks.extend(int(value)*['.'])

for i,value in enumerate(blocks):
    if value == '.':
        while True:
            num = blocks.pop(-1)
            if isinstance(num, int):
                try:
                    blocks[i] = num
                except IndexError:
                    blocks.append(num)
                break

for i, value in enumerate(blocks):
    checksum += i*value

print(checksum)