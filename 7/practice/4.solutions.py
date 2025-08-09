# solution 1
import sys
import time
import random

# intro = """"
# ------------------------
#        Memory Game
# ------------------------
# save numbers in your
# memory, then we ask
# what was the numbers
# ------------------------
# """


# def check_answer(memory, answer):
#     if memory == answer:
#         print("you win correct answer!")
#     else:
#         print(f"you lose answer is: {' '.join(answer)}")


# def main():
#     print(intro)
#     while (1):
#         try:
#             memory = []
#             for _ in range(0, 3):
#                 random_number = random.randint(0, 9)
#                 memory.append(str(random_number))

#             print(f"numbers are: {' '.join(memory)}")
#             time.sleep(3)

#             for _ in range(10):
#                 print()

#             print("enter numbers or exit")

#             answer = input("> ")
#             if answer == "exit":
#                 exit()

#             answer = answer.split()

#             # answer = [int(num) for num in answer.split(" ")]
#             # answer = map(int,answer.split())

#             check_answer(memory, answer)

#         except Exception as e:
#             print(e)


# main()

# solution 2
class Config:
    INTRO = (
        "------------------------" + "\n"
        "       Memory Game      " + "\n"
        "------------------------" + "\n"
        " Save numbers in your   " + "\n"
        " memory, then we'll ask " + "\n"
        " what they were!        " + "\n"
        "------------------------" + "\n"
    )

    WIN_MESSAGE = "You win! Correct answer! 🎉"
    LOSS_MESSAGE = "You lose! The answer was:"
    SLEEP_TIME = 3
    NUMBER_COUNT = 3
    CLEAR_LINES = 20
    EXIT_KEYWORD = "exit"


class Game:
    def __init__(self, config):
        self.config = config

    def print_intro(self):
        print(self.config.INTRO)

    def generate_numbers(self):
        return [random.randint(0, 9) for _ in range(self.config.NUMBER_COUNT)]

    def pause_and_clear(self):
        time.sleep(self.config.SLEEP_TIME)
        print("\n" * self.config.CLEAR_LINES)

    def get_user_input(self):
        prompt = f"> Enter the numbers:"

        user_input = input(prompt)
        if user_input.strip().lower() == self.config.EXIT_KEYWORD:
            print("Goodbye!")
            sys.exit()

        try:
            answer = list(map(int, user_input.strip().split()))
            return answer
        except ValueError:
            print("Invalid input! Please enter numbers separated by spaces.")
            return self.get_user_input()

    def check_answer(self, memory, answer):
        return memory == answer

    def print_numbers(self, numbers):
        print("Numbers are: " + ' '.join(map(str, numbers)))

    def one_round(self):
        memory = self.generate_numbers()

        self.print_numbers(memory)

        self.pause_and_clear()

        answer = self.get_user_input()

        if self.check_answer(memory, answer):
            print(self.config.WIN_MESSAGE)
        else:
            print(f"{self.config.LOSS_MESSAGE} {' '.join(map(str, memory))}")

    def run(self):
        self.print_intro()
        while True:
            try:
                self.one_round()
            except Exception as e:
                print("Error in game:", e)
                break


# game 1
# config = Config()
# game = Game(config)
# game.run()

# game 2
config = Config()
config.NUMBER_COUNT = 5
game = Game(config)
game.run()
