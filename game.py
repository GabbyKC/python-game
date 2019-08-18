game_running = True

while game_running == True:
    new_round = True

    player = {
        'name': 'Gabby',
        'attack': 10,
        'heal': 20,
        'health': 100
    }

    monster = {
        'name': 'MadMax',
        'attack': 12,
        'health': 100
    }

    print('---' * 7)
    print('Enter Player Name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select an action:')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            print('Heal Player')

        elif player_choice == '3':
            new_round = False
            game_running = False

        else:
            print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' +
                  str(player['health']) + ' health left')
            print(monster['name'] + ' has ' +
                  str(monster['health']) + ' health left')

        elif player_won:
            print(player['name'] + ' won!!')
            new_round = False

        elif monster_won:
            print('Noooooo... The Monster won!!')
            new_round = False
