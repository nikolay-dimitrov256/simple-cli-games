import random


def get_random_word(words: list) -> str:
    random_word = random.choice(words)

    return random_word


names = ['Peter', 'Michelle', 'Jane', 'Steve', 'Mike', 'Eugene', 'Jedadiah', 'Maria']
towns = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Montana', 'Blagoevgrad']
verbs = ['eats', 'holds', 'plays with', 'brings', 'sleeps with', 'watches', 'works on', 'talks about']
nouns = ['stones', 'cake', 'apples', 'laptop', 'bikes', 'cats', 'dogs', 'swords', 'guns', 'roses']
adverbs = ['slowly', 'fast', 'diligently', 'warmly', 'sadly', 'happily', 'carelessly', 'lovingly', 'softly']
details = ['near the river', 'at home', 'in the park', 'at work', 'on a date', 'on a meeting']

while True:
    sentence = (f'{get_random_word(names)} from {get_random_word(towns)} {get_random_word(adverbs)} '
                f'{get_random_word(verbs)} {get_random_word(nouns)} {get_random_word(details)}.')

    print(sentence)

    user_input = input('Press [Enter] to generate a new one, or enter [e] to exit: ')

    if user_input.lower() == 'e':
        break
