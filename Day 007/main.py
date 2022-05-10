# ==========================================
# Day 007 - Project: Hangman             
# ==========================================

import random


def logo():
    print("""
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/                       
    """)


def hint_generator(int):
    hint = ""
    for x in range(int):
        hint += "-"

    return list(hint)


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

current = 0
word_list = ["happened", "night", "citizen", "kane", "wizard", "modern", "times", "black", "panther", "parasite",
             "avengers"]
answer = random.choice(word_list)
answer_list = list(answer)

logo()
hint = hint_generator(len(answer))

while current < 6:
    print(HANGMANPICS[current])
    print("".join(hint))
    guess = input("Guess a Letter: ")
    if guess in answer:
        # find occurences and replace in hint
        for pos, char in enumerate(answer):
            if char == guess:
                hint[pos] = guess
        if (answer == "".join(hint)):
            print(f"*** You Won!. The word was: {answer} ***")
            break
    else:
        current += 1
        if current == 6:
            print(HANGMANPICS[current])
            print(f"You Lost!. The word was: {answer}")
