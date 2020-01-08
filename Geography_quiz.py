
def quiz():
    import random
    countries_dict = {"Croatia": "Zagreb", "Spain": "Madrid", "Austria": "Vienna", "Slovenia": "Ljubljana",
                      "Italy": "Rome", "Germany": "Berlin", "France": "Paris", "Hungary": "Budapest"}

    for key, value in countries_dict.items():
        key = random.choice(list(countries_dict))
        command = (input(f'> Game: What is the capital city of {key}? \nUser: ')).title()
        if command == countries_dict[key]:
            return f'> Game: This is correct.'
        else:
            return f'> Game: This is not correct.'


print(quiz())
