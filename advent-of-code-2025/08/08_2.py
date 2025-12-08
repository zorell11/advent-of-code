import math
with  open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = [ list(map(int,line.split(','))) for line in data ]

cycles = round((len(data)*len(data)-1)/2)
distances = {}

def pytagoras(p1,p2):
    distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
    return round(distance,3)

for index1,item1 in enumerate(data[:-1], 0):
    for index2,item2 in enumerate(data[index1+1:], index1+1):
        distance = pytagoras(item1, item2)
        distances[(index1, index2)] = distance

sorted_distances = list(dict(sorted(distances.items(), key=lambda x: x[1])))
circuits = [list(sorted_distances[0])]

counter = 0 
for item in sorted_distances[1:cycles]:
    counter += 1
    indexes = []
    for circuit in circuits:
        if item[0] in circuit and item[1] in circuit:
            indexes = [1]
            break
        elif item[0] in circuit:
            circuit.append(item[1])
            indexes.append(circuits.index(circuit))
            continue
        elif item[1] in circuit:
            circuit.append(item[0])
            indexes.append(circuits.index(circuit))

    if len(indexes) == 0:       
        circuits.append(list(item))
    elif len(indexes) == 2:
        merge = set(circuits.pop(indexes[1]) + circuits.pop(indexes[0]))
        circuits.append(list(merge))

    if len(circuits) == 1 and len(circuits[0]) == len(data):

        print(f'solution: {data[item[0]][0] * data[item[1]][0]}')
        break