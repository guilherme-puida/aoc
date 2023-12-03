with open('d2.txt') as f:
    games = f.read().strip().splitlines()

max_amount = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

possible = 0

for game in games:
    game_possible = True
    game_id, rounds = game.split(':')
    game_id = int(game_id.split(' ')[1])
    rounds = [x.strip() for x in rounds.split(';')]

    for r in rounds:
        cubes = [x.strip() for x in r.split(',')]
        for c in cubes:
            amount, color = c.split(' ')
            if int(amount) > max_amount[color]:
                game_possible = False

    if game_possible:
        possible += game_id

print('Part 1:', possible)

total_power = 0

for game in games:
    game_id, rounds = game.split(':')
    game_id = int(game_id.split(' ')[1])
    rounds = [x.strip() for x in rounds.split(';')]

    power = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for r in rounds:
        cubes = [x.strip() for x in r.split(',')]
        for c in cubes:
            amount, color = c.split(' ')

            power[color] = max(power[color], int(amount))

    total_power += power['red'] * power['green'] * power['blue']

print('Part 2:', total_power)
