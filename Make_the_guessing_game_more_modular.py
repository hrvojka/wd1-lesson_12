import random
import json
import datetime
from operator import itemgetter


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort(key=itemgetter("attempts"))


def get_top_scores():
    for score_dict in score_list[0:3]:
        top_scores = f'NAME: {str(score_dict["name"])}, ATTEMPTS: {str(score_dict["attempts"])}, ' \
                     f'SECRET NUMBER: {str(score_dict["secret"])}, WRONG GUESSES: {str(score_dict["wrong_guesses"])},' \
                     f' DATE: {score_dict["date"]}'
        print(top_scores)


def play_game(level="E"):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    name = input("Name: ")
    while True:
        attempts += 1
        guess = int(input("Guess: "))
        if secret == guess:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses": wrong_guesses, "secret": secret})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "E":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "E":
            print("Your guess is not correct... try something bigger")
        else:
            print(f'{guess} is not the secret number.')
        wrong_guesses.append(guess)


def main():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores or C) quit?").upper()
        if selection == "A":
            level = input("Choose a level. E for easy, H for hard: ").upper()
            play_game(level=level)
        elif selection == "B":
            get_top_scores()
        else:
            break


if __name__ == "__main__":
    main()