import sys
import time


def turkish_upper(s):
    to_ret = ""
    for letter in s:
        if letter == "i":
            to_ret += "İ"
        else:
            to_ret += letter.upper()
    return to_ret


def get_output(words):
    output = ""
    for idx, word in enumerate(words):
        output += word
        if idx != len(words) - 1:
            output += "-"
    return output


def get_score(words):
    total_score = 0
    for word in words:
        score = 0
        for letter in word:
            score += letter_data[letter.upper()]
        score *= len(word)
        total_score += score

    return total_score


if len(sys.argv) != 3:
    print("You must write two arguments for this program.")
    exit()

words_file = open(sys.argv[1], "r", encoding="utf8")
letters_file = open(sys.argv[2], "r", encoding="utf-8-sig")

word_data = {}  # dictionary, keys: words, values: possible words
letter_data = {}  # dictionary, keys: letters, values: points.

for line in words_file.read().split('\n'):
    line.rstrip("\n")
    data = line.split(":")
    word_data[data[0]] = data[1].split(",")

for line in letters_file.readlines():
    data = line.split(":")
    letter_data[data[0]] = int(data[1])

words_file.close()
letters_file.close()

guesses = []
for word_key in word_data:
    initial_time = time.time()
    elapsed_time = 0
    print("Shuffled letters are {} please guess words for these letters, minimum 3 length.".format(word_key))
    while True:
        if elapsed_time > 30:
            print("Time is up.")
            if len(guesses) > 0:
                print("Score for {} is {}, and guessed words are: {}".format(word_key, get_score(guesses), get_output(guesses)))
            exit()
        user_guess = turkish_upper(input("Guessed word: "))
        elapsed_time = time.time() - initial_time
        if elapsed_time > 30:
            continue
        if user_guess in word_data[word_key]:
            if user_guess not in guesses:
                guesses.append(user_guess)
                print("Your guess is correct.")
            else:
                print("You have guessed this before.")
        else:
            print("Your guess is not correct.")
        print("You have {} seconds left.".format(max(0, int(30 - elapsed_time))))
        if len(guesses) == len(word_data[word_key]):    # everything is guessed, move to the next word.
            print("Score for {} is {}, and guessed words are: {}".format(word_key, get_score(guesses), get_output(guesses)))
            guesses = []  # reset this for the next word.
            break
