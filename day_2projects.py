'''Project 1: Number Guessing Game
Generate a random number using random.randint()
Ask the user to guess until they get it right
Give hints: too high / too low
Concepts used: input, conditionals, loops, functions, random module'''

import  random

attempt = 1
choice = random.randint(1,100)

while True:
    n = int(input("Enter your guess(1-100):"))
    attempt+=1
    if n < choice:
        print("too low! try again")
    elif n > choice:
        print("too high! try again")
    else:
        print(f"You have correctly guessed the number in {attempt} attempt")
        break
