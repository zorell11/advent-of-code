with open('input.txt', 'r') as f:
    initial = f.read().split()

N = 25

arrangement = []
for cycle in range(N):
    for stone in initial:
        if stone == '0':
            arrangement.append('1')
        elif len(stone)%2 == 0:
            lenght = len(stone)//2
            arrangement.extend([str(int(stone[:lenght])),str(int(stone[lenght:]))])
        else:
            arrangement.append(str(int(stone)*2024))
    initial = arrangement[:]
    arrangement = []

print(len(initial))