def process_logs(
    logs: list[str]
) -> tuple[int, list[str], list[int], list[int], list[set[str]]]:
    players = []
    blocks_plased = []
    seconds_in_game = []
    achivements = []
    for i in logs:
        log = i.split(' ')
        time = [int(i) for i in log[1][:-1].split(':')]
        player = log[2][1:-2]
        event = log[3]
        seconds = time[2] + time[1]*60 + time[0] * 60*60

        if event == 'connected' and not(player in players):
            players.append(player)
            blocks_plased.append(0)
            seconds_in_game.append(seconds)
            achivements.append(set())
            continue

        player_index = players.index(player)

        if event == 'connected' and player in players:
            seconds_in_game[player_index] += seconds

        if event == 'block_placed':
            blocks_plased[player_index] += 1

        elif event == 'achievement_unlocked':
            achivements[player_index].add(log[4])

        elif event == 'disconnected':
            seconds_in_game[player_index] -= seconds

    seconds_in_game = [-i for i in seconds_in_game]
    return (sum(blocks_plased), players, seconds_in_game, blocks_plased, achivements)

with open(r'tests\minicraft_logs.txt') as f:
    logs = f.read().split('\n')

print(process_logs(logs))