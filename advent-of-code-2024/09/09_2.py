with open('input.txt', 'r') as f:
    data = f.read().strip()

checksum = 0
empty = []
i = 0
stats = {}
poz = 0
for index,value in enumerate(data):
    if index%2 == 0:
        stats[i] = (poz, int(value))
        i+=1
    else:
        if int(value) == 0:
            continue
        empty.append((poz, int(value)))
    poz +=int(value)

while i > 0:
    i -= 1
    stats_index, stats_lenght = stats[i]

    for index, (empty_index, empty_lenght) in enumerate(empty):
        if empty_index >= stats_index:
            empty = empty[:index]
            break
        if stats_lenght <= empty_lenght:
            stats[i] = (empty_index, stats_lenght)
            if stats_lenght == empty_lenght:
                empty.pop(index)
            else:
                empty[index] = (empty_index + stats_lenght, empty_lenght - stats_lenght)
            break

for i,(stat_index, stat_lenght) in stats.items():
    for j in range(stat_index, stat_index+stat_lenght):
        checksum += i * j 

print(checksum)
