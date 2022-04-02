# задание 5

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_joker(x):
    num_of_times = []
    for i in range(x):
        for_nouns = random.choice(nouns)
        for_adverbs = random.choice(adverbs)
        for_adjective = random.choice(adjectives)
        num_of_times.append(f'{for_nouns} {for_adverbs} {for_adjective}')
    return num_of_times
print(get_joker(3))

# не знал как сделать повторения, по этому подсмотрел у вас)
