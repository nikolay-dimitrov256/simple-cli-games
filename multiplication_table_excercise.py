from random import randint


def multiply_check(a: int, b: int, guess: int) -> bool:
    result = a * b == guess

    return result


def main_function():
    number_of_guesses = 0
    correct_guesses = 0

    while True:
        a = randint(2, 9)
        b = randint(2, 9)

        players_guess = input(f'How much is {a} * {b}? Enter a number or [e]xit: ')

        if players_guess.lower() == 'e':
            break

        number_of_guesses += 1

        if players_guess.isdigit():
            players_guess = int(players_guess)

            if multiply_check(a, b, players_guess):
                print('Correct!')
                correct_guesses += 1
            else:
                print(f'Wrong. {a} * {b} = {a * b}')

        else:
            print('Invalid input. Still wrong.')

    print(f'\nYour score is {correct_guesses}/{number_of_guesses}')
    if 24 <= correct_guesses == number_of_guesses:
        print('Chad!')


print("Let's refresh your multiplication skills!\n")

main_function()
