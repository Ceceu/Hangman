import random


# updates guess_letters.
def update_guess_letters(guess_letter, guess_letters, secret_word):
    index = 1
    for letter in secret_word:
        if guess_letter == letter:
            guess_letters[index] = letter
        index += 1
    if "__" not in guess_letters:
        return True
    else:
        return False


# shows the status of the game.
def print_status(guess_letters, errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 0:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif errors == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    elif errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    else:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print(*guess_letters)
    print()


def play():
    print("\n[ Welcome to Hangman ]\n")
    secret_word = getWord()
    guess_letters = ["__" for letter in secret_word]
    guess_letters.insert(0, " | ")

    print_status(guess_letters, 0)

    win = False
    lost = False
    errors = 0

    print(secret_word)

    while not win and not lost:
        guess_letter = input("Give me a leter or give me coin: ").strip().upper()
        if guess_letter in secret_word:
            win = update_guess_letters(guess_letter, guess_letters, secret_word)
        else:
            errors += 1
            lost = errors == 7
        print_status(guess_letters, errors)


def getWord():
    words = []
    file = open("words.txt", "r")

    for line in file:
        words.append(line.strip())
    word = words[random.randint(0, len(words) - 1)]
    return word.upper()


if __name__ == '__main__':
    play()
