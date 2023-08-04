from random import randint

while True:
    secret_number = randint(1, 100)

    number_of_guesses = 0
    guessed_number = False

    while not guessed_number:
        player_guess = input('Guess the number (1-100) or [e]xit: ')
        if player_guess.lower() == 'e':
            exit()

        if player_guess.isdigit():
            player_guess = int(player_guess)
            number_of_guesses += 1

            if player_guess == secret_number:
                print(f"\nThat's right. The number is {secret_number}")
                if number_of_guesses == 1:
                    print('Awesome! You guessed it on the first try!')
                else:
                    print('Number of guesses:', number_of_guesses)
                guessed_number = True

            elif player_guess < secret_number:
                print('Try higher.')

            else:
                print('Try lower.')

        else:
            print('Invalid input. Try again.')

    next_try = input('\nTry again? [y]es / [n]o: ')

    while next_try.lower() not in ['y', 'n']:
        next_try = input('Please enter [y] or [n]: ')

    if next_try.lower() == 'n':
        break
