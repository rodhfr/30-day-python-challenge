import random


def getGuessdNum() -> int:
    valid_numbers = list(range(1, 101))
    while True:
        n_guessed: int = int(input("Guess an integer (1-100): "))
        if n_guessed in valid_numbers or n_guessed == -1:
            break
        print("Invalid number. Try Again. ")
    print("\nn_guessed:", n_guessed)
    return n_guessed


def rndGenNum() -> int:
    return random.randint(1, 100)


def main():
    n_guessed = -10000
    score = 1000
    exit_code = -1
    n_random = rndGenNum()
    while n_guessed != n_random and n_guessed != exit_code:
        print("\nNew Round: ")
        print("Your Score:", score)
        print("To quit insert -1")
        n_guessed = getGuessdNum()
        if n_guessed == -1:
            print("Game stopped")
            break
        is_wrong = n_guessed != n_random
        print(f"Is wrong? {is_wrong}")
        if is_wrong:
            points = 10
            print(f"You lose {points} points")
            score -= points
            print("\nHINT:")
            if n_random > n_guessed:
                print("Number is bigger than guessed")
            else:
                print("Number is lower than guessed")
        else:
            print("You Won")
    print("Your Final Score:", score)
