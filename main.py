"""
Name(s):Charlotte, Alexandra
Name of Project:Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.


#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import page1
import random 
import os

ALL_GUESSES = []
number_of_answers = 3

difficulty = input("Choose a difficulty level: easier or harder:")

if difficulty == 'easier' or difficulty == 'Easier':
  word = random.choice(page1.easier)
if difficulty == 'harder' or difficulty == 'Harder':  
  word = random.choice(page1.harder)
characters = len(word)
print("there are", characters, "letters in this word. You have 10 tries to guess letters and 3 tries to guess the complete word at any point")


lis = list(word)

guess = input("Guess a letter/word:")
ALL_GUESSES.append(guess)




def provide_clue(word):
  masked_word = '_' * len(word)

  for g in ALL_GUESSES:
    p = -1
    if g in word:
      p = word.index(g)

    if p >= 0:
      temp = list(masked_word)
      temp[p] = g
      masked_word = "".join(temp)

  return masked_word

def clear_screen():
  os.system("clear")


while len(ALL_GUESSES) > 0 and number_of_answers > 0:
  position = -1

  if len(guess) == 1:
    if guess in lis:
      print("Correct")
      position = word.index(guess)
     
    else: 
      print("Incorrect")
      
  
  if len(guess) > 1:
    if guess == word:
      print("Congrats! You guessed the word!")
      break
    else: 
      print("Incorrect")
    number_of_answers = number_of_answers - 1
  
  if len(ALL_GUESSES) == 10:
    print("Oh no! You're out of guesses for letters :(")
    print("The word was:", word)
    break 

  if number_of_answers == 0: 
    print("Oh no! You're out of guesses for the word :(")
    print("The word was:", word)
    break

  
  
 
  

  progress = provide_clue(word)

  if progress == word:
      print("Congrats! You guessed it! The word was", word)
      break
  
  progress = f"Progress: {progress}"  
  msg = "Total guesses: %s" % len(ALL_GUESSES)
  msg += "\n%s\n" % ", ".join(ALL_GUESSES)

  clear_screen()
  guess = input(f"{progress}\n{msg}\n\nGuess another letter/word: ")
  ALL_GUESSES.append(guess)


  

 
  