with open('d1.txt') as f:
    lines = f.read().strip().splitlines()

total = 0

for line in lines:
    numbers = [x for x in line if x in '0123456789']
    current_number = numbers[0] + numbers[-1]
    total += int(current_number)

print('part 1:', total)

total = 0

for line in lines:
    line = line.replace('zero', 'z0o')
    line = line.replace('one', 'o1e')
    line = line.replace('two', 't2o')
    line = line.replace('three', 't3e')
    line = line.replace('four', 'f4r')
    line = line.replace('five', 'f5e')
    line = line.replace('six', 's6x')
    line = line.replace('seven', 's7n')
    line = line.replace('eight', 'e8t')
    line = line.replace('nine', 'n9e')

    numbers = [x for x in line if x in '0123456789']
    current_number = numbers[0] + numbers[-1]
    total += int(current_number)

print('part 2:', total)
