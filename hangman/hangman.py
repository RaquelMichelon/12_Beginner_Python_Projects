import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or " " in word:
        word = random.choice(words) 
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the words
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #to track what the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        #letters_used
        print("You have", lives, "lives left and you have used these letters: ", ''.join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word", " ".join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes one life away if it is wrong
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You've already choose this letter. Pick up another one!")
        else:
            print("Invalid character! Please, try again!")
    
    if lives == 0:
        print("You died! The word was", word)
    else:
        print("You guessed the word", word, "!!")

hangman()
