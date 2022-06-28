# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:38:49 2022

@author: samue
"""

import random 


def intro():
    """Prints da rules"""
    print("Welcome to Sam Wong's bootleg Wordle, called Wongle")
    print('')
    print("in this game you attempt to guess a random 5 letter word, you have 6 attempts")
    print("")
    print("You must guess witha other 5 letter words")
    print("")
    
    
def rules():
    """reminds player of the rules"""
    print('If a letter is in the word and in the right place it will have sqaure brackets')
    print("if the word was crane and you guessed chimp, then it would return")
    print("[c](r)(a)(n)(e)")
    print("")
    print('If a letter is in the word but in the wrong place it will have squigly brackets')
    print("if the word was crane and you guessed among, then it would return")
    print("{a}(m)(o){n}(g)")
    print("")
    print('If a letter is not in the word  it will have round brackets')
    print("if the word was fishy and you guessed among, then it would return")
    print("(a)(m)(o)(n)(g)")
    print("")
    print("If you would like to see these rules again, simply enter 'rulez'")
    

def get_guess(num_tries, list_of_words):
    """wwww"""
    guess = (input(f"{num_tries} attempts remaining. Insert a 5 letter word: ")).lower()
    while len(guess) != 5 or guess not in list_of_words:
        if guess == 'rulez':
            rules()
        elif len(guess) != 5:
            print("Word needs to be 5 letters long!")
        elif guess not in list_of_words:
            print("Not a real word")
        guess = (input(f"{num_tries} attempts remaining. Insert a 5 letter word: ")).lower()
    return (letter_process(guess))



def letter_process(word):
    "Takes a word, returns a list of letters"
    letter_list = []
    for i in word:
        letter_list.append(i)
    return letter_list



def letter_checking(letters_guess, letters_word):
    """Takes a list of letters and checkes agasint target"""
    num_correct = 0
    msg = "" 
    for index in range(0, 5):
        if letters_guess[index] is letters_word[index]:
            #print(f"{letters_guess[index]} This is in the right place")
            msg += "[" + letters_guess[index] + "]"
            num_correct += 1
        elif letters_guess[index] in letters_word:
            if True is dupe_check(index, letters_guess, letters_word):
                #print(f"{letters_guess[index]} This is in the word but the wrong place")
                msg += "{" + letters_guess[index] + "}"
            else:
                #print(f"{letters_guess[index]} This letter is not in the word")
                msg += "(" + letters_guess[index] + ")"
        else:
            #print(f"{letters_guess[index]} This letter is not in the word")
            msg += "(" + letters_guess[index] + ")"
        if num_correct == 5:
            return True
    print(msg)
    return False
    

def dupe_check(index,letters_guess, letters_word):
    """handles duplicates"""
    dupe_guess = 0
    dupe_word = 0 
    for i in letters_guess[:index]:
        if i is letters_guess[index] and index != 0:
            dupe_guess += 1 
    for i in letters_word[:index]:
        if i is letters_guess[:index]:   
            dupe_word += 1 
    if dupe_word > dupe_guess:
        return False 
    else:
        return True
    
    
    
def win_message(num_tries):
    """prints winning messgae"""
    win_strings = [None,"Phew", "Getting close","Good","Great", "Amazing","Excellent"]
    print(win_strings[num_tries + 1]) 

    

def main():
    """Nytimes will copyright this"""
    list_of_words = (open('wordlist.txt').read().split())
    word = random.choice(list_of_words)
    letters_word = letter_process(word)
    num_tries = 6
    got_it = False
    intro()
    rules()
    while num_tries != 0 and got_it is False:
        letters_guess = get_guess(num_tries, list_of_words)
        got_it = letter_checking(letters_guess, letters_word)
        num_tries -=1
    if got_it is True:
        win_message(num_tries)
    elif num_tries == 0:
        print(f"Out of guesses, the word was {word}")

main()