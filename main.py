import random

def get_computer_choice():
    x = random.randint(1, 3)
    if x == 1:
        return 'ROCK'
    elif x == 2:
        return 'PAPER'
    else:
        return 'SCISSORS'


def start_game():
    player_choice = input('Choose ROCK, PAPER or SCISSORS: ').upper()
    computer_choice = get_computer_choice()

    if player_choice == 'ROCK' or player_choice == 'PAPER' or player_choice == 'SCISSORS':
        if player_choice == 'ROCK' and computer_choice == 'PAPER' or player_choice == 'PAPER' and computer_choice == 'SCISSORS' or player_choice == 'SCISSORS' and computer_choice == 'ROCK':
            print('You lost.!')
        elif player_choice == 'ROCK' and computer_choice == 'SCISSORS' or player_choice == 'PAPER' and computer_choice == 'ROCK' or player_choice == 'SCISSORS' and computer_choice == 'PAPER':
            print('You won.!')
        else:
            print('It was a draw.!')
    else:
        print('Invalid choice.!')
        return

    print('Your chose: ', player_choice)
    print('Computer chose: ', computer_choice)


start_game()