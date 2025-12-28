#hangman game
import random
from list import words

art = { 0: ("   ",
            "   ",
            "   "),
        1: (" O ",
            "   ",
            "   "),
        2: (" O ",
            " | ",
            "   "),
        3: (" O ",
            "/| ",
            "   "),
        4: (" O ",
            "/|\\",
            "   "),
        5: (" O ",
            "/|\\",
            "/  "),
        6: (" O ",
            "/|\\",
            "/ \\")}

def display_game(wrong):
    print("-------------")
    for line in art[wrong]:
        print(line)
    print("-------------")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong = 0
    guessed = set()
    is_running = True

    while is_running:
        display_game(wrong)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed:
            print(f"{guess} is already guessed")
            continue

        guessed.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong += 1

        if "_" not in hint:
            display_game(wrong)
            display_answer(answer)
            print("You guessed the word!!!")
            is_running = False
        elif wrong >= len(art) -1:
            display_game(wrong)
            display_answer(answer)
            print("You lose!")
            is_running = False
if __name__ == "__main__":
    main()
