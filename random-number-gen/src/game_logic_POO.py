import random


class GuessGame:
    def __init__(self) -> None:
        self.score = 200
        self.exit_code = -1
        self.random_num = self._random_num_gen()

    def _random_num_gen(self) -> int:
        return random.randint(1, 100)

    def get_guessed_num(self) -> int:
        valid_numbers = list(range(1, 101))
        while True:
            try:
                n_guessed: int = int(input("Guess an integer (1-100): "))
            except ValueError:
                print("Invalid input. Enter a number.")
                continue
            if n_guessed in valid_numbers or n_guessed == self.exit_code:
                break
        print("\nn_guessed:", n_guessed)
        return n_guessed

    def play_round(self):
        is_alive = self.check_life()
        if is_alive:
            n_guessed = self.get_guessed_num()
            print("\nNew Round: ")
            print("Your Score:", self.score)
            print("To quit insert exit code: -1")
            if n_guessed == self.exit_code:
                print("Game Stopped.")
                return False
            if n_guessed != self.random_num:
                self.score -= 10
                print(f"Wrong guess! You lose 10 points. Current score: {self.score}")
                if n_guessed < self.random_num:
                    print("Hint: Number is bigger than guessed.")
                else:
                    print("Hint: Number is smaller than guessed.")
                return True
            else:
                return False
        else:
            print("You're Dead")
            return False

    def check_life(self):
        if self.score == 0:
            return False
        else:
            return True

    def start(self):
        print("Welcome to the Guess Game!")
        while True:
            print("\nNew Round")
            print("Current Score:", self.score)
            continue_game = self.play_round()
            if not continue_game:
                break
        print("Final Score:", self.score)


if __name__ == "__main__":
    game = GuessGame()
    game.start()
