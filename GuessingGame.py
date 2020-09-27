#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random
random_number = random.randint(1,100)
guesses = 0

try:
    print("The Guessing Game")
    print("Enter a number (1-100)\nThree Guesses Available!\n")
    
    while guesses < 3:
        guess = int(input("Guess: "))
        if guess == random_number:
            print(f"\nYou are correct! The lucky number was {random_number}.")
            break
        elif guess != random_number:
            guesses+=1
            if guess > random_number:
                print("Too High! Incorrect Answer.\n")
            elif guess < random_number:
                print("Too Low! Incorrect Answer.\n")
    else:
        print(f"\nToo many guesses! The lucky number was {random_number}")
except:
    print("Value must be an Integer!")
else:
    print("Thanks for playing the Guessing Game!")

