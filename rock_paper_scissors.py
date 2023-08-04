from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
wins = 0
losses = 0
draws = 0

while True:
    player_choice = input('Enter [r]ock, [p]aper, [s]cissors, or [e]xit: ')
    if player_choice.lower() == 'e':
        break

    if player_choice.lower() == 'r':
        player_choice = rock
    elif player_choice.lower() == 'p':
        player_choice = paper
    elif player_choice.lower() == 's':
        player_choice = scissors
    else:
        print('Invalid input. Try again.')
        continue

    computer_choice = randint(1, 3)

    if computer_choice == 1:
        computer_choice = rock
    elif computer_choice == 2:
        computer_choice = paper
    elif computer_choice == 3:
        computer_choice = scissors

    if (player_choice == rock and computer_choice == scissors) \
            or (player_choice == paper and computer_choice == rock) \
            or (player_choice == scissors and computer_choice == paper):
        print('You win!')
        wins += 1

    elif player_choice == computer_choice:
        print('Draw!')
        draws += 1

    else:
        print('You lose!')
        losses += 1

print('Your score:\n')
print('Wins:', wins)
print('Draws:', draws)
print('Losses:', losses)
