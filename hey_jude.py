# Have fun!


def verse(number: int):
    first_part = ''
    second_part = ''
    third_part = ''
    fourth_part = ''

    if number == 1:
        first_part = 'make it bad.'
        second_part = 'Take a sad song and make it better.'
        third_part = 'let her into your heart,'
        fourth_part = 'can start'

    elif number == 2:
        first_part = 'be afraid.'
        second_part = 'You were made to go out and get her.'
        third_part = 'let her under your skin,'
        fourth_part = 'begin'

    elif number == 3:
        first_part = 'let me down.'
        second_part = 'You have found her, now go and get her.'
        third_part = 'let her into your heart,'
        fourth_part = 'can start'

    elif number == 4:
        first_part = 'make it bad.'
        second_part = 'Take a sad song and make it better.'
        third_part = 'let her under your skin,'
        fourth_part = 'begin'

    print(f"Hey Jude, don't {first_part}")
    print(second_part)
    print(f"Remember to {third_part}")

    if number == 4:
        print(f"Then you {fourth_part} to make it")
        for _ in range(6):
            print("better", end=' ')
        print("oh.")
    else:
        print(f"Then you {fourth_part} to make it better.")

    print()


def bridge(number: int):
    if number == 1:
        print("And anytime you feel the pain, hey Jude, refrain,")
        print("Don't carry the world upon your shoulders.")
        print("For well you know that it's a fool who plays it cool")
        print("By making his world a little colder.")

    elif number == 2:
        print("So let it out and let it in, hey Jude, begin,")
        print("You're waiting for someone to perform with.")
        print("And don't you know that it's just you, hey Jude, you'll do,")
        print("The movement you need is on your shoulder.")

    print()


def chorus():
    for _ in range(11):
        print("na", end=' ')
    print()
    print("hey Jude...")
    print()


verse(1)
verse(2)
bridge(1)
verse(3)
bridge(2)
verse(4)
for _ in range(20):
    chorus()
