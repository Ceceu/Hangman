import random

def play ():
    print("\n[ Welcome to Hangman ]\n")
    secret_word = getWord()
    guess_letters = ["__" for letter in secret_word]
    print(secret_word)
    print(*guess_letters)

def getWord ():

    words = []
    file = open("words.txt", "r")

    for line in file:
        words.append(line.strip())
    word = words[random.randint(0, len(words)-1)]
    return word


if __name__ == '__main__':
    play()